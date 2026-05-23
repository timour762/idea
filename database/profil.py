from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func, false
from datetime import datetime
from .models import Base
from .user import User
class Profile(Base):
    __tablename__ = "profiles"
    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    user_id: Mapped[int]= mapped_column(
        ForeignKey("users.telegram_id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
        )
    first_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
        )
    last_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
        )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow,
        )
    username: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )
    number_of_users: Mapped[int] = mapped_column(
        nullable=False,
        server_default="0"
    )
    user: Mapped["User"] = relationship(
        "User",
        back_populates="profile",
    )
