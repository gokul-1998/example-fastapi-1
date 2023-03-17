"""add content column to post table

Revision ID: 68a2c9ae2e0f
Revises: 605ad6d55c92
Create Date: 2023-03-17 09:35:00.066332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68a2c9ae2e0f'
down_revision = '605ad6d55c92'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
