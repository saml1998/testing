from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Practice

router = APIRouter()

@router.get("/practices/{platform_code}")
def get_practices_by_platform(platform_code: str, db: Session = Depends(get_db)):
    practices = db.query(Practice).filter(Practice.platform_code == platform_code).all()
    return [{"practice_code": p.practice_code, "practice_name": p.practice_name} for p in practices]



