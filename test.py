from fastapi import APIRouter
from typing import List, Dict, Any
from app.utils.catalogs_ado import CatalogsADO

router = APIRouter(prefix="/catalogs", tags=["Catalogs"])
catalogs_ado = CatalogsADO()

@router.get("/platforms")
async def get_platforms() -> List[Dict[str, Any]]:
    return await catalogs_ado.get_platforms()

@router.get("/practices/{platform_id}")
async def get_practices(platform_id: int) -> List[Dict[str, Any]]:
    return await catalogs_ado.get_practices(platform_id)

@router.get("/offerings/{practice_id}")
async def get_offerings(practice_id: int) -> List[Dict[str, Any]]:
    return await catalogs_ado.get_offerings(practice_id)


















