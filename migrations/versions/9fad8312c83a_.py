"""empty message

Revision ID: 9fad8312c83a
Revises: 569be3bd9c4c
Create Date: 2020-05-21 14:09:03.349794

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9fad8312c83a'
down_revision = '569be3bd9c4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('character_ibfk_2', 'character', type_='foreignkey')
    op.drop_column('character', 'subclass_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('character', sa.Column('subclass_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('character_ibfk_2', 'character', 'subclass', ['subclass_id'], ['id'])
    # ### end Alembic commands ###
