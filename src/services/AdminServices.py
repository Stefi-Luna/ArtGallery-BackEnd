from src.database.db_mysql import get_connection;
from src.models.userModel import Users

class AdminServices():

    @classmethod
    def get_users(cls):
        try:
            connection= get_connection()
            print(connection)
            
            with connection.cursor() as admin_page:
                admin_page.execute('SELECT * FROM user')
                result= admin_page.fetchall()

            user_objects = []
            for user in result:
                usuario = {
                    'ID_User': user[0],
                    'ID_Usertype': user[1],
                    'Name': user[2],
                    'Phone': user[3],
                    'Email': user[4],
                    'Password': user[5],
                    # Añade más campos según la estructura de tu tabla 'user'
                }
                user_objects.append(usuario)

            print(result)
            
            connection.close()
            return user_objects

        except Exception as ex:
            print(ex)

    @classmethod
    def post_users(cls, user: Users):
        try:
            connection= get_connection()
            print(connection)

            with connection.cursor() as admin_page:
                ID_Usertype = user.ID_Usertype
                Name = user.Name
                Phone = user.Phone
                Email = user.Email
                Password = user.Password
                
                admin_page.execute("INSERT INTO `user` (`ID_Usertype`, `Name`, `Phone`, `Email`, `Password`) VALUES (%s, %s, %s, %s, %s);",
                                     (ID_Usertype, Name, Phone, Email, Password,))
                connection.commit()
            
            connection.close()
            return 'User new posted'

        except Exception as ex:
            print(ex)


    @classmethod
    def update_users(cls, user: Users):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as admin_page:
                ID_User = user.ID_User
                ID_Usertype = user.ID_Usertype
                Name = user.Name
                Phone = user.Phone
                Email = user.Email
                Password = user.Password

                admin_page.execute("UPDATE user SET ID_Usertype = %s, Name = %s, Phone = %s, Email = %s, Password = %s WHERE ID_User = %s",
                                     (ID_Usertype, Name, Phone, Email, Password, ID_User))
                connection.commit()

            connection.close()
            return 'User updated'

        except Exception as ex:
            print(ex)



    @classmethod
    def delete_users(cls, ID_User: int):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as admin_page:

                admin_page.execute("DELETE FROM user WHERE ID_User = %s", (ID_User))
                connection.commit()

            connection.close()
            return 'User removed'

        except Exception as ex:
            print(ex)