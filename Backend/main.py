from app import create_app
from flask import request, jsonify
from flask_cors import CORS
from  app.config import Config



app = create_app()

if __name__== 'main':
    app.run(host="0.0.0.0", port=5000)


