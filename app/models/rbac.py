# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship, declarative_base

# Base = declarative_base()

# class Role(Base):
#     __tablename__ = "roles"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
#     parent_id = Column(Integer, ForeignKey("roles.id"))
#     department = Column(String(50))
#     parent = relationship("Role", remote_side=[id])

# class Permission(Base):
#     __tablename__ = "permissions"
#     id = Column(Integer, primary_key=True)
#     resource = Column(String(50), nullable=False)
#     action = Column(String(50), nullable=False)

# class RolePermission(Base):
#     __tablename__ = "role_permissions"
#     role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)
#     permission_id = Column(Integer, ForeignKey("permissions.id"), primary_key=True)
#     delegated_by = Column(Integer)

# class UserRole(Base):
#     __tablename__ = "user_roles"
#     user_id = Column(Integer, primary_key=True)
#     role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)
#     assigned_by = Column(Integer)

# from sqlalchemy import (
#     Column,
#     Integer,
#     String,
#     ForeignKey,
#     CheckConstraint,
#     UniqueConstraint,
#     PrimaryKeyConstraint,
#     ForeignKeyConstraint,
#     Index
# )
# from sqlalchemy.orm import relationship
# from app.core.database import Base  # make sure your database.py exports Base = declarative_base()
# from sqlalchemy import (
#     Column, Integer, String, ForeignKey,
#     CheckConstraint, UniqueConstraint,
#     PrimaryKeyConstraint, ForeignKeyConstraint, Index
# )
# from sqlalchemy.orm import relationship
# from app.core.database import Base   # ← safe, no imports back to models

# # ───────────────────────────────────────────────────────────────────────────────
# class User(Base):
#     __tablename__ = "users"

#     id              = Column(Integer, primary_key=True, index=True)
#     username        = Column(String(50), unique=True, nullable=False, index=True)
#     hashed_password = Column(String, nullable=False)
#     department      = Column(String(50), nullable=False)

#     # one-to-many → UserRole
#     roles = relationship("UserRole", back_populates="user", cascade="all, delete-orphan")


# # ───────────────────────────────────────────────────────────────────────────────
# class Role(Base):
#     __tablename__ = "roles"

#     id         = Column(Integer, primary_key=True)
#     name       = Column(String(50), unique=True, nullable=False)
#     parent_id  = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=True)
#     department = Column(String(50), nullable=True)

#     __table_args__ = (
#         # CEO must have no department; non-CEO must have one
#         CheckConstraint(
#             "(name = 'ceo' AND department IS NULL) OR (name <> 'ceo' AND department IS NOT NULL)",
#             name="ck_roles_department_ceo"
#         ),
#         # CEO must have no parent
#         CheckConstraint(
#             "(name = 'ceo' AND parent_id IS NULL) OR (name <> 'ceo')",
#             name="ck_roles_parent_ceo"
#         ),
#         Index("ix_roles_name", "name"),
#     )

#     # self-referencing hierarchy
#     parent   = relationship("Role", remote_side=[id], backref="children")
#     # many-to-many → RolePermission
#     permissions = relationship("RolePermission", back_populates="role", cascade="all, delete-orphan")
#     # many-to-many → UserRole
#     users       = relationship("UserRole", back_populates="role", cascade="all, delete-orphan")


# # ───────────────────────────────────────────────────────────────────────────────
# class Permission(Base):
#     __tablename__ = "permissions"

#     id       = Column(Integer, primary_key=True)
#     resource = Column(String(50), nullable=False)
#     action   = Column(String(50), nullable=False)

#     __table_args__ = (
#         CheckConstraint(
#             "action IN ('read','write','delete','manage')",
#             name="ck_permissions_action"
#         ),
#         UniqueConstraint("resource", "action", name="uq_permissions_resource_action"),
#         Index("ix_permissions_resource", "resource"),
#     )

#     # many-to-many → RolePermission
#     roles = relationship("RolePermission", back_populates="permission", cascade="all, delete-orphan")


# # ───────────────────────────────────────────────────────────────────────────────
# class RolePermission(Base):
#     __tablename__ = "role_permissions"

