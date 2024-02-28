import time;

def trackFunctionTime(func) :
  initial_time = time.time();
  time.sleep(10**-3);
  print(f"Function took {time.time() - initial_time}s");
  return func;

#@trackFunctionTime
def getTwoNumbersSum(number_one, number_two) :
  return number_one + number_two;

#print(getTwoNumbersSum(2, 5));

#Repeat functions with decorators

def repeat(times) :
  def func_wrapper(function) :
    def args_wrapper(*args, **kwargs) :
      for time in range(times) :
        call = function(*args, **kwargs);
    return args_wrapper;
  return func_wrapper;

@repeat(10)
def sendGreeting(name) :
  print(f"Welcome, {name}!");
sendGreeting("Robert");