from fastapi import APIRouter, Query
from app.utils.catalogs_ado import CatalogsADO

router = APIRouter(prefix="/catalogs", tags=["catalogs"])
ado = CatalogsADO()

@router.get("/platforms")
async def get_platforms():
    return await ado.get_platforms()

@router.get("/practices")
async def get_practices(platform_id: int = Query(..., gt=0)):
    return await ado.get_practices(platform_id)

@router.get("/offerings")
async def get_offerings(practice_id: int = Query(..., gt=0)):
    return await ado.get_offerings(practice_id)
















