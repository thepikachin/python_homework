import mysql.connector

def typesearch(country):
    sql = (f"select type, count(*) from airport where iso_country = '{country}' group by type")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for type in result:
        print(f"{type[0]}: {type[1]}")
    return

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'pikachu69',
    autocommit = True
)

country = input("Anna maakoodi: ")
typesearch(country)