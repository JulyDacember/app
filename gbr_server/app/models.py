from sqlalchemy import String, ForeignKey, DateTime, Boolean, Text, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from .db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    full_name: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str | None] = mapped_column(String(50))
    person_num: Mapped[str | None] = mapped_column(String(50))
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class Board(Base):
    __tablename__ = "boards"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    number_plate: Mapped[str | None] = mapped_column(String(50))
    model: Mapped[str | None] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class Crew(Base):
    __tablename__ = "crews"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    board_id: Mapped[str | None] = mapped_column(UUID(as_uuid=False), ForeignKey("boards.id"))
    status_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("crew_statuses.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class Alert(Base):
    __tablename__ = "alerts"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    title: Mapped[str | None] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(Text)
    address: Mapped[str | None] = mapped_column(Text)
    sender: Mapped[str | None] = mapped_column(String(255))
    type_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("alert_types.id"))
    state_wait_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("alert_state_wait.id"))
    state_current_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("alert_state_current.id"))
    reason_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("alert_reasons.id"))
    image_count: Mapped[int | None]
    time_to_arrive: Mapped[str | None] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    assigned_crew_id: Mapped[str | None] = mapped_column(UUID(as_uuid=False), ForeignKey("crews.id"))


class AlertAssignment(Base):
    __tablename__ = "alert_assignments"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    alert_id: Mapped[str] = mapped_column(UUID(as_uuid=False), ForeignKey("alerts.id"))
    crew_id: Mapped[str] = mapped_column(UUID(as_uuid=False), ForeignKey("crews.id"))
    assigned_by_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    assigned_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class Shift(Base):
    __tablename__ = "shifts"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    crew_id: Mapped[str] = mapped_column(UUID(as_uuid=False), ForeignKey("crews.id"))
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    ended_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)


class AlertOpenRequest(Base):
    __tablename__ = "alert_open_requests"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    alert_id: Mapped[str] = mapped_column(UUID(as_uuid=False), ForeignKey("alerts.id"))
    requested_by_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    requested_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    status_id: Mapped[int] = mapped_column(Integer, ForeignKey("request_statuses.id"))
    approved_by_user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
    approved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

