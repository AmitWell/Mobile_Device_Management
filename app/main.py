from fastapi import FastAPI
from app.views import router as api_router

app = FastAPI(title="Mobile Device Management RBAC API")

app.include_router(api_router)
