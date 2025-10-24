from fastapi import FastAPI
from app.routes.catalogs import router as catalogs_router

app = FastAPI()
app.include_router(catalogs_router)

















