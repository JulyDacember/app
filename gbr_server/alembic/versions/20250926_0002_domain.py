"""domain schema

Revision ID: 20250926_0002
Revises: 20250926_0001
Create Date: 2025-09-26 01:00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "20250926_0002"
down_revision: Union[str, None] = "20250926_0001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto;")

    # Lookups
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("code", sa.String(50), nullable=False, unique=True),
        sa.Column("name", sa.String(100), nullable=False),
    )

    op.create_table(
        "alert_types",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("code", sa.String(50), nullable=False, unique=True),
        sa.Column("name", sa.String(100), nullable=False),
    )

    op.create_table(
        "alert_state_wait",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("code", sa.String(50), nullable=False, unique=True),
        sa.Column("name", sa.String(100), nullable=False),
    )

    op.create_table(
        "alert_state_current",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("code", sa.String(50), nullable=False, unique=True),
        sa.Column("name", sa.String(100), nullable=False),
    )

    op.create_table(
        "alert_reasons",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("code", sa.String(50), nullable=False, unique=True),
        sa.Column("name", sa.String(100), nullable=False),
    )

    op.create_table(
        "crew_statuses",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("code", sa.String(50), nullable=False, unique=True),
        sa.Column("name", sa.String(100), nullable=False),
    )

    op.create_table(
        "request_statuses",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("code", sa.String(50), nullable=False, unique=True),
        sa.Column("name", sa.String(100), nullable=False),
    )

    # Employees
    op.create_table(
        "employees",
        sa.Column("id", sa.dialects.postgresql.UUID(), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("full_name", sa.String(255), nullable=False),
        sa.Column("phone", sa.String(50)),
        sa.Column("user_id", sa.Integer(), unique=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="SET NULL"),
    )

    # Boards
    op.create_table(
        "boards",
        sa.Column("id", sa.dialects.postgresql.UUID(), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("number_plate", sa.String(50), unique=True),
        sa.Column("model", sa.String(100)),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    )

    # Crews
    op.create_table(
        "crews",
        sa.Column("id", sa.dialects.postgresql.UUID(), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("board_id", sa.dialects.postgresql.UUID()),
        sa.Column("status_id", sa.Integer()),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["board_id"], ["boards.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["status_id"], ["crew_statuses.id"], ondelete="RESTRICT"),
    )

    op.create_table(
        "crew_members",
        sa.Column("crew_id", sa.dialects.postgresql.UUID(), nullable=False),
        sa.Column("employee_id", sa.dialects.postgresql.UUID(), nullable=False),
        sa.Column("role_in_crew", sa.String(100)),
        sa.PrimaryKeyConstraint("crew_id", "employee_id"),
        sa.ForeignKeyConstraint(["crew_id"], ["crews.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["employee_id"], ["employees.id"], ondelete="CASCADE"),
    )

    # Shifts
    op.create_table(
        "shifts",
        sa.Column("id", sa.dialects.postgresql.UUID(), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("crew_id", sa.dialects.postgresql.UUID(), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("ended_at", sa.DateTime(timezone=True)),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        sa.ForeignKeyConstraint(["crew_id"], ["crews.id"], ondelete="CASCADE"),
    )
    op.create_index("uq_shifts_active_crew", "shifts", ["crew_id"], unique=True, postgresql_where=sa.text("is_active = true"))

    # Alerts
    op.create_table(
        "alerts",
        sa.Column("id", sa.dialects.postgresql.UUID(), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("title", sa.String(255)),
        sa.Column("description", sa.Text()),
        sa.Column("address", sa.Text()),
        sa.Column("sender", sa.String(255)),
        sa.Column("type_id", sa.Integer()),
        sa.Column("state_wait_id", sa.Integer()),
        sa.Column("state_current_id", sa.Integer()),
        sa.Column("reason_id", sa.Integer()),
        sa.Column("image_count", sa.Integer(), server_default="0"),
        sa.Column("time_to_arrive", sa.String(50)),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("assigned_crew_id", sa.dialects.postgresql.UUID()),
        sa.ForeignKeyConstraint(["type_id"], ["alert_types.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["state_wait_id"], ["alert_state_wait.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["state_current_id"], ["alert_state_current.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["reason_id"], ["alert_reasons.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["assigned_crew_id"], ["crews.id"], ondelete="SET NULL"),
    )

    op.create_table(
        "alert_points",
        sa.Column("id", sa.dialects.postgresql.UUID(), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("alert_id", sa.dialects.postgresql.UUID(), nullable=False),
        sa.Column("seq_num", sa.Integer(), nullable=False),
        sa.Column("lat", sa.Float(), nullable=False),
        sa.Column("lon", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(["alert_id"], ["alerts.id"], ondelete="CASCADE"),
    )
    op.create_index("ix_alert_points_alert_seq", "alert_points", ["alert_id", "seq_num"], unique=False)

    op.create_table(
        "alert_messages",
        sa.Column("id", sa.dialects.postgresql.UUID(), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("alert_id", sa.dialects.postgresql.UUID(), nullable=False),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("author_employee_id", sa.dialects.postgresql.UUID()),
        sa.ForeignKeyConstraint(["alert_id"], ["alerts.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["author_employee_id"], ["employees.id"], ondelete="SET NULL"),
    )

    op.create_table(
        "alert_solutions",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("code", sa.String(50), unique=True, nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
    )

    op.create_table(
        "alert_assignments",
        sa.Column("id", sa.dialects.postgresql.UUID(), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("alert_id", sa.dialects.postgresql.UUID(), nullable=False),
        sa.Column("crew_id", sa.dialects.postgresql.UUID(), nullable=False),
        sa.Column("assigned_by_user_id", sa.Integer(), nullable=False),
        sa.Column("assigned_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["alert_id"], ["alerts.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["crew_id"], ["crews.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["assigned_by_user_id"], ["users.id"], ondelete="RESTRICT"),
    )
    op.create_index("ix_alert_assignments_alert", "alert_assignments", ["alert_id"], unique=False)
    op.create_index("ix_alert_assignments_crew", "alert_assignments", ["crew_id"], unique=False)

    op.create_table(
        "alert_open_requests",
        sa.Column("id", sa.dialects.postgresql.UUID(), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("alert_id", sa.dialects.postgresql.UUID(), nullable=False),
        sa.Column("requested_by_user_id", sa.Integer(), nullable=False),
        sa.Column("requested_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("status_id", sa.Integer(), nullable=False),
        sa.Column("approved_by_user_id", sa.Integer()),
        sa.Column("approved_at", sa.DateTime(timezone=True)),
        sa.ForeignKeyConstraint(["alert_id"], ["alerts.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["requested_by_user_id"], ["users.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["approved_by_user_id"], ["users.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["status_id"], ["request_statuses.id"], ondelete="RESTRICT"),
    )
    op.create_index("ix_alert_open_requests_alert", "alert_open_requests", ["alert_id"], unique=False)

    # Seed
    op.execute("""
    INSERT INTO roles(code,name) VALUES
      ('admin','Администратор'),('guard','Охранник'),('dispatcher','Диспетчер')
    ON CONFLICT (code) DO NOTHING;

    INSERT INTO crew_statuses(code,name) VALUES
      ('Unknown','Неизвестно'),('Free','Свободен'),('OnAlert','На тревоге')
    ON CONFLICT (code) DO NOTHING;

    INSERT INTO request_statuses(code,name) VALUES
      ('Pending','Ожидает'),('Approved','Подтверждено'),('Rejected','Отклонено')
    ON CONFLICT (code) DO NOTHING;

    INSERT INTO alert_types(code,name) VALUES
      ('Alert','Тревога'),('Moving','Перемещение'),('Task','Задание'),('Post','Пост'),('Detour','Объезд'),('TechnicalDetour','Технический объезд'),('Drill','Учебная тревога')
    ON CONFLICT (code) DO NOTHING;

    INSERT INTO alert_state_wait(code,name) VALUES
      ('WaitAlertShow','Ожидает показа'),('WaitConfirmAlert','Ожидает подтверждения тревоги'),('WaitConfrimArrive','Ожидает подтверждения прибытия'),('WaitConfirmClose','Ожидает подтверждения закрытия'),('WaitConfirmCancel','Ожидает подтверждения отмены')
    ON CONFLICT (code) DO NOTHING;

    INSERT INTO alert_state_current(code,name) VALUES
      ('ConfirmAlertShow','Подтверждение показа'),('ConfirmAlert','Подтверждение тревоги'),('ConfrimArrive','Подтверждение прибытия'),('ConfirmClose','Подтверждение закрытия'),('ConfirmCancel','Подтверждение отмены'),('CallProlongArrive','Продление прибытия')
    ON CONFLICT (code) DO NOTHING;

    INSERT INTO alert_reasons(code,name) VALUES
      ('OS','ОС'),('KTS','КТС'),('PS','ПС'),('POWER','АКБ и 220'),('OTHER','Иное')
    ON CONFLICT (code) DO NOTHING;
    """)


def downgrade() -> None:
    op.drop_index("ix_alert_open_requests_alert", table_name="alert_open_requests")
    op.drop_table("alert_open_requests")
    op.drop_index("ix_alert_assignments_crew", table_name="alert_assignments")
    op.drop_index("ix_alert_assignments_alert", table_name="alert_assignments")
    op.drop_table("alert_assignments")
    op.drop_table("alert_solutions")
    op.drop_table("alert_messages")
    op.drop_index("ix_alert_points_alert_seq", table_name="alert_points")
    op.drop_table("alert_points")
    op.drop_table("alerts")
    op.drop_index("uq_shifts_active_crew", table_name="shifts")
    op.drop_table("shifts")
    op.drop_table("crew_members")
    op.drop_table("crews")
    op.drop_table("boards")
    op.drop_table("employees")
    op.drop_table("request_statuses")
    op.drop_table("crew_statuses")
    op.drop_table("alert_reasons")
    op.drop_table("alert_state_current")
    op.drop_table("alert_state_wait")
    op.drop_table("alert_types")
    op.drop_table("roles")

