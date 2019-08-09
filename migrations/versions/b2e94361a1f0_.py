"""empty message

Revision ID: b2e94361a1f0
Revises: 142ee4a5d31c
Create Date: 2019-06-29 20:00:56.688679

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b2e94361a1f0'
down_revision = '142ee4a5d31c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('display', sa.Boolean(), nullable=True))
    op.drop_column('comment', 'state')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('state', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('comment', 'display')
    # ### end Alembic commands ###