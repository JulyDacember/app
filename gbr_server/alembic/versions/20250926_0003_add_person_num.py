"""add person_num to employees

Revision ID: 20250926_0003
Revises: 20250926_0002
Create Date: 2025-09-26 02:00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "20250926_0003"
down_revision: Union[str, None] = "20250926_0002"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add person_num column to employees table
    op.add_column('employees', sa.Column('person_num', sa.String(50), nullable=True))


def downgrade() -> None:
    # Remove person_num column from employees table
    op.drop_column('employees', 'person_num')
