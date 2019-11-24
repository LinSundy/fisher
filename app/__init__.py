from flask import Flask


def register_blueprint(app):
    from app.web.book import book
    app.register_blueprint(book)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.debug = True
    register_blueprint(app)
    return app
