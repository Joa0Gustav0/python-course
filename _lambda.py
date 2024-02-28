#Lambda Functions are commum functions with a single line expression
#Lambda Function Structure -> lambda arguments :

#Commum Function
def getNumberPower(number, exponent) :
  return number**exponent;
print(getNumberPower(9, 2));

#Lambda Function
print((lambda number, exponent : number**exponent)(9, 2));

#Sort a list of tuples by second key
coordinates = [(5,9), (3,2), (8,7), (-4, 5)];
coordinates = sorted(coordinates, key=lambda element : element[1])

print(coordinates)

#Map and Lambda
numbers = [5, 9, 2, 7];
second_powers = list(map(lambda number: number**2, numbers));

print(second_powers);

#Filter and Lambda
ages = [12, 32, 17, 49];
adults = list(filter(lambda age: age >= 18, ages));

print(adults);

#Reduce and Lambda
from functools import reduce

money_saving_per_month = [50, 24, 89, 100];
total_saving = reduce(lambda previous, current: previous + current, money_saving_per_month);

print(total_saving);