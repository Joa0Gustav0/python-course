import json
target_test_file = open("./json-test.json", "w");

#Turn a Python data into a JSON data -> json.dumps()
class Person :
  def __init__(self, name, age, email, hobbies) :
    target_test_file.write(
      json.dumps(
        {"name": name, "age": age, "email": email, "hobbies": hobbies}, indent=2)
      );

Person("Robert", 89, "hey_its_robert@gmail.com", ["Drink Wine", "Write Books"]);

#Turn a JSON data into a Python Data -> json.load()
target_test_file.close();
target_test_file = open("./json-test.json", "r");

converted_json_data = json.load(target_test_file);
print(converted_json_data["hobbies"]);