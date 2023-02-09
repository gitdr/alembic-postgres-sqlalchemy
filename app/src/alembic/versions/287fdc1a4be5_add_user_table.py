"""Add user table

Revision ID: 287fdc1a4be5
Revises: 
Create Date: 2023-02-09 15:21:20.570884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '287fdc1a4be5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_account')
    # ### end Alembic commands ###
