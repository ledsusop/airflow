# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""dagrun_config

Revision ID: 40e67319e3a9
Revises: 2e541a1dcfed
Create Date: 2015-10-29 08:36:31.726728

"""

# revision identifiers, used by Alembic.
revision = '40e67319e3a9'
down_revision = '2e541a1dcfed'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


def upgrade():
    op.add_column('dag_run', sa.Column('conf', sa.PickleType(), nullable=True))


def downgrade():
    op.drop_column('dag_run', 'conf')
