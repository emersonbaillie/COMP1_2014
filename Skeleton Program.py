# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014


import random
import datetime


NO_OF_RECENT_SCORES = 10

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = ""

Deck = [None]
RecentScores = [None]
Choice = ''



def GetRank(RankNo):
  Rank = ''
  if RankNo == 1:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  elif RankNo == 14:
    Rank = "Ace"
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print("5. Options")
  print("6. Save high scores")
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  print()
  Choice = Choice.lower()
  return Choice

def LoadDeck(Deck,AceOption):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    if Deck[Count].Rank == 1 and AceOption == True: #Task 6
      Deck[Count].Rank = 14
    Count = Count + 1
 

def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():
  ValidName = False
  while not ValidName:
    print()
    PlayerName = input('Please enter your name (No numbers or symbols): ')
    print()
    ValidName = PlayerName.isalpha()
    if ValidName == False:
      print()
      print("This is not a valid name")
      print()
  return PlayerName

def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter Y or N)? ')
  Choice = Choice[0]
  return Choice.lower()

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].Date = ""

def DisplayRecentScores(RecentScores):
  BubbleSortScores(RecentScores)
  print()
  print('Recent Scores: ')
  print()
  print("{0:<15}{1:<15}{2}".format("Name","Score","Date"))
  print()
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print("{0:<15}{1:<15}{2}".format(RecentScores[Count].Name,RecentScores[Count].Score,RecentScores[Count].Date))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score, Date):
  SaveScore = input("Do you wish to save your score? (Y/N):")
  SaveScore = SaveScore[0].upper()
  if SaveScore == "Y":
    PlayerName = GetPlayerName()
    print("Score Saved")
    FoundSpace = False
    Count = 1
    while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
      if RecentScores[Count].Name == '':
        FoundSpace = True
      else:
        Count = Count + 1
    if not FoundSpace:
      for Count in range(1, NO_OF_RECENT_SCORES):
        RecentScores[Count].Name = RecentScores[Count + 1].Name
        RecentScores[Count].Score = RecentScores[Count + 1].Score
        RecentScores[Count].Date = RecentScores[Count + 1].Date
      Count = NO_OF_RECENT_SCORES
    RecentScores[Count].Name = PlayerName
    RecentScores[Count].Score = Score
    RecentScores[Count].Date = Date
  elif SaveScore == "N":
    print()
    print("Score not saved")
  else:
    print()
    print("This is not a valid input")
    print()
    UpdateRecentScores(RecentScores, Score, Date)

def TestScores(RecentScores):
  Score = 1

  for Count in range(1,NO_OF_RECENT_SCORES+1):
    Score = random.randint(0,51)
    RecentScores[Count].Name = "{0}".format("Test")
    RecentScores[Count].Score = Score
    RecentScores[Count].Date = "{0}".format("Test")

def SaveScores(RecentScores):
  with open("save_scores.txt",mode="w",encoding="utf-8")as my_file:
    for Count in range(1,NO_OF_RECENT_SCORES+1):
      Name = RecentScores[Count].Name
      Score = ("{0}".format(RecentScores[Count].Score))
      Date = RecentScores[Count].Date
      my_file.write(Name+("\n"))
      my_file.write(Score+("\n"))
      my_file.write(Date+("\n"))
    print()
    print("Scores Saved")
      
def LoadScores():
  with open("save_scores.txt",mode="r",encoding="utf-8")as my_file:
    for Count in range(1,NO_OF_RECENT_SCORES+1):
      Name = my_file.readline()
      Score = my_file.readline()
      Date = my_file.readline()
      Name = Name.rstrip("\n")
      Score = Score.rstrip("\n")
      Score = int(Score)
      Date = Date.rstrip("\n")
      RecentScores[Count].Name = Name
      RecentScores[Count].Score = Score
      RecentScores[Count].Date = Date


def PlayGame(Deck, RecentScores, SameCard):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  PointsLost = 0
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)  
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - (1+PointsLost))
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    elif (not Higher and SameCard == False) and (LastCard.Rank == NextCard.Rank):
      print()
      print("Cards match, no points awarded")
      print()
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
      PointsLost = PointsLost + 1 
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - (2+PointsLost))
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - (2+PointsLost), Date)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51, Date)

def SaveCurrentGame(Deck, LastCard, NextCard, Score, NoOfCardsTurnedOver):
  with open("deck.txt",mode"w",encoding"utf-8")as deck_file:
    Rank = ThisCard.Rank = Deck[1].Rank
    Suit = ThisCard.Suit = Deck[1].Suit
    deck_file.write(Rank+("\n"))
    deck_file.write(Suit+("\n"))
    for Count in range(1, 52 - NoOfCardsTurnedOver):
      Deck[Count].Rank = Deck[Count + 1].Rank
      Deck[Count].Suit = Deck[Count + 1].Suit
      deck_file.write(Rank+("\n"))
      deck_file.write(Suit+("\n"))
##    deck_file.write(LastCard.Rank+("\n"))              NEEDS TO BE IN A .DAT FILE
##    deck_file.write(NextCard.Rank+("\n"))
##    deck_file.write(Score+("\n"))
##    deck_file.write(NoOfCardsTurnedOver+("\n"))
      
def Date():
  Day = datetime.datetime.now().strftime("%d")
  Month = datetime.datetime.now().strftime("%m")
  Year = datetime.datetime.now().strftime("%y")
  Date = ("{0}-{1}-{2}".format(Day,Month,Year))
  return Date

  
def DisplayOptionMenu():
  print("OPTION MENU")
  print()
  print("1. Set Ace to be HIGH or LOW")
  print("2. Card of same sort ends game")
  print()


def GetOptionMenuChoice():
  OptionChoice = int(input("Select an option from the menu (Enter 'q' to quit): "))
  return OptionChoice

def SetAce():
  print()
  AceOption = input("Do you wish the Ace to be (h)igh or (l)ow: ")
  AceOption = AceOption[0].lower()
  if AceOption == "h":
    AceOption = True
  elif AceOption == "l":
    AceOption = False
  return AceOption

def SetSameScore():
  SameCard = input("Do you wish two cards having the same face to end the game? (y/n): ")
  SameCard = SameCard = SameCard[0].lower()
  if SameCard == "y":
    SameCard = True
  elif SameCard == "n":
    SameCard = False
  return SameCard
  
def BubbleSortScores(RecentScores):
  sorted = False
  while not sorted:
    sorted = True
    for count in range(1,NO_OF_RECENT_SCORES):
      if RecentScores[count].Score < RecentScores[count + 1].Score:
        sorted = False
        Temp = RecentScores[count + 1]
        RecentScores[count + 1] = RecentScores[count]
        RecentScores[count] = Temp


if __name__ == '__main__':
  Date = Date()
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  try:
    LoadScores()
  except IOError:
    print()
    print("save_scores.txt not found. New file being created.")
    print()
    SaveScores(RecentScores)
  Choice = ''
  AceOption = False
  SameCard = False
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck,AceOption)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores, SameCard)
    elif Choice == '2':
      LoadDeck(Deck,AceOption)
      PlayGame(Deck, RecentScores, SameCard)
    elif Choice == '3':
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == "5":
      DisplayOptionMenu()
      OptionChoice = GetOptionMenuChoice()
      if OptionChoice == 1:
        AceOption = SetAce()
      elif OptionChoice == 2:
        SetSameScore()
    elif Choice == "6":
      SaveScores(RecentScores)
    elif Choice == "20":
      TestScores(RecentScores)
