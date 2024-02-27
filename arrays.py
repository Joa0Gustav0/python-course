my_friends = ["Mariana", "Wynne", "Mozart", "Beatriz", "Isabela"];

my_bestie = my_friends[0];
not_my_bestie = my_friends[
  (my_friends.index(my_bestie) + 1):
]

print("My best friend is:", my_bestie);
print(not_my_bestie, "are my other friends.");

#Arrays Functions
#.extend()
#Just pretend zero is a positive number 🦄
positive_numbers = [0, 1, 2, 3]; 
negative_numbers = [-3, -2, -1];

interger_numbers = negative_numbers;
interger_numbers.extend(positive_numbers);
print("The integer numbers (with absolute value <= 3) are:");
print(interger_numbers);

#add new array element on the right -> .append()
favorite_foods = ["🍕","🍔","🍍","🍞"];
favorite_foods.append("🍳");

print("My favorite foods are: \n" + str(favorite_foods));

#add new array element on an specific index (Dont remove any element) -> .insert()
favorite_foods.insert(1, "🍟");
print("I missed one favorite food:\n" + str(favorite_foods));

#remove an specific array element -> .remove(element)
favorite_foods.remove("🍕")
print("I ate the pizza:\n" + str(favorite_foods));

#remove all array elements -> .clear()
favorite_foods.clear();
print("Now, ate everything:\n" + str(favorite_foods));

#remove last array element -> .pop()
orders = ["hamburger", "pizza", "french-fries"];

print("I have some orders:\n" + str(orders));
orders.pop();
print("I've done the last entry order:\n" + str(orders));

#order the array -> .sort()
letters = ["z", "t", "b", "d", "a"];
letters.sort();
print("The letters were organized:\n" + str(letters));

#count how many times an array element appears -> .count()
rats_and_cheeses = ["🐀", "🧀", "🐀", "🐀", "🧀"];
print(
  "In", str(rats_and_cheeses) + "\n" +
  "There are", rats_and_cheeses.count("🐀"), "🐀.\n" +
  "And ", rats_and_cheeses.count("🧀"), "🧀."
)

#List Creation With Expressions -> [expression]
even_numbers = [2, 4, 6, 8, 10];

even_numbers_second_power = [number**2 for number in even_numbers];
print(even_numbers_second_power);