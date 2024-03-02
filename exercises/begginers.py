#Python program to check whether the given number is even or not.
def classifyEvenOrOdd(number) :
  if number % 2 == 0 :
    return "The number {} is even.".format(number);
  else :
    return "The number {} is odd.".format(number);

print(classifyEvenOrOdd(40));

#Python program to convert the temperature in degree centigrade to Fahrenheit
def converToFahrenheit(celsius_temperature) :
  return "{}°C is equal to {}°F.".format(celsius_temperature, celsius_temperature * 1.8 + 32);

print(converToFahrenheit(32));

#Python program to find the area of a triangle whose sides are given
def getTriangleArea(base, height) :
  print("The area of a triangle, which it's base is {}cm and it's height is {}cm, is: {}".format(
    base, height, base * height / 2
  ));

getTriangleArea(4, 6);

#Python program to find out the average of a set of integers
from functools import reduce

numbers = set([6, 7.25, 8.4, 5]);
average = reduce(lambda prev_val, curr_val: prev_val + curr_val, numbers) / len(numbers);

print(average);

#Python program to find the product of a set of real numbers
result = reduce(lambda prev_val, curr_value: prev_val * curr_value, numbers);
print(result);

#Python program to find the circumference and area of a circle with a given radius
radius = float(input("Insert the radius length of a circle: "));
circumference = 2 * 3.14 * radius;
area = 3.14 * radius**2;

print("For a circle which it's radius is {}cm, \nThe circumference is {}cm, \nAnd the are is {}cm.".format(radius, circumference, area));


def checkMultiple(number, multiple_base) :
  if number % multiple_base == 0 :
    print("The number {} is a multiple of {}.".format(number, multiple_base));
    return True;
  else :
    print("The number {} is NOT a multiple of {}.".format(number, multiple_base))
    return False;


#Python program to check whether the given integer is a multiple of 5
number = int(input("Insert a number: "));
checkMultiple(number, 5)

#Python program to find the average of 10 numbers using while loop
sum = 0;
for number in [6, 7.25, 8.4, 5, 8, 2, 5.5, 7, 10]:
  sum += number;

average = sum / 10;
print(average);

#Python program to find the sum of the digits of an integer using a while loop
digits = list(input("Insert a number: "));
digits_sum = reduce(lambda prev_val, curr_val: int(prev_val) + int(curr_val), digits);

print(digits_sum);
