# app/schemas/user.py
from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str
    first_name: str
    last_name: str


class UserRead(UserBase):
    id: int
    first_name: str
    last_name: str
    created_at: datetime

    class Config:
        from_attributes = True

class UserStatistics(BaseModel):
    total_tests: int
    total_questions: int
    total_files: int
    avg_questions_per_test: float
    last_test_created_at: datetime | None

    total_closed_questions: int
    total_open_questions: int
    total_easy_questions: int
    total_medium_questions: int
    total_hard_questions: int

class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str

__all__ = [
    "UserBase",
    "UserCreate",
    "UserRead",
    "UserStatistics",
    "ChangePasswordRequest",
]
