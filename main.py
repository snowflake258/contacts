from api.app import create_app


app = create_app()


if __name__ == '__main__':
    from aiohttp.web import run_app
    run_app(app)
