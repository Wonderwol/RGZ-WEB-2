"""Удаление номера зала из cinema_sessions

Revision ID: 3d2915f63c77
Revises: 6810043f403e
Create Date: 2023-12-25 00:41:47.093486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d2915f63c77'
down_revision = '6810043f403e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cinema_sessions', schema=None) as batch_op:
        batch_op.drop_column('room_number')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cinema_sessions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('room_number', sa.INTEGER(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
