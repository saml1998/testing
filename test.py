
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Practice(Base):
    __tablename__ = "practice"

    id = Column(Integer, primary_key=True, index=True)
    practice_code = Column(String, unique=True, index=True)
    practice_name = Column(String)
    platform_code = Column(String, ForeignKey("platform.platform_code"))
