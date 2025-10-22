
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.platform import Practice  

@router.get("/practices/{platform_code}")
def get_practices_by_platform(platform_code: str, db: Session = Depends(get_db)):
    """
    Fetch all practices for a specific platform using its platform_code.
    Example: /platforms/practices/OPM_001
    """
    try:
        practices = db.query(Practice).filter(Practice.platform_code == platform_code).all()
        return [
            {"practice_code": p.practice_code, "practice_name": p.practice_name}
            for p in practices
        ]
    except Exception as e:
        print("Error fetching practices:", e)
        return []

