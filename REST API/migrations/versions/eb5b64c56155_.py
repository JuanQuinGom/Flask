"""empty message

Revision ID: eb5b64c56155
Revises: 683ab06f169a
Create Date: 2021-03-03 09:58:33.013537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb5b64c56155'
down_revision = '683ab06f169a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.String(length=255), nullable=False),
    sa.Column('product_description', sa.String(length=255), nullable=False),
    sa.Column('product_price', sa.Integer(), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('product_name'),
    sa.UniqueConstraint('public_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
