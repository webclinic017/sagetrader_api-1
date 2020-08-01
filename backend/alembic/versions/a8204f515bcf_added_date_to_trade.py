"""Added date to trade

Revision ID: a8204f515bcf
Revises: 4d883b1ac286
Create Date: 2020-05-30 22:08:51.964945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8204f515bcf'
down_revision = '4d883b1ac286'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trade', sa.Column('date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('trade', 'date')
    # ### end Alembic commands ###
