from server import create_app
from server.models import db

app = create_app()
with app.app_context():
    db.create_all()
