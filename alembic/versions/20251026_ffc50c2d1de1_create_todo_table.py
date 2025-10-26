# pylint: skip-file
"""
Message: create-todo-table
Revision ID: ffc50c2d1de1
Revises:
Create Date: 2025-10-26 18:31:51.908987.
"""
from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from sqlalchemy import text

from alembic import op

# pylint: disable=invalid-name,no-member,unused-import,unnecessary-pass


# revision identifiers, used by Alembic.
revision: str = 'ffc50c2d1de1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade the database."""
    op.create_table('todomodel',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
                    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
                    sa.Column('done', sa.Boolean(), nullable=False, server_default='f'),
                    sa.Column('create_at', sa.DateTime(), nullable=False, server_default=text('now()')),
                    sa.Column('update_at', sa.DateTime(), nullable=False, server_default=text('now()'), server_onupdate=text(
                        'now()')),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    """Downgrade the database."""
    op.drop_table('todomodel')
