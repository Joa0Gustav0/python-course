#while
countage_number = 10;

while countage_number >= 0 :
  print(countage_number);
  countage_number -= 1;

#for
from math import *;

numbers = [1, 9, 34, 48, 32];

for index in range(len(numbers)) :
  number = numbers[index]

  print("The 2º power of", str(number), "is", str(floor(number**2)), ".");

#2D array and nested loop
messy = [
  ["🔑", "👓", "⚽"],
  ["💄", "💍",  "🧸"],
  ["💊", "📖", "🧵"],
]
def displayMessy() :
  for y_index in range(len(messy)) :
    print(messy[y_index]);

def matchElementInList(target, list_element) :
  return target == list_element;

def queryInsideSingleList(target, list_index) :
  for x_index in range(len(messy[list_index])) :
    if matchElementInList(target, messy[list_index][x_index]) :
      return {
        "x_axis": str(x_index + 1),
        "y_axis": str(list_index + 1)
      }

def queryElementInMessy(target_element) :
  mapping_results = None;

  for y_index in range(len(messy)) :
    if (queryInsideSingleList(target_element, y_index)) :
      mapping_results = str(queryInsideSingleList(target_element, y_index));
  
  print(getQueryResult(target_element, mapping_results));
  
def getQueryResult(target, result) :
  if (result != None) :
    return "The element " + target + " was found at:\n" + result;
  
  return "The element was not found.";

print("+----------------------+");
displayMessy();
queryElementInMessy(input("Search for an element in the messy: "));
print("+----------------------+");