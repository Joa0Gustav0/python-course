#Counter -> returns a dictionary where "keys" reffer to the element, and "values" reffer to the element countage
from collections import Counter, namedtuple

crazy_word = "aaaaaaaaeeeeeeeeiiiiiioooo!!!";
crazy_word_countage = Counter(crazy_word);

for elements_keys, countage in crazy_word_countage.items() :
  print("The char {} was used {} times.".format(elements_keys, countage));

#->Most Appearing Element In Counter -> .most_commum(number_of_wished_elements)
print(crazy_word_countage.most_common(1)[0][0]);

#Named Tuple
new_user = namedtuple("User", "username, password");
my_user = new_user("Gustavo", 2409);
print(my_user.username);