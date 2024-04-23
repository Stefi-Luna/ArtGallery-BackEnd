from ..database.db_mysql import get_connection
from flask import Flask, jsonify
import jwt
from config import Config

class AuthService():

    @classmethod
    def authenticate(cls, Name, Password):
        try: 
            connection = get_connection()
        
            with connection.cursor() as cursor:
                # Ejecutar la consulta SQL para verificar el nombre de usuario y la contraseña
                cursor.callproc("AuthenticateUser", (Name, Password))
                print("rrrrrrrrrrrrrrrrrrrrrrr")
                print(Name)
                print(Password)
                print("rrrrrrrrrrrrrrrrrrrrrrr")
                # Obtener el resultado de la consulta
                result = cursor.fetchone()
                print(result)
                print(jsonify(result)) 
                if result:
                    # Si el usuario y la contraseña son válidos, retornar el ID de usuario y el rol
                    # return {'Name': result['Name'], 'Role': result['Role']}
                     return {'Name': result[1], 'Role': result[2]}
                else:
                    # Si no se encuentra un usuario con esas credenciales, retornar None
                    return None
                
        except Exception as ex:
            print ("gggggggggggggggggggggggggg")
            # Manejar cualquier excepción que pueda ocurrir durante la autenticación
            print(ex)

    @classmethod
    def generate_token(cls, Name):
        payload = {'name': Name}
        secret_key = Config.SECRET_KEY  # Utiliza la clave secreta de la configuración
        algorithm = 'HS256'  # Algoritmo de encriptación
        
        # Generar el token utilizando la librería JWT
        token = jwt.encode(payload, secret_key, algorithm=algorithm)
        
        return token
       



























































# class AuthService():

#     @classmethod
#     def authenticate(cls, Name, Password):
#         try: 
#             connection = get_connection()
        
#             with connection.cursor() as cursor:
#                 # Ejecutar la consulta SQL para verificar el nombre de usuario y la contraseña
#                 cursor.execute("SELECT user.ID_User, user.Name, user_type.Role as Role FROM user INNER JOIN user_type ON user.ID_Usertype = user_type.ID_Usertype WHERE user.Name = %s AND user.Password = %s", (Name, Password))
#                 print("rrrrrrrrrrrrrrrrrrrrrrr")
#                 print(Name)
#                 print(Password)
#                 print("rrrrrrrrrrrrrrrrrrrrrrr")
#                 # Obtener el resultado de la consulta
#                 result = cursor.fetchone()
#                 print(result)
#                 print(jsonify(result)) 
#                 if result:
#                     # Si el usuario y la contraseña son válidos, retornar el ID de usuario y el rol
#                     # return {'Name': result['Name'], 'Role': result['Role']}
#                      return {'Name': result[1], 'Role': result[2]}
#                 else:
#                     # Si no se encuentra un usuario con esas credenciales, retornar None
#                     return None
                
#         except Exception as ex:
#             print ("gggggggggggggggggggggggggg")
#             # Manejar cualquier excepción que pueda ocurrir durante la autenticación
#             print(ex)

#     @classmethod
#     def generate_token(cls, Name):
#         payload = {'name': Name}
#         secret_key = Config.SECRET_KEY  # Utiliza la clave secreta de la configuración
#         algorithm = 'HS256'  # Algoritmo de encriptación
        
#         # Generar el token utilizando la librería JWT
#         token = jwt.encode(payload, secret_key, algorithm=algorithm)
        
#         return token
       
