import file_actions;

def breakLine() :
  print("+--------------------------+");

def getUserAction() :
  required_action = createRequestForActionInput();

  while required_action == None :
    required_action = createRequestForActionInput();

  return required_action;

def createRequestForActionInput() :
  breakLine();
  print("Available actions into files:")
  print("Read File (R) || Write Into File (W) || Exit Program (E)");
  breakLine();

  return validateActionInput(input("Select one of the actions above: "));

def validateActionInput(required_action) :
  if required_action not in "R | W | E" :
    print("\n⚠ Invalid action. try again.");
    return None;
  else :
    return required_action;

def executeUserAction(user_action) :
  actions = {
    "W": requestArgsForExecuteFileAction,
    "R": requestArgsForExecuteFileAction,
  }

  actions[user_action](user_action);

def requestArgsForExecuteFileAction(action) :
  if action == "W" :
    return checkActionExecution(
      file_actions.writeIntoFile(input("Insert the target file path/name: "), input("Insert the content for being written: "))
      );
  elif action == "R" :
    return checkActionExecution(
      file_actions.showFileContent(input("Insert the target file path/name: "))
    );
  else :
    print("Some error ocurred. Try Again.")
    return False;
  
def checkActionExecution(execution_ok) :
  if execution_ok :
    print("Action was executed successfully.")
    return True;
  else :
    print("Some error ocurred while executing the action. Try Again.");
    return False;


program_running = True;
while program_running == True :
  user_action = getUserAction();
  if user_action == "E" : program_running = False;
  else : executeUserAction(user_action);

breakLine();
print("Program was ended.");