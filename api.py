from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from apis import apiv1

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'super-secret'  
jwt = JWTManager(app)

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return {'message': 'Username and password are required'}, 400
        
        if username != 'admin' or password != 'admin':
            return {'message': 'Invalid credentials'}, 401
        access_token = create_access_token(identity=username)
        return {'access_token': access_token}, 200

class Protected(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        data = {"message": f"Device used by user {current_user} is RTX 4090"}
        return jsonify(data)

api.add_resource(Login, '/login')
api.add_resource(Protected, '/protected')
api.add_resource(apiv1.device,'/')
app.register_blueprint(apiv1.device_info)

if __name__ == '__main__':
    app.run(debug=True)
