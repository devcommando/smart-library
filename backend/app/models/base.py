from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import DateTime

class Base(DeclarativeBase):
    pass

#Base class so child class can inherit the created_at & updated_at columns in each model/table
class TimestampBase:
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True))
    updated_at : Mapped[datetime] = mapped_column(DateTime(timezone=True))

