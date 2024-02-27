#Sets are unordered, mutable, distincts
#Declaring a set -> {} || set()

my_set = set([1, 2, 2, 4, 1]);
my_set.add(3);
my_set.remove(4);

#Union Between sets -> .union()
another_set = my_set.union([5, 8, 10]);
print(my_set);
print(another_set);

#Intersection Between Sets -> .intersection()
print(my_set.intersection(another_set));

#Difference Between Sets -> .difference()
a_set = set([1, 2, 3]);
b_set = set([1, 2, 3, 4, 5]);

print(b_set.difference(a_set));

#Update Set -> .update()
animals = set(["Monkey", "Shark", "Dinossaur"]);
more_animals = set(["Fish", "Bear", "Bat"]);

animals.update(more_animals);

print(animals);

#Check if a set is contained in another -> .issubset()
print(more_animals.issubset(animals));

#Check if a set contains another one -> .issuperset()
print(animals.issuperset(more_animals));