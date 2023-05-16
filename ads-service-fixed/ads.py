from flask import Response, Flask
from flask import request as flask_request

def create_app():
    """Create a Flask application"""
    app = Flask(__name__)
    return app

app = create_app()


@app.route('/')
def hello():
    app.logger.info("home url for ads called")
    return Response({'Hello from Advertisements!': 'world'}, mimetype='application/json')
