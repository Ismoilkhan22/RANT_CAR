from datetime import date
from typing import Optional

from core.models.auth import User
from ninja import ModelSchema, Schema


class UserSchema(Schema):
    id: int
    fio: str
    phone: str
    seria_ps: str
    username: Optional[str]
    g_year: Optional[date]
    g_seria: Optional[str]
    g_ctg: Optional[str]
    is_superuser: bool
    is_staff: bool
    is_active: bool
    user_type: int


class UserCreateSchema(Schema):
    fio: str
    phone: str
    seria_ps: str
    username: Optional[str] = None
    g_year: Optional[date] = None
    g_seria: Optional[str] = None
    g_ctg: Optional[str] = None
    password: str
    user_type: int


class UserUpdateSchema(Schema):
    fio: Optional[str] = None
    phone: Optional[str] = None
    seria_ps: Optional[str] = None
    username: Optional[str] = None
    g_year: Optional[date] = None
    g_seria: Optional[str] = None
    g_ctg: Optional[str] = None
    is_superuser: Optional[bool] = None
    is_staff: Optional[bool] = None
    is_active: Optional[bool] = None
    user_type: Optional[int] = None