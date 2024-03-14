"""added token

Revision ID: ff59250fa0e6
Revises: 20b24b3b32c6
Create Date: 2024-03-15 01:17:57.993952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff59250fa0e6'
down_revision: Union[str, None] = '20b24b3b32c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
