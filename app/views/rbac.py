from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.rbac import Role, Permission, UserRole
from app.viewmodels.rbac import RoleViewModel, PermissionViewModel, UserRoleViewModel
from app.core.auth import verify_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/roles", response_model=list[Role])
def list_roles(db: Session = Depends(get_db), token: dict = Depends(verify_token)):
    return RoleViewModel(db).get_roles()

@router.get("/permissions", response_model=list[Permission])
def list_permissions(db: Session = Depends(get_db), token: dict = Depends(verify_token)):
    return PermissionViewModel(db).get_permissions()

@router.get("/user_roles/{user_id}", response_model=list[UserRole])
def list_user_roles(user_id: int, db: Session = Depends(get_db), token: dict = Depends(verify_token)):
    return UserRoleViewModel(db).get_user_roles(user_id)
