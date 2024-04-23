from src.database.db_mysql import get_connection;
from src.models.artisticModel import Artistic

class ArtServices():

    @classmethod
    def get_Artistic(cls):
        try:
            connection= get_connection()
            print(connection)
            
            with connection.cursor() as personal_gallery:
                personal_gallery.execute('SELECT * FROM artistic')
                result= personal_gallery.fetchall()


            art_objects = []
            for arts in result:
                art = {
                    'ID_Art': arts[0],
                    'ID_User': arts[1],
                    'Title': arts[2],
                    'Description': arts[3],
                    'Measurements': arts[4],
                    'Unit_Price': arts[5],
                    'Image': arts[6],
                    'Stock': arts[7]
                    # Añade más campos según la estructura de tu tabla 'user'
                }
                art_objects.append(art)


                print(result)
            
            connection.close()
            return art_objects

        except Exception as ex:
            print(ex)

    @classmethod
    def post_Artistics(cls, arts: Artistic):
        try:
            connection= get_connection()
            print(connection)

            with connection.cursor() as personal_gallery:
                ID_Art = arts.ID_Art
                ID_User = arts.ID_User
                Title = arts.Title
                Description = arts.Description
                Measurements = arts.Measurements
                Unit_Price = arts.Unit_Price
                Image = arts.Image
                Stock = arts.Stock
                
                personal_gallery.execute("INSERT INTO `artistic` (`ID_Art`, `ID_User`, `Title`, `Description`, `Measurements`, `Unit_Price`, `Image`, `Stock`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                                     (ID_Art, ID_User, Title, Description, Measurements, Unit_Price, Image, Stock))
                connection.commit()
            
            connection.close()
            return 'Artistics new posted'

        except Exception as ex:
            print(ex)


    @classmethod
    def update_Artistics(cls, arts: Artistic):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as personal_gallery:
                ID_Art = arts.ID_Art
                ID_User = arts.ID_User
                Title = arts.Title
                Description = arts.Description
                Measurements = arts.Measurements
                Unit_Price = arts.Unit_Price
                Image = arts.Image
                Stock = arts.Stock

                personal_gallery.execute("UPDATE artistic SET ID_User = %s, Title = %s, Description = %s, Measurements = %s, Unit_Price = %s, Image = %s, Stock = %s WHERE ID_Art = %s",
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

                personal_gallery.execute("DELETE FROM artistic WHERE ID_Art = %s", (ID_Art))
                connection.commit()

            connection.close()
            return 'Artistics removed'

        except Exception as ex:
            print(ex)