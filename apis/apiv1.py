from flask import Blueprint ,request , jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

API_KEY = "my_secret_key"
device_info = Blueprint("device",__name__)

class device(Resource):
    @jwt_required
    def get(self):
        api_key = request.headers.get('X-API-Key')
        if api_key != API_KEY:
            return {'message': 'API key authentication required'}, 401
        data = {"message": "RTX 4090"}
        return jsonify(data)

