from functools import reduce

def getNumbersSum(*numbers) :
  return reduce(lambda prev_value, curr_value: prev_value + curr_value, numbers);

print(getNumbersSum(2, 4, 6));
