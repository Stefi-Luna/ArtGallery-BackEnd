from flask import Blueprint, request
from src.services.AdminServices import AdminServices
from src.models.userModel import Users

main = Blueprint('userspost_users_blueprint',__name__)

@main.route('/', methods=['GET'])
def get_users():
    
    get_userspost_users=AdminServices.get_users()
    print(get_users)

    print('Esto se imprime en consola, GET')
    return 'Get exitoso'

@main.route('/create',methods=['POST'])
def post_users():

    ID_User = request.json['ID_User']
    Name = request.json['Name']
    Phone = request.json['Phone']
    Email = request.json['Email']
    Password = request.json['Password']

    user1 = Users(ID_User,Name,Phone,Email,Password)

    post_users=AdminServices.post_users(user1)
    print(post_users)

    print('Esto se imprime en consola, PUT')
    return 'Create exitoso'

@main.route('/update',methods=['PUT'])
def update_users():

    ID_User = request.json['ID_User']
    Name = request.json['Name']
    Phone = request.json['Phone']
    Email = request.json['Email']
    Password = request.json['Password']

    user1 = Users(ID_User,Name,Phone,Email,Password)

    update_users=AdminServices.update_users(user1)
    print(update_users)

    print('Esto se imprime en consola, UPDATE')
    return 'Update exitoso'

@main.route('/remove',methods=['DELETE'])
def delete_users():

    ID_User = request.json['ID_User']

    delete_users=AdminServices.delete_users(ID_User)
    print(delete_users)

    print('Esto se imprime en consola, DELETE')
    return 'Delete exitoso'