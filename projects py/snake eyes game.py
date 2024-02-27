

#UNFINISHED!!!!!!!!!!!!





















import math, random, time, replit

print("Welcome to GAME \n")
p1banked = 0
p1run = 0
p2banked = 0
p2run = 0

def player2():
  global p2banked
  print("test worked")
def test():
  global p1banked
  global p1run
  print("\nPlayer One is gambling!")
  die1player1 = random.randint(1, 6)
  die2player1 = random.randint(1, 6)
  print(f"Values of both are: {die1player1}, {die2player1}")
  p1run += die1player1 + die2player1
  print(f"Running total is : {p1run}")

def player1():
    global p1banked
    global p1run
    global answer
    print("\nPlayer One is rolling two die")
    die1player1 = random.randint(1, 6)
    die2player1 = random.randint(1, 6)
    print(f"Values of both are: {die1player1}, {die2player1}")
    p1run = die1player1 + die2player1
    print(f"Running total: {p1run}")


    if die1player1 == 1 and die2player1 == 1:
      print("You rolled a double 1, your banked total is 0")
      p1banked = 0
      p1run = 0
      answer = 0
      player2()
      return
    elif die1player1 == 1 or die2player1 == 1:
      print("You rolled a 1, your running total is 0")
      p1run = 0
      answer = 0
      player2()
      return

    else:
      answer = input("Do you want to bank or gamble? (bank/gamble): ")
      if answer == "bank":
        print("You have banked your points")
        p1banked += p1run
        p1run = 0
        print(f"Your banked points are: {p1banked}")
        return
      elif answer == "gamble":
        test()


    return p1run
player1()
if answer == "bank":
  print(f"bank test correct! {p1banked}")
elif answer == "gamble":
  print("gambe test correct!")
else:
  print("")


def player2():
  global p2banked
