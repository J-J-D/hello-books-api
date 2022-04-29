"""adds Book model

Revision ID: 025aeb5321c1
Revises: 
Create Date: 2022-04-29 08:42:31.324814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '025aeb5321c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###
