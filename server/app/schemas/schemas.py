from typing import List, Optional, Any
from pydantic import BaseModel, EmailStr

# Auth Schemas
class UserRegister(BaseModel):
    firstName: str
    lastName: str
    username: str
    email: EmailStr
    age: int
    password: str
    confirmPassword: Optional[str] = None
    otp: Optional[str] = None
    role: Optional[str] = "USER"

class UserLogin(BaseModel):
    username: str  # Can be username or email
    password: str

class UserResponse(BaseModel):
    id: int
    username: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: str = "USER"

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

class SendOTPRequest(BaseModel):
    email: EmailStr

class VerifyOTPRequest(BaseModel):
    email: EmailStr
    otp: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr
    otp: str
    new_password: str

# Catalog Schemas
class ServiceResponse(BaseModel):
    id: int
    name: str
    category: str
    description: Optional[str] = None
    starting_price: float
    price_unit: Optional[str] = "flat"
    image_url: Optional[str] = None

    class Config:
        from_attributes = True

class PackageResponse(BaseModel):
    id: int
    name: str
    tier_slug: str
    badge_text: str
    starting_price: float
    base_price: float
    description: Optional[str] = None
    image_url: Optional[str] = None

    class Config:
        from_attributes = True

# Booking Schemas
class BookingCalculateRequest(BaseModel):
    package_tier: str  # "high", "medium", "low"
    needs_values: List[int] = []
    from_date: Optional[str] = None
    to_date: Optional[str] = None

class BookingCalculateResponse(BaseModel):
    duration_days: int
    base_amount: float
    add_ons_total: float
    total_estimated_amount: float
    formatted_total: str

class BookingCreateRequest(BaseModel):
    package_tier: str
    fullName: str
    mobileNo: str
    altMobileNo: Optional[str] = None
    emailAddr: EmailStr
    functionType: str
    needs: List[str] = []
    districtSelect: str
    place: str
    fullAddress: str
    pincode: str
    fromDate: str
    toDate: str
    fromTime: str
    toTime: str
    mapLocation: str
    estimatedAmount: Optional[float] = None

class BookingResponse(BaseModel):
    id: int
    booking_reference: Optional[str] = None
    package_tier: Optional[str] = None
    full_name: Optional[str] = None
    mobile_no: Optional[str] = None
    alt_mobile_no: Optional[str] = None
    email: Optional[str] = None
    function_category: Optional[str] = None
    district: Optional[str] = None
    place_area: Optional[str] = None
    full_address: Optional[str] = None
    pincode: Optional[str] = None
    from_date: Optional[str] = None
    to_date: Optional[str] = None
    from_time: Optional[str] = None
    to_time: Optional[str] = None
    duration_days: Optional[int] = 1
    map_location_url: Optional[str] = None
    selected_needs: Optional[str] = None
    status: str = "UPCOMING"
    total_amount: Optional[float] = 0.0
    created_at: Optional[Any] = None

    class Config:
        from_attributes = True

class StatusUpdateRequest(BaseModel):
    status: str  # UPCOMING, COMPLETED, CANCELLED

class AdminStatsResponse(BaseModel):
    total_bookings: int
    total_revenue: float
    upcoming_bookings: int
    completed_bookings: int
    cancelled_bookings: int
    total_customers: int
