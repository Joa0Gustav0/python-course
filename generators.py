def getAvailablePasswordRequests(requests) :
  while True :
    requests -= 1;
    yield requests;
password_requests = getAvailablePasswordRequests(5);

password = "gustavo223829967hakjndsa";
def tryPasswordRequest() :
  available_requests = next(password_requests);
  print("");

  if available_requests > 0 :
    print("Your password is: {}".format(password));
    print("⚠ You have, now, {} available password requests.".format(available_requests));
  else :
    print("⚠ You reached the password requests limit.")
  print("-----------------------------\n")



while True :
  input("Press \"Enter\" for request your password: ");
  tryPasswordRequest()

