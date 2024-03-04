from crud import executeSQLCommand;
import random
import os

clear = lambda : os.system('cls' if os.name == 'nt' else 'clear');


program_on_process = True;


def setLineBreak() :
  print("+-------------------------------+");


def getUserAction() :
  action = requestUserAction();
  while action == None :
    action = requestUserAction();

  return action;

def requestUserAction() :
  setLineBreak();
  print(f"Available Actions:\n{"".join([f"| {action} |" for action in available_actions.keys()])}\n");
  return validateUserAction(input("Insert one of the actions above: "));

def validateUserAction(user_input) :
  if user_input not in "NI | VI | E" :
    clear();
    print("\n⚠ This is not recognized as an available action. Try again.\n");
    return None;
  
  return user_input;

def executeAction(user_action) :
  for action in available_actions.items() :
    if user_action in action[0] :
      action[1]();

      return True;

  return False;


def addNewItem() :
  item_data = getItemData();

  if executeSQLCommand(
    f"INSERT INTO items (Item_Name, Item_Barcode, Item_Price) VALUES (\'{item_data["name"]}\', \'{item_data["barcode"]}\', {item_data["price"]});"
  ) :
    print("A new item was added.");
  else :
    print("⚠ An error ocurred. Try again later.");


def getItemData() :
  clear();
  item_data = requestInputForItemData();

  while item_data == None :
    clear();
    item_data = requestInputForItemData();

  return item_data;

def requestInputForItemData() :
  return validateItemData({
    "name" : input("Insert the name for your product (max.: 30 char.): "),
    "barcode" : random.randint(100000000000, 999999999999),
    "price" : input("Insert the price of your product: ")
  });

def validateItemData(item_data) :
  for key, value in item_data.items() :
    if key == "name" :
      if len(item_data[key]) > 30 :
        print("⚠ Product name should contain a 30 characters maximum. Try again.");
        return None;
      #Check if is contained in database(MISSING! 💡)

    if key == "price" :
      if float(item_data[key]) <= 0 :
        print("⚠ This is not a valid product price.");
        return None;

  return item_data;

def viewItems() :
  response = executeSQLCommand("SELECT * FROM items;")
  if response :
    clear()
    setLineBreak();
    for item_id, item_name, item_barcode, item_price in response :
      print("{} | ${}\n".format(item_name, item_price));


def endProgram() :
  program_on_process = False;

available_actions = {
  "New Item(NI)" : addNewItem,
  "View Items(VI)" : viewItems,
  "Exit Program(E)" : endProgram
}

while program_on_process :
  user_action = getUserAction();

  if user_action == "E" :
    program_on_process = False;
  else : 
    executeAction(user_action);

clear();
print("⚠ Program Execution was Ended.")