import random  
import os  
#####################################################################################
WIN_LIST_RPS = [('ROCK', 'SCISSORS'),('SCISSORS', 'PAPER'),('PAPER', 'ROCK')]  
####################################################################################
SELECTIONS_LIST_RPS = ['ROCK', 'PAPER', 'SCISSORS']
stats_count = {'player':0, 'computer':0, 'ties':0}
#######################################################################################
def clrscr():
  """ Clears the console in order to make a more pleasant game """
  if os.name == "posix": 
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"): 
    os.system('CLS')
#########################################################################################
def welcome():
  """ Main menu for the Game """
  clrscr()
  while True:
    option = input(
      "************** Welcome to my Rock-Paper-Scissors based Games ******************"
    "\n*******************************************************************************"
    "\n*                                OPTIONS                                      *"
    "\n*******************************************************************************"
    "\n* [1] - (Play) Rock Paper Scissors                                            *"
    "\n* [2] -  Exit                                                                 *"                   
    "\n*******************************************************************************"
    "\n Please select an option (1, 2): ")
    if option == '1':  
      lets_play(option)
    elif option == '2':  
      print("Bye bye")
      exit()
    else:  
      input("Invalid option. Try again... Please press ENTER to continue")
      clrscr()
########################################################################################    
def lets_play(option):
  """ A function that sets which game is going to be played based on the option selected """
  clrscr()
  
  if option == '1':  
    intro = (" Welcome to Rock + Paper + Scissors game!")  
    option_help = ("\n This game is simple and goes as following:"  
          "\n *You can choose between: Rock, Paper or Scissors."
          "\n\n You must take in consideration that:"
          "\n *Rock crushers Scissors."
          "\n *Scissors cut Paper."
          "\n *Paper covers Rock."
          "\n\n Notes: *The first one that scores 5 points WINS the game!"
          "\n        *If you forgot the rules, just type 'help'."
          "\n        *If you want to go to main menu to try the other games, just type 'quit'."
          "\n        *If you want to exit because you're afraid of loosing, just type 'exit' you coward!\n")
    selections_list = SELECTIONS_LIST_RPS  
    win_list = WIN_LIST_RPS 
  
      
  print(intro) 
  print(option_help) 
    
  while True:
    player_selection = input("Your Selection {}: ".format(selections_list))
    player_selection = player_selection.upper()
    
    if player_selection in selections_list:
      clrscr()
      computer_selection = random.choice(selections_list)
      
      print("Player Selection: {}".format(player_selection))
      print("Computer Selection: {}".format(computer_selection))
      
      match = player_selection, computer_selection 
      
      if player_selection == computer_selection:  
        stats_count['ties'] += 1
        print("\nResult: Both are {}! So that's a Tie!".format(player_selection))
      elif match in win_list:  
        stats_count['player'] += 1
        print("\nResult: The power of {} beats {}! You won!".format(player_selection, computer_selection))
      else:  
        stats_count['computer'] += 1
        print("\nResult: The power of {} is stronger than {}! You lost!".format(computer_selection, player_selection))
      print("-------  STATS  -------"
            "\n YOU  | COMPUTER | DRAW"
            "\n  {player}        {computer}        {ties} "
            "\n-----------------------".format(**stats_count))
      if stats_count['player'] == 5: 
        print("The game is DONE! You won! Congratulations!")
        exit()
      elif stats_count['computer'] == 5:  
        print("The game is DONE! You lost against a perfectly designed AI! You're now in the wall of shame!")
        exit()
    elif player_selection == 'HELP':  
      clrscr()
      print(option_help)
    elif player_selection == 'QUIT':  
      stats_count['player'] = 0
      stats_count['computer'] = 0
      stats_count['ties'] = 0
      input("Let's try another game mode then. I hope you enjoyed! Please press ENTER to continue...")
      clrscr()
      break
    elif player_selection == 'EXIT':  
      print("Bye bye... !")
      exit()
    else:
      print("Invalid selection. Try again...")  
############################################################################################     
welcome()
