from app.core.database import SessionLocal
from app.models.rbac import Role, Permission, RolePermission, UserRole
from sqlalchemy.orm import Session
from typing import List

class RoleViewModel:
    def __init__(self, db: Session):
        self.db = db
    def get_roles(self) -> List[Role]:
        return self.db.query(Role).all()
    # Add more business logic as needed

class PermissionViewModel:
    def __init__(self, db: Session):
        self.db = db
    def get_permissions(self) -> List[Permission]:
        return self.db.query(Permission).all()
    # Add more business logic as needed

class UserRoleViewModel:
    def __init__(self, db: Session):
        self.db = db
    def get_user_roles(self, user_id: int) -> List[UserRole]:
        return self.db.query(UserRole).filter(UserRole.user_id == user_id).all()
    # Add more business logic as needed
