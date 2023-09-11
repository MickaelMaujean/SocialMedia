"""add again owner_id

Revision ID: 2d2d2ec10970
Revises: c39253ca093a
Create Date: 2023-09-11 16:13:55.656456

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d2d2ec10970'
down_revision: Union[str, None] = 'c39253ca093a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fkey', 
                          source_table='posts', 
                          referent_table='users', 
                          local_cols=['owner_id'], 
                          remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fkey', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
