from flask import Blueprint, request, jsonify
from src.services.AdminServices import AdminServices
from src.models.userModel import Users
from flask_cors import CORS

main = Blueprint('users_blueprint',__name__)
cors = CORS(main, origins='*')

@main.route('/', methods=['GET'])
def get_users():
    
    get_users=AdminServices.get_users()
    print(get_users)

    print('Esto se imprime en consola, GET')
    return jsonify(get_users)

@main.route('/create',methods=['POST'])
def post_users():
    ID_User = ""
    ID_Usertype = request.json['ID_Usertype']
    Name = request.json['Name']
    Phone = request.json['Phone']
    Email = request.json['Email']
    Password = request.json['Password']

    user1 = Users(ID_User,ID_Usertype,Name,Phone,Email,Password)

    post_users=AdminServices.post_users(user1)
    print(post_users)

    return 'Create exitoso'

@main.route('/update',methods=['PUT'])
def update_users():

    ID_User = request.json['ID_User']
    ID_Usertype = request.json['ID_Usertype']
    Name = request.json['Name']
    Phone = request.json['Phone']
    Email = request.json['Email']
    Password = request.json['Password']

    user1 = Users(ID_User,ID_Usertype,Name,Phone,Email,Password)

    update_users=AdminServices.update_users(user1)
    print(update_users)

    return 'Update exitoso'

@main.route('/remove',methods=['DELETE'])
def delete_users():

    ID_User = request.json['ID_User']

    delete_users=AdminServices.delete_users(ID_User)
    print(delete_users)

    return 'Delete exitoso'