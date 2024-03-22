"""empty message

Revision ID: c98275fb22f1
Revises: 
Create Date: 2024-03-15 12:07:09.657105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c98275fb22f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients_table',
    sa.Column('client_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('cpf', sa.String(length=12), nullable=True),
    sa.Column('cellphone', sa.String(length=50), nullable=True),
    sa.Column('registration_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('client_id')
    )
    op.create_table('users_table',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('password', sa.String(length=250), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('cellphone', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('packages_table',
    sa.Column('package_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('origin', sa.String(length=150), nullable=False),
    sa.Column('destination', sa.String(length=150), nullable=False),
    sa.Column('departure_date', sa.Date(), nullable=False),
    sa.Column('return_date', sa.Date(), nullable=True),
    sa.Column('registration_date', sa.Date(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('meals', sa.String(length=10), nullable=True),
    sa.Column('accommodation', sa.Boolean(), nullable=True),
    sa.Column('kids', sa.SmallInteger(), nullable=True),
    sa.Column('adults', sa.SmallInteger(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients_table.client_id'], ),
    sa.PrimaryKeyConstraint('package_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('packages_table')
    op.drop_table('users_table')
    op.drop_table('clients_table')
    # ### end Alembic commands ###