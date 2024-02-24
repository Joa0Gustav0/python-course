import random;

class TTTGame :
  players = {
    "1": "O",
    "2": "X"
  }
  player_in_game = players.get(str(random.randint(1, 2)));

  dashboard = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
  ]

  def __init__(self) :
    print("Welcome to the Tic-Tac-Toe Game!");
    self.setNewRound();
  

  def showDashboard(self) :
    print("+------------------------------+");
    for row in self.dashboard :
      print(row);
    print("+------------------------------+");

  def changePlayerInGame(self) :
    if self.player_in_game == "O":
      self.player_in_game = "X";
    else :
      self.player_in_game = "O";

  def setNewRound(self) :
    self.showDashboard();
    self.createPlayRequestStatement();


  def createPlayRequestStatement(self) :
    print("The turn is with \"" + self.player_in_game + "\".");
    target_cell = self.requestPlay();

    while target_cell == None :
      target_cell = self.requestPlay();

    self.executeThePlay(target_cell);
  
  def requestPlay(self) :
    return self.validatePlay(input("Select an available number for mark with an \"" + self.player_in_game + "\": "));
  

  def validatePlay(self, play) :
    if self.indexInDashboard(play) == None or self.indexIsAlreadyOccuped(play) == None :
      print("\n⚠ This play is invalid. Try another.");
      print("+------------------------------+");
      return None;
  
    return play;

  def indexInDashboard(self, play) :
    for row in self.dashboard :
      if play in row : return True;

  def indexIsAlreadyOccuped(self, play) :
    if int(play) <= 3 :
      return self.queryIndexInSingleRow(play, 0);
    elif int(play) > 3 and int(play) <= 6 :
      return self.queryIndexInSingleRow(play, 1);
    else :
      return self.queryIndexInSingleRow(play, 2);

  def queryIndexInSingleRow(self, play, row) :
    if play in self.dashboard[row] : return True;
    return None;

  def executeThePlay(self, target_cell) :
    for row in range(len(self.dashboard)) :
      self.targetDashboardCellInRowByMapping(target_cell, row);
    
    self.changePlayerInGame();
    self.setNewRound();

  def targetDashboardCellInRowByMapping(self, target_cell, row) :
    for column_cell in range(len(self.dashboard[row])) :
      if self.dashboard[row][column_cell] == target_cell : self.dashboard[row][column_cell] = self.player_in_game;

TTTGame();
