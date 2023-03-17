"""add last few columns to posts table

Revision ID: f802ea2ee810
Revises: 9c7ff059d147
Create Date: 2023-03-17 10:02:12.360700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f802ea2ee810'
down_revision = '9c7ff059d147'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default="TRUE"),)
    op.add_column('posts',sa.Column("created_at",sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts',"published")
    op.drop_column('posts',"created_at")
    pass
