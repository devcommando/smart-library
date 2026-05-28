from sqlalchemy import String, Boolean, Integer, Date, Enum
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from .base import Base, TimestampBase
import enum

class UserRole(enum.Enum):
    GUEST = "guest"
    MEMBER = "member"
    LIBRARIAN = "librarian"
    ADMIN = "admin"


class User(Base, TimestampBase):
    __tablename__ = "users"
    userid : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    address1: Mapped[str | None] = mapped_column(String)
    address2: Mapped[str | None] = mapped_column(String)
    city: Mapped[str | None] = mapped_column(String)
    state: Mapped[str | None] = mapped_column(String)
    zip: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    date_of_birth: Mapped[date] = mapped_column(Date)
    hashed_password: Mapped[str] = mapped_column(String)
    user_type: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.MEMBER)
    account_status: Mapped[bool] = mapped_column(Boolean, default=True)
    consent_email: Mapped[bool] = mapped_column(Boolean, default=False)
    consent_phone: Mapped[bool] = mapped_column(Boolean, default=False)
    updated_by: Mapped[int | None] = mapped_column(Integer)
    


