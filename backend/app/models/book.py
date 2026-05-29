from sqlalchemy import String, Boolean, Integer, Date, Enum, Text
from sqlalchemy.orm import Mapped, mapped_column
import enum
from .base import Base, TimestampBase

class AgeRange(enum.Enum):
    BOARD_BOOK = "board_book"
    CHAPTER_BOOK = "chapter_book"
    MIDDLE_GRADE = "middle_grade"
    YOUNG_ADULT = "young_adult"
    NEW_ADULT = "new_adult"
    ADULT = "adult"

    @property
    def min_age(self):
        ages = {
            "board_book" : 0,
            "chapter_book" : 6,
            "middle_grade" : 8,
            "young_adult" : 12,
            "new_adult" : 18,
            "adult" : 18
        }

        return ages[self.value]
    

class Genre(enum.Enum):
    ROMANCE = "romance"
    SCI_FI = "sci_fi"
    MYSTERY = "mystery"
    THRILLER = "thriller"
    CHILDREN = "children"
    FICTION = "fiction"
    NON_FICTION = "non_fiction"
    BIOGRAPHY = "biography"
    RELIGIOUS = "religious"
    HISTORY = "history"
    CRIME = "crime"
    SCIENCE = "science"
    FINANCE = "finance"


class Book(Base, TimestampBase):
    __tablename__ = "books"
    book_id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    isbn : Mapped[str] = mapped_column(String, unique=True)
    title : Mapped[str] = mapped_column(String)
    description : Mapped[str | None] = mapped_column(Text)
    author : Mapped[str] = mapped_column(String)
    publisher : Mapped[str] = mapped_column(String)
    edition : Mapped[str | None] = mapped_column(String)
    lexile_level : Mapped[int | None] = mapped_column(Integer)
    age_group : Mapped[AgeRange] = mapped_column(Enum(AgeRange), default=AgeRange.ADULT)
    genre : Mapped[Genre] = mapped_column(Enum(Genre), default=Genre.NON_FICTION)
    tags : Mapped[str | None] = mapped_column(String)
    cover_url : Mapped[str | None] = mapped_column(String)
    is_active : Mapped[bool] = mapped_column(Boolean, default=True)
    updated_by : Mapped[int | None] = mapped_column(Integer)
    