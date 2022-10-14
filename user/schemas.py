from typing import Optional, Literal

from pydantic import BaseModel, EmailStr, Field, validator

from user import enums
from user import validators


class BasicModel(BaseModel):
    class Config:
        orm_mode = True


class Role(BasicModel):
    id: int
    role: enums.Role
    user_id: int


class UserEmail(BasicModel):
    email: EmailStr


class User(UserEmail):
    name: str = Field(..., min_length=3, max_length=50)
    gender: Literal["M", "F"]
    is_active: bool = True


class CreateRoles(User):
    roles: Optional[list[Literal[tuple(enums.roles)]]] = Field(unique_items=True)


class UserWithRoles(User):
    roles: list[Role]


class CreateUser(User):
    password: str = Field(..., min_length=5, max_length=255)

    _hash_pass = validator("password", allow_reuse=True)(validators.hash_password)


class DbUser(User):
    id: int
    password: str
