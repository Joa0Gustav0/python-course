""" print("Let's sum.");
number_one = input("Input the first number: ");
number_two = input("Input the second number: ");

result_sum = int(number_one) + int(number_two);
print(
  "The sum between",
  number_one, "and", number_two,
  "is", str(result_sum)
); """

print("\n--------------------------");
#Test Time ⚔

print("👋 Let's create your ID card.");
print("For this, we need some informations:");
input("Press \"Enter\" for continue.");
person_name = input("What's is your name? ");
person_age = input("What's your age? ");
person_gender = input("What's your gender? ");
person_pronouns = input("What are your pronouns? ");
person_hobby = input("Share a hobby: ");
input("Ready to see your new ID?\nPress \"Enter\" for continue!");

print("\n*------------------------*");
print("ID Card");
print("Name:", person_name);
print("Age:", person_age);
print("Pronouns:", person_gender);
print("Gender:", person_pronouns);
print("Hobby:", person_hobby);
print("*------------------------*");
