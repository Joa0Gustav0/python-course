#Line Break -> \n
print("Ouch...\nThe line broke.");


#Quotation Mark inside string -> \"
print("Quotation mark on the right\"Quotation mark on the left.");


#Uppercase, Lowercase and Capitalize -> upper() && lower() && capitalize()
#For verify if its upper || lower -> islower() || isupper()
big_name = "This is a big name.";
small_name = "THIS IS A SMALL NAME.";

print(big_name.upper(), small_name.lower().capitalize());


target_text = "Hello, world";
#Get string length -> len(string)
print("\"" + target_text + "\"", "contains", len(target_text), "chars.");

#Get the index of a char in a string -> index() || find()
target_substring = "rld";
print(
  "The index of", 
  "\"" + target_substring + "\"", 
  "in", "\"" + target_text + "\"", 
  "is", target_text.index(target_substring), ".");

#Replace string content -> .replace(old_Value, new_value)
error_name = "Slada";

print(error_name, "was shuffled.", "Unshuffled, it means:", error_name.replace("lada", "alad") + " 🥗.");

#Remove the white-space from a string -> .strip()
white_space_string = "   Hey, darling!  ";
white_space_string = white_space_string.strip();
print(white_space_string);


greeting = "Hello World!";
#Check if some string starts with a specific string value -> .startswith()
print(greeting.startswith("Hello"));

#Check if some string ends with a specific string value -> .endswith()
print(greeting.endswith("World!"));

print(greeting.find("llo"));

#Turn a list into a string value -> .join()
splited_string = ["Life", "is", "a", "waterfall..."];
my_string = "".join(word + " " for word in splited_string);
print(my_string);

#Ways of Formating Values For a String -> % || format() || f""""string...{value}...string"""
variable = 1.67 * 4.985;
print("The result is: %s" % variable);
print("The result is: {}".format(variable));
print(f"The result is: {variable}");