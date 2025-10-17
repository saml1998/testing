# backend/app/routes/platforms_mapping.py
from fastapi import APIRouter
import pandas as pd

router = APIRouter(prefix="/mapping", tags=["mapping"])

@router.get("/platforms")
def get_platforms():
    df = pd.read_excel("backend/app/data/platform_practice_offering.xlsx")
    platforms = (
        df[["platform_code", "platform_name"]]
        .drop_duplicates()
        .to_dict(orient="records")
    )
    return platforms

@router.get("/practices/{platform_code}")
def get_practices(platform_code: str):
    df = pd.read_excel("backend/app/data/platform_practice_offering.xlsx")
    practices = (
        df[df["platform_code"] == platform_code][["practice_code", "practice_name"]]
        .drop_duplicates()
        .to_dict(orient="records")
    )
    return practices

@router.get("/offerings/{platform_code}/{practice_code}")
def get_offerings(platform_code: str, practice_code: str):
    df = pd.read_excel("backend/app/data/platform_practice_offering.xlsx")
    filtered = df[
        (df["platform_code"] == platform_code)
        & (df["practice_code"] == practice_code)
    ][["offering_code", "offering_name"]].drop_duplicates()
    return filtered.to_dict(orient="records")
#pello