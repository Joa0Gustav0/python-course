def getAgeClassification(age) :
  if (age < 12) :
    return "child";
  elif (age >= 12 and age < 18) :
    return "teenager";
  elif (age >= 18 and age < 60) :
    return "adult";
  else :
    return "elder";

person_age = int(input("Whats is your age? "));
print("You are", person_age, "years old.");
print("Then, you are a", getAgeClassification(person_age) + ".");