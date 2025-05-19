from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    parent_id = Column(Integer, ForeignKey("roles.id"))
    department = Column(String(50))
    parent = relationship("Role", remote_side=[id])

class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True)
    resource = Column(String(50), nullable=False)
    action = Column(String(50), nullable=False)

class RolePermission(Base):
    __tablename__ = "role_permissions"
    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)
    permission_id = Column(Integer, ForeignKey("permissions.id"), primary_key=True)
    delegated_by = Column(Integer)

class UserRole(Base):
    __tablename__ = "user_roles"
    user_id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)
    assigned_by = Column(Integer)