#     role_id       = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
#     permission_id = Column(Integer, ForeignKey("permissions.id", ondelete="CASCADE"), nullable=False)
#     delegated_by  = Column(Integer, nullable=True)

#     __table_args__ = (
#         PrimaryKeyConstraint("role_id", "permission_id", name="pk_role_permissions"),
#         CheckConstraint("role_id <> delegated_by", name="ck_rp_no_self_delegate"),
#         ForeignKeyConstraint(
#             ["delegated_by", "permission_id"],
#             ["role_permissions.role_id", "role_permissions.permission_id"],
#             name="fk_rp_delegation_chain"
#         ),
#     )

#     role       = relationship("Role", back_populates="permissions")
#     permission = relationship("Permission", back_populates="roles")


# # ───────────────────────────────────────────────────────────────────────────────
# class UserRole(Base):
#     __tablename__ = "user_roles"

#     user_id     = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
#     role_id     = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
#     assigned_by = Column(Integer, nullable=False)

#     __table_args__ = (
#         PrimaryKeyConstraint("user_id", "role_id", name="pk_user_roles"),
#         # Assigner must be parent of the assigned role
#         ForeignKeyConstraint(
#             ["assigned_by", "role_id"],
#             ["roles.id", "roles.parent_id"],
#             name="fk_user_roles_assigner"
#         ),
#         # Only CEO (role_id=1) can assign themselves
#         CheckConstraint(
#             "(role_id = 1 AND assigned_by = user_id) OR (role_id <> 1)",
#             name="ck_ur_ceo_assign_self"
#         ),
#     )

#     user = relationship("User", back_populates="roles")
#     role = relationship("Role", back_populates="users")

# from sqlalchemy import (
#     Column, Integer, String, ForeignKey,
#     CheckConstraint, UniqueConstraint,
#     PrimaryKeyConstraint, ForeignKeyConstraint, Index
# )
# from sqlalchemy.orm import relationship
# from app.core.database import Base

# class User(Base):
#     __tablename__ = "users"
#     id              = Column(Integer, primary_key=True, index=True)
#     username        = Column(String(50), unique=True, nullable=False, index=True)
#     hashed_password = Column(String, nullable=False)
#     department      = Column(String(50), nullable=False)
#     roles           = relationship("UserRole", back_populates="user", cascade="all, delete-orphan")

# class Role(Base):
#     __tablename__ = "roles"
#     id         = Column(Integer, primary_key=True)
#     name       = Column(String(50), unique=True, nullable=False)
#     parent_id  = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=True)
#     department = Column(String(50), nullable=True)

#     __table_args__ = (
#         CheckConstraint(
#             "(name = 'ceo' AND department IS NULL) OR (name <> 'ceo' AND department IS NOT NULL)",
#             name="ck_roles_department_ceo"
#         ),
#         CheckConstraint(
#             "(name = 'ceo' AND parent_id IS NULL) OR (name <> 'ceo')",
#             name="ck_roles_parent_ceo"
#         ),
#         Index("ix_roles_name", "name"),
#     )

#     parent      = relationship("Role", remote_side=[id], backref="children")
#     permissions = relationship("RolePermission", back_populates="role", cascade="all, delete-orphan")
#     users       = relationship("UserRole", back_populates="role", cascade="all, delete-orphan")

# class Permission(Base):
#     __tablename__ = "permissions"
#     id       = Column(Integer, primary_key=True)
#     resource = Column(String(50), nullable=False)
#     action   = Column(String(50), nullable=False)

#     __table_args__ = (
#         CheckConstraint("action IN ('read','write','delete','manage')", name="ck_permissions_action"),
#         UniqueConstraint("resource", "action", name="uq_permissions_resource_action"),
#         Index("ix_permissions_resource", "resource"),
#     )

#     roles = relationship("RolePermission", back_populates="permission", cascade="all, delete-orphan")

# class RolePermission(Base):
#     __tablename__ = "role_permissions"
#     role_id       = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
#     permission_id = Column(Integer, ForeignKey("permissions.id", ondelete="CASCADE"), nullable=False)
#     delegated_by  = Column(Integer, nullable=True)

