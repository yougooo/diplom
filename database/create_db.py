#!/usr/bin/python3

import psycopg2


connection_row = "dbname=environment user=alex password=95qaz26plm"

with psycopg2.connect(connection_row) as connect:
    with connect.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS results")
        cursor.execute("DROP TABLE IF EXISTS measurments")
        cursor.execute("DROP TABLE IF EXISTS stations")
        cursor.execute("DROP TABLE IF EXISTS locations")
        cursor.execute("DROP TABLE IF EXISTS metals")
        cursor.execute("DROP TABLE IF EXISTS city_metals")
        #cursor.execute("DROP TABLE IF EXISTS average")

        #cursor.execute("CREATE EXTENSION postgis")

        cursor.execute("CREATE TABLE locations(" +
                       "location_id SERIAL UNIQUE," +
                       "city VARCHAR(20) NOT NULL," +
                       "street VARCHAR(50) NOT NULL," +
                       "location geometry(Point)," +
                       "PRIMARY KEY (city, street))")

        cursor.execute("CREATE TABLE stations(" +
                       "station_id SERIAL UNIQUE," +
                       "location_id int2 REFERENCES locations (location_id),"
                       "station_code int2 NOT NULL," +
                       "PRIMARY KEY (location_id, station_code))")

        cursor.execute("CREATE TABLE metals(" +
                       "metal_id SERIAL UNIQUE," +
                       "metal_type VARCHAR(30) PRIMARY KEY)")

        cursor.execute("CREATE TABLE station_metals(" +
                       "city_metal_id SERIAL UNIQUE," +
                       "station int2 REFERENCES stations(station_id)," +
                       "ON UPDATE CASCADE ON DELETE CASCADE," +
                       "metal int2 REFERENCES metals(metal_id)" +
                       "ON UPDATE CASCADE ON DELETE CASCADE," +
                       "measure real," +
                       "PRIMARY KEY (station, metal, date))")

        cursor.execute("CREATE TABLE results(" +
                       "station_id int2 REFERENCES station (station_id)," +
                       "ON UPDATE CASCADE ON DELETE CASCADE," +
                       "filter_counter int2 NOT NULL," +
                       "volum real NOT NULL," +
                       "dust real NOT NULL," +
                       "K1 int2," +
                       "K2 int2," +
                       "K3 int2," +
                       "K4 int2," +
                       "d int2 NOT NULL," +
                       "koef real NOT NULL," +
                       "k_measur real NOT NULL," +
                       "empty_filter real NOT NULL," +
                       "norm_volum real NOT NULL," +
                       "mass_x real NOT NULL)")

