"""Third

Revision ID: 5837773c1abc
Revises: 169fdf3c6a35
Create Date: 2023-04-02 22:01:37.738622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5837773c1abc'
down_revision = '169fdf3c6a35'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.add_column('zero_table', sa.Column('user', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'zero_table', 'user', ['user'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'zero_table', type_='foreignkey')
    op.drop_column('zero_table', 'user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###