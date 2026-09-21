from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.models import Package
from app.schemas.schemas import PackageResponse

router = APIRouter(prefix="/packages", tags=["Packages"])

DEFAULT_PACKAGES = [
    {
        "id": 1,
        "name": "Royal Luxury Package",
        "tier_slug": "high",
        "badge_text": "High Package",
        "starting_price": 350000.0,
        "base_price": 150000.0,
        "description": "Grand stage decor, premium imported floral setups, 4K cinematic videography, drone coverage, and lavish multi-course buffet catering.",
        "image_url": "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=80"
    },
    {
        "id": 2,
        "name": "Standard Classic Package",
        "tier_slug": "medium",
        "badge_text": "Medium Package",
        "starting_price": 120000.0,
        "base_price": 75000.0,
        "description": "Elegant flower arc background, candid photography, professional sound & DJ setup, theme cake table, and quality catering service.",
        "image_url": "https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=1200&q=80"
    },
    {
        "id": 3,
        "name": "Budget Friendly Package",
        "tier_slug": "low",
        "badge_text": "Low Package",
        "starting_price": 25000.0,
        "base_price": 30000.0,
        "description": "Minimalist stage backdrop setup, balloon arches, focus LED lighting, and basic audio equipment suitable for small home events.",
        "image_url": "https://images.unsplash.com/photo-1513151233558-d860c5398176?auto=format&fit=crop&w=1200&q=80"
    }
]

@router.get("", response_model=List[PackageResponse])
def get_packages(db: Session = Depends(get_db)):
    return DEFAULT_PACKAGES

@router.get("/{tier_slug}", response_model=PackageResponse)
def get_package_by_slug(tier_slug: str, db: Session = Depends(get_db)):
    for pkg in DEFAULT_PACKAGES:
        if pkg["tier_slug"].lower() == tier_slug.lower():
            return pkg
    return DEFAULT_PACKAGES[0]
