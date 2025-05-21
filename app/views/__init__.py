# # from app.views.rbac import router as rbac_router

# # router = rbac_router
# # app/views/__init__.py

# from fastapi import APIRouter
# from app.views.rbac import router

# # create a root router
# router = APIRouter()

# # mount the RBAC router under "/rbac"
# # so endpoints become: /api/rbac/roles, /api/rbac/permissions, etc.
# router.include_router(
#     rbac_router,
#     prefix="/rbac",
#     tags=["rbac"],
# )

# app/views/__init__.py

from fastapi import APIRouter
from app.views.rbac import router as rbac_router  # ← import it here!

router = APIRouter()

# mount your RBAC endpoints under /rbac
router.include_router(
    rbac_router,
    prefix="/rbac",
    tags=["rbac"],
)
