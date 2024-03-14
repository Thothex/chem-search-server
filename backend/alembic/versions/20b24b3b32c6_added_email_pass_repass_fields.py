"""added email/pass/repass fields

Revision ID: 20b24b3b32c6
Revises: 56f045844bbb
Create Date: 2024-03-15 00:49:38.999064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20b24b3b32c6'
down_revision: Union[str, None] = '56f045844bbb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
