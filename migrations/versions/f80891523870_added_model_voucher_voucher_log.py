"""added model voucher, voucher log

Revision ID: f80891523870
Revises: 6d42e83abcd2
Create Date: 2020-11-12 01:44:02.185406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f80891523870'
down_revision = '6d42e83abcd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('voucher',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('code', sa.String(length=30), nullable=True),
    sa.Column('discount_type', sa.Enum('PERCENT', 'AMOUNT', 'FREESHIPPING'), nullable=True),
    sa.Column('value_type', sa.Enum('RUPIAH', 'POINT'), nullable=True),
    sa.Column('discount_value', sa.DECIMAL(), nullable=False),
    sa.Column('valid_from', sa.Date(), nullable=True),
    sa.Column('valid_to', sa.Date(), nullable=True),
    sa.Column('limit', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('voucher_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('voucher_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voucher_log')
    op.drop_table('voucher')
    # ### end Alembic commands ###