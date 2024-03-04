import mysql.connector;

database_connection = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "2409SQLGustav@@2409",
  database = "my_market"
)
cursor = database_connection.cursor();

cursor.execute("SELECT * FROM items;");
data = cursor.fetchall();

for item in data :
  print(f"{item}\n");

cursor.close();
database_connection.close();

#For "cruding" in a database: 
#-> 1º Establish a connection 
#-> 2º Set a cursor for mediating the connection
#-> 3º Close the cursor and the connection after all.