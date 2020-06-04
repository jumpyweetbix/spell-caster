"""empty message

Revision ID: d38b1075d1fa
Revises: d9204973eb73
Create Date: 2020-06-04 22:52:48.821834

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd38b1075d1fa'
down_revision = 'd9204973eb73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('slots', sa.Column('lvl_1', sa.Integer(), nullable=True))
    op.add_column('slots', sa.Column('lvl_2', sa.Integer(), nullable=True))
    op.add_column('slots', sa.Column('lvl_3', sa.Integer(), nullable=True))
    op.add_column('slots', sa.Column('lvl_4', sa.Integer(), nullable=True))
    op.add_column('slots', sa.Column('lvl_5', sa.Integer(), nullable=True))
    op.add_column('slots', sa.Column('lvl_6', sa.Integer(), nullable=True))
    op.add_column('slots', sa.Column('lvl_7', sa.Integer(), nullable=True))
    op.add_column('slots', sa.Column('lvl_8', sa.Integer(), nullable=True))
    op.add_column('slots', sa.Column('lvl_9', sa.Integer(), nullable=True))
    op.drop_column('slots', 'res')
    op.drop_column('slots', 'lvl')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('slots', sa.Column('lvl', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('slots', sa.Column('res', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('slots', 'lvl_9')
    op.drop_column('slots', 'lvl_8')
    op.drop_column('slots', 'lvl_7')
    op.drop_column('slots', 'lvl_6')
    op.drop_column('slots', 'lvl_5')
    op.drop_column('slots', 'lvl_4')
    op.drop_column('slots', 'lvl_3')
    op.drop_column('slots', 'lvl_2')
    op.drop_column('slots', 'lvl_1')
    # ### end Alembic commands ###