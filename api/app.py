from aiohttp.web import Application, run_app
from aiohttp_apispec import validation_middleware, setup_aiohttp_apispec
from api.web.middlewares import catch_errors_middleware
from api.db.managers.db_manager import DbManager
from api.routes import setup_routes


def create_app():
    app = Application(
        middlewares=[validation_middleware, catch_errors_middleware]
    )
    setup_routes(app)
    app.on_startup.append(DbManager.connect_db)
    app.on_cleanup.append(DbManager.close_db)

    setup_aiohttp_apispec(app=app, title="Contacts Api Documentation", version="v1")

    return app
