"""add content column to post table

Revision ID: 19292494e8f5
Revises: f49857fb41f7
Create Date: 2023-09-11 14:36:34.302091

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19292494e8f5'
down_revision: Union[str, None] = 'f49857fb41f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
