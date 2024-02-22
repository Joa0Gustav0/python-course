#Integer Number
number_one = 2;

#Floating Number
number_two = 4.7896;

#Sum
print(number_one + number_two);
#Subtract
print(number_one - number_two);
#Divide
print(number_one / number_two);
#Time
print(number_one * number_two);

#Convert number to string -> str(number_value)
print(str(number_one) + ", now, can concatenate with text.");

#Absolute value of a number -> abs()
print(abs(-57));

#Power value of a number -> pow()
print(pow(2, 9)); #equal to 2^9

#Max and min value -> max() && min()
print(
  "The minor value between", 
  number_one, 
  "and", number_two, 
  "is", min(number_one, number_two), ".");

print(
  "The major value between", 
  number_one, 
  "and", number_two, 
  "is", max(number_one, number_two), ".")

#Get rounded value -> round()
print(
  "The rounded value of",
  number_two,
  "is", round(number_two), "."
);

#Math Lib
from math import *

#sqrt() is a math lib's function for get the square root of number
print(round(sqrt(81)));
