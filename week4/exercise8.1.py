import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'pikachu69',
    autocommit = True
)

icaosearch = input("Anna lentokentän ICAO-koodi: ")

sql = (f"select ident, name, municipality from airport where ident = '{icaosearch}'")
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
airport = result[0]
print(f"Lentokenttä {airport[1]} sijaitsee kunnassa {airport[2]}.")