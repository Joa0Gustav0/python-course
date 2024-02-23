math_operation_realized = False;

def executeCalculator() :
  calculator_user_input = getCalculatorUserInputs();
  operation_result = getOperationResult(calculator_user_input);
  if operation_result == None : return False;

  return displayOperationResult(calculator_user_input, operation_result);

def getCalculatorUserInputs() :
  user_inputs = requestUserInputs();

  while validateUserInputs(user_inputs) == None :
    throwCalculatorWarning("Some inserted informations are not valid. Try again.");
    user_inputs = requestUserInputs();

  return user_inputs;
def throwCalculatorWarning(message) :
  print("\n⚠", message);
  print("+-----------------------------------------------------+");
def requestUserInputs() :
  return {
    "first_number": setNumberInput("first"),
    "math_operator": getOperator(),
    "second_number": setNumberInput("second")
  }

def setNumberInput(order_number) :
  try :
    return int(input("Insert the " + order_number + " number: "));
  except ValueError:
    return None;

def getOperator() :
  math_operator = input("Insert the operator: ");

  if math_operator == "+" :
    return "sum";
  elif math_operator == "-" :
    return "subtraction";
  elif math_operator == "*" :
    return "multiplication";
  elif math_operator == "/" :
    return "division";
  else :
    return None;

def validateUserInputs(user_inputs) :
  inputs_for_validation = [
    "first_number", "math_operator", "second_number"
  ];

  if (user_inputs["first_number"] != None
      and user_inputs["math_operator"] == "division"
      and user_inputs["second_number"] == 0) :
    throwCalculatorWarning("Why dividing by 0? (All numbers divide by 0 is 0)");
    return None;

  for _input in inputs_for_validation :
    if user_inputs[_input] == None :
      return None;

  return True;


def getOperationResult(user_input) :
  if user_input["math_operator"] == "sum" :
    return user_input["first_number"] + user_input["second_number"];

  elif user_input["math_operator"] == "subtraction" :
    return user_input["first_number"] - user_input["second_number"];

  elif user_input["math_operator"] == "multiplication" :
    return user_input["first_number"] * user_input["second_number"];

  elif user_input["math_operator"] == "division":
    return user_input["first_number"] / user_input["second_number"];

  else :
    throwCalculatorWarning("Some error ocurred. Try again.");
    return None; 
def displayOperationResult(user_input, operation_result) :
  print(
    "The", user_input["math_operator"], 
    "between", str(user_input["first_number"]), "and", str(user_input["second_number"]), 
    "is", str(operation_result),
    )
  
  return True;

while math_operation_realized != True :
  math_operation_realized = executeCalculator();

print("+---------------------------+");
print("End!");

