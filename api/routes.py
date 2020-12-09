from aiohttp.web import Application, view
from api.web.views import *


def setup_routes(app: Application):
    app.add_routes([
        view('/group/{id}', GroupView),
        view('/group', GroupView),
        view('/contact/{id}', ContactView),
        view('/contact', ContactView)
    ])
