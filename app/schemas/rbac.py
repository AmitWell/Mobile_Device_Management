from pydantic import BaseModel
from typing import Optional, List

class RoleBase(BaseModel):
    name: str
    department: Optional[str]
    parent_id: Optional[int]

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int
    class Config:
        orm_mode = True

class PermissionBase(BaseModel):
    resource: str
    action: str

class PermissionCreate(PermissionBase):
    pass

class Permission(PermissionBase):
    id: int
    class Config:
        orm_mode = True

class RolePermission(BaseModel):
    role_id: int
    permission_id: int
    delegated_by: Optional[int]

class UserRole(BaseModel):
    user_id: int
    role_id: int
    assigned_by: Optional[int]
