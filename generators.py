def getUserInOrder() :
  users_list = ["Robert", "Paulo", "Jeremmy"];

  for user in users_list :
    yield user;

user = getUserInOrder()
while user:
  print(f"The current user is: {next(user)}");
 
  input("Press \"Enter\" for getting the next user.")

