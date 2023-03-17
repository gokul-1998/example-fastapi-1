"""Add user table

Revision ID: 92bcfc8dd7c0
Revises: 68a2c9ae2e0f
Create Date: 2023-03-17 09:45:03.384364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92bcfc8dd7c0'
down_revision = '68a2c9ae2e0f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('email',sa.String(),nullable=False),
    sa.Column('password',sa.String(),nullable=False),
    sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'))
    
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
