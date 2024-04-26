from flask import Blueprint, request, jsonify
from src.services.AuthService import AuthService


login_routes = Blueprint('login_routes', __name__)


@login_routes.route('/api/login', methods=['POST'])
def login():
   
    Name = request.json.get('name')
    Password = request.json.get('password') 
    print(Name)
    print(Password)
   
    
    
    user_data = AuthService.authenticate(Name, Password)

    if user_data:
       
        Name = user_data['Name']
        Role = user_data['Role']

        
        token = AuthService.generate_token(Name)
        print(token)
        
        response = {
            'token': token,
            'role': Role
        }
        
        return jsonify(response), 200
    else:
        
        return jsonify({'error': 'Datos no válidos'}), 401