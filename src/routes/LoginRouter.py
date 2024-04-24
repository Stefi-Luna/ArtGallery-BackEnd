from flask import Blueprint, request, jsonify
from src.services.AuthService import AuthService


login_routes = Blueprint('login_routes', __name__)


@login_routes.route('/api/login', methods=['POST'])
def login():
   
    Name = request.json.get('name')
    Password = request.json.get('password') 
    print(Name)
    print(Password)
   
    
    #  verificar las credenciales en la base de datos
    user_data = AuthService.authenticate(Name, Password)

    if user_data:
        # Obtener el nombre y el rol del usuario autenticado
        Name = user_data['Name']
        Role = user_data['Role']

        # Generar el token JWT para el usuario
        token = AuthService.generate_token(Name)
        print(token)
        # Devolver la respuesta con el token y el rol del usuario
        response = {
            'token': token,
            'role': Role
        }
        
        return jsonify(response), 200
    else:
        
        return jsonify({'error': 'Datos no válidos'}), 401