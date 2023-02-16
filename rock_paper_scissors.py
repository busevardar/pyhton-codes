import random
action_list=["rock","paper","scissors"]
computer_score=0
player_score=0
total_rounds=input("How many rounds do you want to play?Please enter a number here:")
round_counter=0
while True:
  round_counter+=1
  print("Round number:",round_counter)
  computer_choice = random.choice(action_list)
  player_choice = input("Please choose your action:")
  print("Computer:",computer_choice)
  print("Player:",player_choice)

  #tie condition
  if computer_choice == player_choice:
    print("Tie! Both players chose the same action.")  


  #Remaining conditions
  elif computer_choice == "paper":
    if player_choice == "rock":
      print("Winner is: Computer")
      computer_score+=1
    else: 
      print("Winner is: Player")
      player_score+=1
  elif computer_choice== "rock":
    if player_choice== "paper":
      print("Winner is: Player")
      player_score+=1
    else:
      print("Winner is: Computer")
      computer_score+=1
  elif computer_choice == "scissors":
    if player_choice=="paper":
      print("Winner is: Computer")
      computer_score+=1
    else:
      print("Winner is: Player")
      player_score+=1



  #Stop the while loop if the round_counter equals the number of total rounds
  if round_counter == int(total_rounds):
    break


#Print the outcome of the game by using conditional statements
if computer_score == player_score:
  print("There is no winner,tie.",computer_score,":",player_score)
elif computer_score>player_score:
  print("Computer won with score",computer_score,":",player_score) 
elif computer_score<player_score:
  print("Player won with score",computer_score,":",player_score)  
