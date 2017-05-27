from flask import Flask
from .models import db
from .mail import mail


def create_app(config_module=None):
    app = Flask(__name__, static_url_path="")

    app.config.from_object(config_module or 'config')

    db.init_app(app)
    mail.init_app(app)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        """Catch all that redirects to index.html for the single page
        application
        """
        return app.send_static_file('index.html')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
