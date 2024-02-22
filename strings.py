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

#Get the index of a char in a string -> index()
target_substring = "rld";
print(
  "The index of", 
  "\"" + target_substring + "\"", 
  "in", "\"" + target_text + "\"", 
  "is", target_text.index(target_substring), ".");

#Replace string content -> .replace(old_Value, new_value)
error_name = "Slada";

print(error_name, "was shuffled.", "Unshuffled, it means:", error_name.replace("lada", "alad") + " 🥗.");