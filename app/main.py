# from fastapi import FastAPI
# from app.views import router as api_router

# app = FastAPI(title="Mobile Device Management RBAC API")

# app.include_router(api_router)

# from fastapi import FastAPI
# from app.views import router as api_router

# # bring in DB core
# from app.database import engine, Base
# import app.models.rbac   # ← ensures all ORM models are registered

# Base.metadata.create_all(bind=engine)  # skip if you use Alembic

from fastapi import FastAPI
from app.core.database import engine, Base
import app.models.rbac       # register ORM models

from app.views import router as api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mobile Device Management – RBAC API",
    version="1.0.0",
    description="Manage devices and permissions with hierarchical RBAC"
)
app.include_router(api_router, prefix="/api", tags=["rbac"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)

