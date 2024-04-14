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
                print(result)
            
            connection.close()
            return 'Lista mostrada'

        except Exception as ex:
            print(ex)

    @classmethod
    def post_products(cls,product: Users):
        try:
            connection= get_connection()
            print(connection)

            with connection.cursor() as admin_page:
                ID_User=ID_User
                Name=Name
                Phone=Phone
                Email=Email
                Password=Password
                
                admin_page.execute("INSERT INTO `user` (`ID_User`, `Name`, `Phone`, `Email`, `Password`) VALUES (%s, %s, %s, %s, %s);",
                                     (ID_User, Name, Phone, Email, Password,))
                connection.commit()
            
            connection.close()
            return 'user ingresado'

        except Exception as ex:
            print(ex)


    @classmethod
    def update_products(cls, product: Users):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as admin_page:
                ID_User = product.ID_User
                Name = product.Name
                Phone = product.Phone
                Email = product.Email
                Password = product.Password
                Stock = product.Stock

                admin_page.execute("UPDATE user SET Name = %s, Phone = %s, Email = %s, Password = %s, Stock = %s WHERE ID_User = %s",
                                     (Name, Phone, Email, Password, Stock, ID_User))
                connection.commit()

            connection.close()
            return 'user actualizado'

        except Exception as ex:
            print(ex)



    @classmethod
    def delete_products(cls, ID_User: int):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as admin_page:

                admin_page.execute("DELETE FROM user WHERE ID_User = %s", (ID_User))
                connection.commit()

            connection.close()
            return 'user eliminado'

        except Exception as ex:
            print(ex)