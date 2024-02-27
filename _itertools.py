from itertools import product, permutations
#product returns a list containing all the possibilities of combinations between lists
t_shirts = ["green-t-shirt", "red-t-shirt", "blue-t-shirt"];
trousers = ["purple-trouser", "black-trouser", "yellow-trouser"];

print(f"The maximum number of combinations is: {len(list(product(t_shirts, trousers)))}");

#permutations
print(f"The number of permutations is: {len(list(permutations(t_shirts)))}");