from flask import Blueprint, request
from src.services.PaintingsServices import PaintingsServices
from src.models.artisticModel import Artistics

main = Blueprint('paintings_blueprint',__name__)

@main.route('/', methods=['GET'])
def get_Artistics():
    
    get_paintings=PaintingsServices.get_Artistics()
    print(get_Artistics)

    print('Esto se imprime en consola, GET')
    return 'Get exitoso'

@main.route('/create',methods=['POST'])
def post_Artistics():

    ID_Art = request.json['ID_Art']
    ID_User = request.json['ID_User']
    Title = request.json['Title']
    Description = request.json['Description']
    Measurements = request.json['Measurements']
    Unit_Price = request.json['Unit_Price']
    Image = request.json['Image']
    Stock = request.json['Stock']

    painting1 = Artistics(ID_Art,ID_User,Title,Description,Measurements,Unit_Price,Image,Stock)

    post_paintings=PaintingsServices.post_Artistics(painting1)
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

    painting1 = Artistics(ID_Art,ID_User,Title,Description,Measurements,Unit_Price,Image,Stock)

    update_paintings=PaintingsServices.update_Artistics(painting1)
    print(update_Artistics)

    print('Esto se imprime en consola, UPDATE')
    return 'Update exitoso'

@main.route('/remove',methods=['DELETE'])
def delete_Artistics():

    ID_Art = request.json['ID_Art']

    delete_paintings=PaintingsServices.delete_Artistics(ID_Art)
    print(delete_Artistics)

    print('Esto se imprime en consola, DELETE')
    return 'Delete exitoso'