import mysql.connector
import geopy.distance

def distancesearch(airport1, airport2):
    sql = (f"select ident, name, latitude_deg, longitude_deg from airport where ident = '{airport1}'")
    result = sqlexecute(sql)
    coord1 = result[0]
    sql = (f"select ident, name, latitude_deg, longitude_deg from airport where ident = '{airport2}'")
    result = sqlexecute(sql)
    coord2 = result[0]
    distance = (geopy.distance.geodesic( (coord1[2:]), (coord2[2:]) ).km)
    return coord1, coord2, distance

def sqlexecute(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = 'pikachu69',
    autocommit = True,
)

airport1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
airport2 = input("Anna toisen lentokentän ICAO-koodi: ")
coord1, coord2, distance = distancesearch(airport1, airport2)
print(f"Lentokenttien {coord1[1]} ja {coord2[1]} välinen etäisyys on {distance:.2f} kilometriä.")