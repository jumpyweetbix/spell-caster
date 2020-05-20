"""empty message

Revision ID: a4938f3a7392
Revises: ccbb7e5e4019
Create Date: 2020-05-19 23:32:56.578376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4938f3a7392'
down_revision = 'ccbb7e5e4019'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spell',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subclass',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('desc', sa.String(length=5000), nullable=True),
    sa.Column('resource_name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('race', sa.String(length=128), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('class',
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('desc', sa.String(length=5000), nullable=True),
    sa.Column('resource', sa.Integer(), nullable=True),
    sa.Column('saving_throw', sa.String(length=128), nullable=True),
    sa.Column('ability_score', sa.Integer(), nullable=True),
    sa.Column('spell_save', sa.Integer(), nullable=True),
    sa.Column('spell_attack', sa.Integer(), nullable=True),
    sa.Column('prof_bonus', sa.Integer(), nullable=True),
    sa.Column('subclass_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['subclass_id'], ['subclass.id'], ),
    sa.PrimaryKeyConstraint('character_id')
    )
    op.create_table('slots',
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('lvl_1', sa.Integer(), nullable=True),
    sa.Column('lvl_2', sa.Integer(), nullable=True),
    sa.Column('lvl_3', sa.Integer(), nullable=True),
    sa.Column('lvl_4', sa.Integer(), nullable=True),
    sa.Column('lvl_5', sa.Integer(), nullable=True),
    sa.Column('lvl_6', sa.Integer(), nullable=True),
    sa.Column('lvl_7', sa.Integer(), nullable=True),
    sa.Column('lvl_8', sa.Integer(), nullable=True),
    sa.Column('lvl_9', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.PrimaryKeyConstraint('character_id')
    )
    op.create_table('spellbook',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('spell_id', sa.Integer(), nullable=True),
    sa.Column('prepared', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['spell_id'], ['spell.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spellbook')
    op.drop_table('slots')
    op.drop_table('class')
    op.drop_table('character')
    op.drop_table('user')
    op.drop_table('subclass')
    op.drop_table('spell')
    # ### end Alembic commands ###