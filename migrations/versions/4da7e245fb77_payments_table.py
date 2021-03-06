"""Payments table

Revision ID: 4da7e245fb77
Revises: 
Create Date: 2020-06-20 12:07:43.720132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4da7e245fb77'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_payments():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bank_account_name', sa.String(length=256), nullable=False),
    sa.Column('bank_name', sa.String(length=128), nullable=False),
    sa.Column('exact_money', sa.Integer(), nullable=False),
    sa.Column('transfer_datetime', sa.String(length=128), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_payments_bank_account_name'), 'payments', ['bank_account_name'], unique=False)
    op.create_index(op.f('ix_payments_bank_name'), 'payments', ['bank_name'], unique=False)
    op.create_index(op.f('ix_payments_transfer_datetime'), 'payments', ['transfer_datetime'], unique=False)
    # ### end Alembic commands ###


def downgrade_payments():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_payments_transfer_datetime'), table_name='payments')
    op.drop_index(op.f('ix_payments_bank_name'), table_name='payments')
    op.drop_index(op.f('ix_payments_bank_account_name'), table_name='payments')
    op.drop_table('payments')
    # ### end Alembic commands ###

