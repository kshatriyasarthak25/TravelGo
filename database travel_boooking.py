import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='sarthak25',database='travel_booking')
c1=conn.cursor()
if conn.is_connected:
    c1.execute("create database travel_bookings;")
    print("database created successfully")
