"""empty message

Revision ID: c548ea0014ee
Revises: ff3594f07908
Create Date: 2020-05-21 22:25:17.200064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c548ea0014ee'
down_revision = 'ff3594f07908'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spell', sa.Column('concentration', sa.Boolean(), nullable=True))
    op.add_column('spell', sa.Column('ritual', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('spell', 'ritual')
    op.drop_column('spell', 'concentration')
    # ### end Alembic commands ###
