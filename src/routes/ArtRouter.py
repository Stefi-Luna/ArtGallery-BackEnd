from flask import Blueprint, request, jsonify
from src.services.ArtServices import ArtServices
from src.models.artisticModel import Artistic

main = Blueprint('artistics_blueprint',__name__)

@main.route('/', methods=['GET'])
def get_Artistic():
    
    get_Artistic=ArtServices.get_Artistic()
    print(get_Artistic)

    print('Esto se imprime en consola, GET')
    return jsonify(get_Artistic)

@main.route('/create',methods=['POST'])
def post_Artistic():

    ID_Art = ""
    ID_User = request.json['ID_User']
    Title = request.json['Title']
    Description = request.json['Description']
    Measurements = request.json['Measurements']
    Unit_Price = request.json['Unit_Price']
    Image = request.json['Image']
    Stock = request.json['Stock']

    painting1 = Artistic(ID_Art,ID_User,Title,Description,Measurements,Unit_Price,Image,Stock)

    post_Artistics=ArtServices.post_Artistics(painting1)
    print(post_Artistics)

    print('Esto se imprime en consola, PUT')
    return 'Create exitoso'

@main.route('/update',methods=['PUT'])
def update_Artistics():

    ID_Art = request.json['ID_Art']
    ID_User = request.json['ID_User']
    Title = request.json['Title']
    Description = request.json['Description']
    Measurements = request.json['Measurements']
    Unit_Price = request.json['Unit_Price']
    Image = request.json['Image']
    Stock = request.json['Stock']

    painting1 = Artistic(ID_Art,ID_User,Title,Description,Measurements,Unit_Price,Image,Stock)

    update_Artistics=ArtServices.update_Artistics(painting1)
    print(update_Artistics)

    print('Esto se imprime en consola, UPDATE')
    return 'Update exitoso'

@main.route('/remove',methods=['DELETE'])
def delete_Artistics():

    ID_Art = request.json['ID_Art']

    delete_Artistics=ArtServices.delete_Artistics(ID_Art)
    print(delete_Artistics)

    print('Esto se imprime en consola, DELETE')
    return 'Delete exitoso'