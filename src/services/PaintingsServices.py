from src.database.db_mysql import get_connection;
from src.models.artisticModel import Artistics

class PaintingsServices():

    @classmethod
    def get_Artistics(cls):
        try:
            connection= get_connection()
            print(connection)
            
            with connection.cursor() as personal_gallery:
                personal_gallery.execute('SELECT * FROM artistic')
                result= personal_gallery.fetchall()
                print(result)
            
            connection.close()
            return 'Artistics showed'

        except Exception as ex:
            print(ex)

    @classmethod
    def post_Artistics(cls, Artistics: Artistics):
        try:
            connection= get_connection()
            print(connection)

            with connection.cursor() as personal_gallery:
                ID_Art = Artistics.ID_Art
                ID_User = Artistics.ID_User
                Title = Artistics.Title
                Description = Artistics.Description
                Measurements = Artistics.Measurements
                Unit_Price = Artistics.Unit_Price
                Image = Artistics.Image
                Stock = Artistics.Stock
                
                personal_gallery.execute("INSERT INTO `Artistics` (`ID_Art`, `ID_User`, `Title`, `Description`, `Measurements`, `Unit_Price`, `Image`, `Stock`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                                     (ID_Art, ID_User, Title, Description, Measurements, Unit_Price, Image, Stock))
                connection.commit()
            
            connection.close()
            return 'Artistics new posted'

        except Exception as ex:
            print(ex)


    @classmethod
    def update_Artistics(cls, Artistics: Artistics):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as personal_gallery:
                ID_Art = Artistics.ID_Art
                ID_User = Artistics.ID_User
                Title = Artistics.Title
                Description = Artistics.Description
                Measurements = Artistics.Measurements
                Unit_Price = Artistics.Unit_Price
                Image = Artistics.Image
                Stock = Artistics.Stock

                personal_gallery.execute("UPDATE Artistics SET ID_User = %s, Title = %s, Description = %s, Measurements = %s, Unit_Price = %s, Image = %s, Stock = %s WHERE ID_Art = %s",
                                     (ID_User, Title, Description, Measurements, Unit_Price, Image, Stock, ID_Art))
                connection.commit()

            connection.close()
            return 'Artistics updated'

        except Exception as ex:
            print(ex)



    @classmethod
    def delete_Artistics(cls, ID_Art: int):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as personal_gallery:

                personal_gallery.execute("DELETE FROM Artistics WHERE ID_Art = %s", (ID_Art))
                connection.commit()

            connection.close()
            return 'Artistics removed'

        except Exception as ex:
            print(ex)