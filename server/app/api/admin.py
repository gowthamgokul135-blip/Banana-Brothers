from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.core.security import require_admin
from app.models.models import Booking, User
from app.schemas.schemas import AdminStatsResponse, BookingResponse, StatusUpdateRequest, UserResponse

router = APIRouter(prefix="/admin", tags=["Admin Portal"])

@router.get("/stats", response_model=AdminStatsResponse)
def get_admin_stats(db: Session = Depends(get_db), current_admin: User = Depends(require_admin)):
    total_bookings = db.query(Booking).count()
    upcoming_bookings = db.query(Booking).filter(Booking.status == "UPCOMING").count()
    completed_bookings = db.query(Booking).filter(Booking.status == "COMPLETED").count()
    cancelled_bookings = db.query(Booking).filter(Booking.status == "CANCELLED").count()
    
    total_rev = db.query(func.sum(Booking.total_amount)).filter(Booking.status != "CANCELLED").scalar() or 0.0
    total_customers = db.query(User).filter(User.role == "USER").count()

    return AdminStatsResponse(
        total_bookings=total_bookings,
        total_revenue=float(total_rev),
        upcoming_bookings=upcoming_bookings,
        completed_bookings=completed_bookings,
        cancelled_bookings=cancelled_bookings,
        total_customers=total_customers
    )

@router.get("/bookings", response_model=List[BookingResponse])
def get_all_bookings(
    status_filter: Optional[str] = Query(None, alias="status"),
    q: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_admin: User = Depends(require_admin)
):
    query = db.query(Booking)
    
    if status_filter and status_filter.upper() != "ALL":
        query = query.filter(Booking.status == status_filter.upper())
        
    if q:
        search_term = f"%{q.strip()}%"
        query = query.filter(
            (Booking.booking_reference.ilike(search_term)) |
            (Booking.full_name.ilike(search_term)) |
            (Booking.email.ilike(search_term)) |
            (Booking.mobile_no.ilike(search_term)) |
            (Booking.district.ilike(search_term)) |
            (Booking.function_category.ilike(search_term))
        )
        
    bookings = query.order_by(Booking.id.desc()).all()
    
    return [
        BookingResponse(
            id=b.id,
            booking_reference=b.booking_reference,
            package_tier=b.package_tier,
            full_name=b.full_name,
            mobile_no=b.mobile_no,
            alt_mobile_no=b.alt_mobile_no,
            email=b.email,
            function_category=b.function_category,
            district=b.district,
            place_area=b.place_area,
            full_address=b.full_address,
            pincode=b.pincode,
            from_date=b.from_date,
            to_date=b.to_date,
            from_time=b.from_time,
            to_time=b.to_time,
            duration_days=b.duration_days,
            map_location_url=b.map_location_url,
            selected_needs=b.selected_needs,
            status=b.status,
            total_amount=float(b.total_amount or 0.0),
            created_at=b.created_at.isoformat() if b.created_at else None
        )
        for b in bookings
    ]

@router.get("/bookings/{booking_id}", response_model=BookingResponse)
def get_booking_detail(
    booking_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(require_admin)
):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    
    return BookingResponse(
        id=booking.id,
        booking_reference=booking.booking_reference,
        package_tier=booking.package_tier,
        full_name=booking.full_name,
        mobile_no=booking.mobile_no,
        alt_mobile_no=booking.alt_mobile_no,
        email=booking.email,
        function_category=booking.function_category,
        district=booking.district,
        place_area=booking.place_area,
        full_address=booking.full_address,
        pincode=booking.pincode,
        from_date=booking.from_date,
        to_date=booking.to_date,
        from_time=booking.from_time,
        to_time=booking.to_time,
        duration_days=booking.duration_days,
        map_location_url=booking.map_location_url,
        selected_needs=booking.selected_needs,
        status=booking.status,
        total_amount=float(booking.total_amount or 0.0),
        created_at=booking.created_at.isoformat() if booking.created_at else None
    )

@router.patch("/bookings/{booking_id}/status")
def update_booking_status(
    booking_id: int,
    payload: StatusUpdateRequest,
    db: Session = Depends(get_db),
    current_admin: User = Depends(require_admin)
):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    
    new_status = payload.status.upper()
    if new_status not in ["UPCOMING", "COMPLETED", "CANCELLED"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid status. Must be UPCOMING, COMPLETED, or CANCELLED.")
    
    booking.status = new_status
    db.commit()
    db.refresh(booking)
    
    return {
        "success": True,
        "message": f"Booking {booking.booking_reference} status updated to {new_status}",
        "booking_id": booking.id,
        "status": booking.status
    }

@router.get("/users", response_model=List[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_admin: User = Depends(require_admin)
):
    users = db.query(User).order_by(User.id.desc()).all()
    return [
        UserResponse(
            id=u.id,
            username=u.username,
            email=u.email,
            first_name=u.first_name,
            last_name=u.last_name,
            role=u.role
        )
        for u in users
    ]
