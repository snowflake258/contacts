import sqlalchemy
from api.db.models import meta, group, contact


def create_db():
    engine = sqlalchemy.create_engine('postgresql://contacts_api:qdg058znm230@127.0.0.1:5432/contacts')
    meta.create_all(
        bind=engine,
        tables=[group, contact]
    )


if __name__ == '__main__':
    create_db()