#     __table_args__ = (
#         PrimaryKeyConstraint("role_id", "permission_id", name="pk_role_permissions"),
#         CheckConstraint("role_id <> delegated_by", name="ck_rp_no_self_delegate"),
#         ForeignKeyConstraint(
#             ["delegated_by", "permission_id"],
#             ["role_permissions.role_id", "role_permissions.permission_id"],
#             name="fk_rp_delegation_chain"
#         ),
#     )

#     role       = relationship("Role", back_populates="permissions")
#     permission = relationship("Permission", back_populates="roles")

# class UserRole(Base):
#     __tablename__ = "user_roles"
#     user_id     = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
#     role_id     = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
#     assigned_by = Column(Integer, nullable=False)

#     __table_args__ = (
#         PrimaryKeyConstraint("user_id", "role_id", name="pk_user_roles"),
#         ForeignKeyConstraint(
#             ["assigned_by", "role_id"],
#             ["roles.id", "roles.parent_id"],
#             name="fk_user_roles_assigner"
#         ),
#         CheckConstraint(
#             "(role_id = 1 AND assigned_by = user_id) OR (role_id <> 1)",
#             name="ck_ur_ceo_assign_self"
#         ),
#     )

#     user = relationship("User", back_populates="roles")
#     role = relationship("Role", back_populates="users")

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    CheckConstraint,
    UniqueConstraint,
    PrimaryKeyConstraint,
    ForeignKeyConstraint,
    Index
)
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    id              = Column(Integer, primary_key=True, index=True)
    username        = Column(String(50), unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    department      = Column(String(50), nullable=False)

    roles = relationship("UserRole", back_populates="user", cascade="all, delete-orphan")


class Role(Base):
    __tablename__ = "roles"
    id         = Column(Integer, primary_key=True)
    name       = Column(String(50), unique=True, nullable=False)
    parent_id  = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=True)
    department = Column(String(50), nullable=True)

    __table_args__ = (
        CheckConstraint(
            "(name = 'ceo' AND department IS NULL) OR (name <> 'ceo' AND department IS NOT NULL)",
            name="ck_roles_department_ceo"
        ),
        CheckConstraint(
            "(name = 'ceo' AND parent_id IS NULL) OR (name <> 'ceo')",
            name="ck_roles_parent_ceo"
        ),
        Index("ix_roles_name", "name"),
    )

    parent      = relationship("Role", remote_side=[id], backref="children")
    permissions = relationship("RolePermission", back_populates="role", cascade="all, delete-orphan")
    users       = relationship("UserRole", back_populates="role", cascade="all, delete-orphan")


class Permission(Base):
    __tablename__ = "permissions"
    id       = Column(Integer, primary_key=True)
    resource = Column(String(50), nullable=False)
    action   = Column(String(50), nullable=False)

    __table_args__ = (
        CheckConstraint("action IN ('read','write','delete','manage')", name="ck_permissions_action"),
        UniqueConstraint("resource", "action", name="uq_permissions_resource_action"),
        Index("ix_permissions_resource", "resource"),
    )

    roles = relationship("RolePermission", back_populates="permission", cascade="all, delete-orphan")


class RolePermission(Base):
    __tablename__ = "role_permissions"
    role_id       = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
    permission_id = Column(Integer, ForeignKey("permissions.id", ondelete="CASCADE"), nullable=False)
    delegated_by  = Column(Integer, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint("role_id", "permission_id", name="pk_role_permissions"),
        CheckConstraint("role_id <> delegated_by", name="ck_rp_no_self_delegate"),
        ForeignKeyConstraint(
            ["delegated_by", "permission_id"],
            ["role_permissions.role_id", "role_permissions.permission_id"],
            name="fk_rp_delegation_chain"
        ),
    )

    role       = relationship("Role", back_populates="permissions")
    permission = relationship("Permission", back_populates="roles")


class UserRole(Base):
    __tablename__ = "user_roles"
    user_id     = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    role_id     = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)
    assigned_by = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)

    __table_args__ = (
        # Only CEO (role_id=1) can assign themselves; other validations handled in code
        CheckConstraint(
            "(role_id = 1 AND assigned_by = user_id) OR (role_id <> 1)",
            name="ck_ur_ceo_assign_self"
        ),
    )

    user = relationship("User", back_populates="roles")
    role = relationship("Role", back_populates="users")