import random, time

print("Welcome to the Snake Eyes Game!")

def dice():
  return random.randint(1,6), random.randint(1,6)

def main():
  playerScore = [0,0]
  currentPlayer = 0
  runningTotal = 0
  line = '-' * 38

  while max(playerScore) < 100:
    print(line)
    print(f"\n Player Scores: P1 - |{playerScore[0]}|   P2 - |{playerScore[1]}|\n")

    print(f"Player {currentPlayer + 1}'s turn")
    
    dice1, dice2 = dice()
    total = dice1 + dice2
    
    print(f"Roll: {dice1},{dice2} , total is {total}")
    print(f"Running total is {runningTotal}")
    if dice1 == dice2 == 1:
      playerScore[currentPlayer] = 0
      total = 0
      runningTotal = 0
      currentPlayer = 1 - currentPlayer
      print(f"Uh oh! A Double 1! . Banked and running totals reset to 0")
      time.sleep(3.5)
    elif dice1 == 1 or dice2 == 1:
      runningTotal = 0
      currentPlayer = 1 - currentPlayer
      print("You rolled a 1! Running total reset to 0")
      time.sleep(3)
    else:
      choice = input("\nDo you want to gamble (g) or bank (b)? ").lower()
      if choice == 'g':
        runningTotal = total + runningTotal
      elif choice == 'b':
        runningTotal += total
        playerScore[currentPlayer] += runningTotal
        runningTotal = 0
        currentPlayer = 1 - currentPlayer
      else:
        print("Wrong choice buddy, re-enter option please!")
  print(f"Player {playerScore.index(max(playerScore)) + 1} wins!")

if __name__ == "__main__":
  main()

#if using REPLIT IDE then import replit, and add replit.clear() at 31-32 , 36-37 and 38-39
