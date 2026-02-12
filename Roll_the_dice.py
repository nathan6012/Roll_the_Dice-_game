import random
import time
# global Vars to track progress 
rolls = 0
ai_total = 0
user_total = 0

def roll_dice():
  global rolls 
  global ai_total
  global user_total
  
  
  while True:
    user = input("""Would you like to roll the dice 
  (Y/N) press n/N to also check total scores  : """)
    print()
    print("#######################################")
    if user =="Y" or user =="y":
      print(" Have fun ")
      print("______________________________")
      ai = random.randint(1,6)
      print("AI is  rolling\n")
      time.sleep(3)
      print(f"Ai rolled : {ai}\n ")
    
      roll1 = random.randint(1,6)
      print("You are Rolling\n")
      time.sleep(3)
      print(f"You rolled: {roll1}")
      print("______________________________")
      time.sleep(2)
      print()
      if ai > roll1:
        print (" Ai won this round ")
        ai_total += 1
        
      elif ai < roll1:
        print(" You won this round  ")
        user_total += 1
      else:
        print("Drew this round ")
      print("#################################")  
      rolls += 1
      
      if rolls > 1:
        print(f" You have rolled {rolls} times")
      
    
    elif user == "N" or user =="n":
      print("Thanks for Dropping By ")
      print("Exiting")
      break
    
def check_total():
  print(f" Ai scored {ai_total} and you scored {user_total}")
  if ai_total > user_total:
    print("Ai wins")
  elif user_total > ai_total:
    print("You win ")
  else:
    print("Ended in Draw")
  
  
def main():
  global rolls
  global ai_total
  global user_total
  
  print("Roll the Deice Game".upper())
  print()
  roll_dice()
  check_total()
   
if __name__ =="__main__":
  main()
  