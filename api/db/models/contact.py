from sqlalchemy import (
    Table, Column, Integer, String, ForeignKey
)
from api.db.models import meta


contact = Table(
    'contact', meta,
    Column('id', Integer, primary_key=True),
    Column('firstname', String(30), nullable=False),
    Column('lastname', String(30), nullable=False),
    Column('phone', String(16), nullable=False),
    Column(
        'group_id',
        Integer,
        ForeignKey('group.id', ondelete='CASCADE'),
        nullable=False
    )
)
