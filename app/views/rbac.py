# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from app.core.database import SessionLocal
# from app.schemas.rbac import Role, Permission, UserRole
# from app.viewmodels.rbac import RoleViewModel, PermissionViewModel, UserRoleViewModel
# from app.core.auth import verify_token

# router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.get("/roles", response_model=list[Role])
# def list_roles(db: Session = Depends(get_db), token: dict = Depends(verify_token)):
#     return RoleViewModel(db).get_roles()

# @router.get("/permissions", response_model=list[Permission])
# def list_permissions(db: Session = Depends(get_db), token: dict = Depends(verify_token)):
#     return PermissionViewModel(db).get_permissions()

# @router.get("/user_roles/{user_id}", response_model=list[UserRole])
# def list_user_roles(user_id: int, db: Session = Depends(get_db), token: dict = Depends(verify_token)):
#     return UserRoleViewModel(db).get_user_roles(user_id)

# app/views/rbac.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import APIRouter

# 1) Import the shared get_db
from app.core.database import get_db

# 2) Your Pydantic schemas (adjust names if needed)
from app.schemas.rbac import Role, Permission, UserRole

# 3) Your ViewModel adapters
from app.viewmodels.rbac import RoleViewModel, PermissionViewModel, UserRoleViewModel

# 4) Auth dependency
from app.core.auth import verify_token

router = APIRouter(
    prefix="/api/rbac",
    tags=["rbac"],
)

@router.get("/roles", response_model=list[Role])
def list_roles(
    db: Session = Depends(get_db),
    token: dict = Depends(verify_token),
):
    return RoleViewModel(db).get_roles()

@router.get("/permissions", response_model=list[Permission])
def list_permissions(
    db: Session = Depends(get_db),
    token: dict = Depends(verify_token),
):
    return PermissionViewModel(db).get_permissions()

@router.get("/user_roles/{user_id}", response_model=list[UserRole])
def list_user_roles(
    user_id: int,
    db: Session = Depends(get_db),
    token: dict = Depends(verify_token),
):
    return UserRoleViewModel(db).get_user_roles(user_id)
