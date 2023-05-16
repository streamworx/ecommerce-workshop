from flask import Response
from flask import request as flask_request
# from flask_cors import CORS

from bootstrap import create_app

app = create_app()
# CORS(app)

@app.route('/')
def hello():
    app.logger.info("home url for ads called")
    return Response({'Hello from Advertisements!': 'world'}, mimetype='application/json')
