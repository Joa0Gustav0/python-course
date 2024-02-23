#Number Guessing Game
import random;

def breakLine() :
  print("+----------------------------+");
def getUserGuessNumber(player_lives) :
  return int(
    input("(" + str(player_lives) + "❤ " + ") " + "Guess the misterious number:")
  );
def exitGame(guess_number, misterious_number) :
  if guess_number != misterious_number :
    print("Hahaha! Pay with blood and soul! 😈");
    print("The misterious number was: " + str(misterious_number));
  else :
    print("Wow! You got the misterious number (" + str(misterious_number) + ").");
  
  print("Game Finished. 🎲");
  input();
def runGame() :
  player_lives = 3;
  misterious_number = random.randint(0, 10);  

  print("Welcome to the Number Guessing Game! 😈🎲");
  breakLine();

  guess_number = getUserGuessNumber(player_lives);

  while guess_number != misterious_number and player_lives > 0 :
    print("Wrong answer! Lose one life! 😈💔")
    player_lives -= 1;

    breakLine();

    if player_lives > 0 : guess_number = getUserGuessNumber(player_lives);
  
  exitGame(guess_number, misterious_number);

runGame();