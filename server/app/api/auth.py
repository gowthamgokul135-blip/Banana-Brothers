from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import verify_password, get_password_hash, create_access_token, get_current_user
from app.models.models import User
from app.schemas.schemas import UserRegister, UserLogin, TokenResponse, UserResponse, SendOTPRequest, VerifyOTPRequest, ForgotPasswordRequest
from app.models.models import OTPVerification
from app.core.config import settings
import smtplib
from email.mime.text import MIMEText
import random
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/send-otp")
def send_otp(payload: SendOTPRequest, db: Session = Depends(get_db)):
    db.query(OTPVerification).filter(OTPVerification.email == payload.email).delete()
    
    otp_code = f"{random.randint(100000, 999999)}"
    expires_at = datetime.utcnow() + timedelta(minutes=5)
    
    new_otp = OTPVerification(email=payload.email, otp_code=otp_code, expires_at=expires_at, is_used=0)
    db.add(new_otp)
    db.commit()
    
    try:
        msg = MIMEText(f"Your Banana Brothers verification code is: {otp_code}\n\nIt expires in 10 minutes.")
        msg['Subject'] = 'Your OTP Verification Code'
        msg['From'] = settings.SMTP_FROM_EMAIL
        msg['To'] = payload.email

        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"SMTP Error: {e}")
        db.delete(new_otp)
        db.commit()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to send OTP via email.")
        
    return {"message": "OTP sent successfully to your email!", "email": payload.email}

@router.post("/verify-otp")
def verify_otp(payload: VerifyOTPRequest, db: Session = Depends(get_db)):
    stored_otp = db.query(OTPVerification).filter(
        OTPVerification.email == payload.email,
        OTPVerification.otp_code == payload.otp,
        OTPVerification.is_used == 0,
        OTPVerification.expires_at > datetime.utcnow()
    ).first()
    
    if not stored_otp:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired OTP")
        
    if stored_otp:
        stored_otp.is_used = 1
        db.commit()
        
    return {"message": "OTP verified successfully!", "verified": True}

@router.post("/register", response_model=TokenResponse)
def register(payload: UserRegister, db: Session = Depends(get_db)):
    if not payload.otp:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="OTP is required")

    stored_otp = db.query(OTPVerification).filter(
        OTPVerification.email == payload.email,
        OTPVerification.otp_code == payload.otp,
        OTPVerification.is_used == 1,
        OTPVerification.expires_at > datetime.utcnow()
    ).first()
    
    if not stored_otp:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please verify your OTP first")
            
    # Check if username exists
    if db.query(User).filter(User.username == payload.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username is already taken")
    
    # Check if email exists
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is already registered")

    user_role = "ADMIN" if payload.role and payload.role.upper() == "ADMIN" else "USER"

    user = User(
        name=f"{payload.firstName} {payload.lastName}",
        first_name=payload.firstName,
        last_name=payload.lastName,
        username=payload.username,
        email=payload.email,
        age=payload.age,
        role=user_role,
        password_hash=get_password_hash(payload.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    stored_otp = db.query(OTPVerification).filter(
        OTPVerification.email == payload.email,
        OTPVerification.otp_code == payload.otp
    ).first()
    if stored_otp:
        db.delete(stored_otp)
        db.commit()

    access_token = create_access_token(data={"sub": str(user.id), "username": user.username, "role": user.role})
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            role=user.role
        )
    )

@router.post("/login", response_model=TokenResponse)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(
        (User.username == payload.username) | (User.email == payload.username)
    ).first()

    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    access_token = create_access_token(data={"sub": str(user.id), "username": user.username, "role": user.role})
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            first_name=user.first_name or "",
            last_name=user.last_name or "",
            role=user.role
        )
    )

@router.get("/me", response_model=UserResponse)
def get_current_user_profile(current_user: User = Depends(get_current_user)):
    return UserResponse(
        id=current_user.id,
        username=current_user.username,
        email=current_user.email,
        first_name=current_user.first_name or "",
        last_name=current_user.last_name or "",
        role=current_user.role
    )

@router.post("/forgot-password")
def forgot_password(payload: ForgotPasswordRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No account registered with this email")
        
    if not payload.otp:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="OTP is required")

    stored_otp = db.query(OTPVerification).filter(
        OTPVerification.email == payload.email,
        OTPVerification.otp_code == payload.otp,
        OTPVerification.is_used == 1,
        OTPVerification.expires_at > datetime.utcnow()
    ).first()
    
    if not stored_otp:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please verify your OTP first")
        
    db.delete(stored_otp)

    user.password_hash = get_password_hash(payload.new_password)
    db.commit()
    return {"message": "Password has been successfully reset! You can now login.", "success": True}
