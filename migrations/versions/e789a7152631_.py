"""empty message

Revision ID: e789a7152631
Revises: 
Create Date: 2024-01-16 13:40:33.934893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e789a7152631'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('code_snippets',
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('language', sa.String(length=50), nullable=False),
    sa.Column('code', sa.Text(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_code_snippets'))
    )
    with op.batch_alter_table('code_snippets', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_code_snippets_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('code_snippets', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_code_snippets_id'))

    op.drop_table('code_snippets')
    # ### end Alembic commands ###
