from sqlalchemy import (
    Table, Column, Integer, String
)
from api.db.models import meta


group = Table(
    'group', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False)
)
