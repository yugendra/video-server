"""empty message

Revision ID: 400f2da5848c
Revises: 
Create Date: 2018-05-31 23:53:34.660584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '400f2da5848c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###