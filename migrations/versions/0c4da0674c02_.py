"""empty message

Revision ID: 0c4da0674c02
Revises: 4c2ff31abec3
Create Date: 2019-06-29 17:58:10.044146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c4da0674c02'
down_revision = '4c2ff31abec3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('comment_clean', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'comment_clean')
    # ### end Alembic commands ###