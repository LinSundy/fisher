from flask import Flask


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.debug = True
    register_blueprint(app)
    return app
