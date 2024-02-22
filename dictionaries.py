animals = {
  "🐒": "Monkey",
  "🦍": "Gorilla",
  "🦜": "Parrot",
  "🐕": "Dog",
  "🐈": "Cat",
  "🐐": "Goat",
  "🐘": "Elephant",
  "🐢": "Turtle",
  "🐟": "Fish"
};

query_target = input("Insert a animal emoji: ");
print(
  query_target + ":", 
  animals.get(query_target, "Not found in the dictionary.")
);