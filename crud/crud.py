#CRUD - Python & MySQL
def executeSQLCommand(command) :
  import mysql.connector;

  #Stablish connection with the database
  #Create the connection -> mysql.connector
  database_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2409SQLGustav@@2409",
    database = "my_market"
  )

  #Execute the connection -> .cursor()
  connection_cursor = database_connection.cursor();
  
  try :
    connection_cursor.execute(command);
    if "SELECT" in command :
      return connection_cursor.fetchall()

    database_connection.commit();

    #Split the connection -> .close()
    connection_cursor.close();
    database_connection.close();
  
    return True;
  except :
    print("⚠ Some error ocurred. Try again later.");

    #Split the connection -> .close()
    connection_cursor.close();
    database_connection.close();

    return False;


