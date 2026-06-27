print("********* Welcome to the treasure island *********")
print("Your mission is to find the treasure called !! Onepiece !!")
print(r'''
                        _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')# Developed by: Pankaj Pawar
print('You are standing at a crossroads in a mysterious jungle.\nYou are a player and made choice "left" or "right"to go inside  the jungle \nAnd find the treasure ....')
print('''     Standing at the fork
        """
               [Left]     [Right]
                 \\          /
                  \\        /
                   \\  o   /
                    \\/|\\ /
                     / \\
        """,''')
choice = input("Enter your choice 'left' or 'right' : ").strip().capitalize()
if choice=="Right":
    print("****** Your choice result is ******\nYou fall into a deep hole ")
    print(r'''
           Walking down the right path
        
               [Left]     [Right]
                 \\          /
                  \\    o   /
                   \\  /|\\ /
                    \\ / \\
                     
    
            Approaching the edge
        
                          [Right]
                            /
                           o 
                          /|\\  ____
                          / \\ /    \\
                             |      |
        
             Slipping over the edge
        
                          [Right]
                            /
                             
                            ~o~ ____
                          / /  /    \\
                             |      |
        
             Falling into the hole
        
                          [Right]
                            /
                               ____
                              / o  \\
                             | /|\\  |
                               / \\
        
             Deep in the hole
        
                          [Right]
                            /
                               ____
                              /    \\
                             |  o   |
                               /|\\
        
             Gone!
        
                          [Right]
                            /
                               ____
                              /    \\
                             |      |
                             
                             *SPLASH*
                  ''')
    game_over = r"""
          _______   _______  _______  _______ 
         |  _____| |  ___  ||       ||  _____|
         | |  ___  | |___| || |\_/| || |____  
         | | |_  | |  ___  || |   | ||  ____| 
         | |___| | | |   | || |   | || |_____ 
         |_______| |_|   |_||_|   |_||_______|
         
                _.-'''''''-._
              .'  ________   '.
             /   / -+====+- \   \
            |   |    __  __  |   |
            |   |   |  ||  | |   |
             \   \   \ || / /   /
              '.  '.  `||` .'  .'
                '-._'-.__.-'_.-'
                    |  ||  |
                    |__||__|
                    
          _______  ___  ___  _______  _______ 
         |  ___  ||   \ /   ||  _____||  ___  |
         | |   | ||         || |____  | |___| |
         | |   | || |\   /| ||  ____| |  __  _/
         | |___| || | \_/ | || |_____ | |  \ \ 
         |_______||_|     |_||_______||_|   \_\
"""

    print(game_over)

# Now if the player chooses left 

elif choice == "Left":
    print("***** Result of your choice is *******\n**** Now you are at the LARGE MYSTIC LAKE ")

    print(r'''
                 /\                 /\
                /  \               /  \
               /    \             /    \
              /      \           /      \

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~                                 ~~~~~~~~~
~~~~~~~        LARGE MYSTIC LAKE        ~~~~~~~~~
~~~~~~~                                 ~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            __/___
      _____/______|
      \              \
~~~~~~~\______________\~~~~~~~~~~~~~~~~~~~~~~~~~~

      WAIT for a boat or SWIM across?
''')# Developed by: Pankaj Pawar
    
    choice_1=input("**** Now you have to go acrooss the lake ***** \n You have two options 'Swim' or 'Wait for a boat' ").strip().capitalize()
    if choice_1 == "Swim":
        print("***** Here is the result of your choice *****")
        print(r'''


        YOU ARE ATTACKED BY A
            GIANT SNAKE!

                /^\/^\
              _|__|  O|
     \/     /~     \_/ \
      \____|__________/  \
             \_______      \
                     `\     \                 \
                       |     |                  \
                      /      /                    \
                     /     /                       \\
                   /      /                         \ \
                  /     /                            \  \
                /     /             _----_            \   \
               /     /           _-~      ~-_         |   |
              (      (        _-~            ~-_     _/   |
               \      ~-____-~                  ~-_-~    /
                 ~-_                           _-~     _/
                    ~--______-----------______--~

             


         ''')
        game_over = r"""
          _______   _______  _______  _______ 
         |  _____| |  ___  ||       ||  _____|
         | |  ___  | |___| || |\_/| || |____  
         | | |_  | |  ___  || |   | ||  ____| 
         | |___| | | |   | || |   | || |_____ 
         |_______| |_|   |_||_|   |_||_______|
         
                _.-'''''''-._
              .'  ________   '.
             /   / -+====+- \   \
            |   |    __  __  |   |
            |   |   |  ||  | |   |
             \   \   \ || / /   /
              '.  '.  `||` .'  .'
                '-._'-.__.-'_.-'
                    |  ||  |
                    |__||__|
                    
          _______  ___  ___  _______  _______ 
         |  ___  ||   \ /   ||  _____||  ___  |
         | |   | ||         || |____  | |___| |
         | |   | || |\   /| ||  ____| |  __  _/
         | |___| || | \_/ | || |_____ | |  \ \ 
         |_______||_|     |_||_______||_|   \_\
         """
# Developed by: Pankaj Pawar
        print(game_over)
    elif choice_1 == "Wait for boat":
        print("**** this is the result of your choice ")
        print(r'''
    
    

                     __/___
               _____/______|
       _______/_____\_______\____
       \                        /
    ~~~~\_____ _____ ____ ___ ___/~~~~

              A SMALL BOAT
          SAFELY TAKES YOU TO

        
                          /\
                         /  \
                        /    \
                       /      \
                      /  /\    \
                     /  /  \    \
                    /__/____\____\

                    TREASURE ISLAND

         You arrive safely at the island!
         ''')
        
        choice_2=input("#### Now you are on the treasure island #### \n there is three doors \nRed door\nBlue door\nYellow door\nYou have to choose one \nEnter your choosen door color : \n***** This is the result of your choice *****\nEnter the door you want to go : ").strip().capitalize()

        if choice_2 == "Red door":
            print(r'''
####################################################

                RED DOOR OPENED

                      ||
                    __||__
                   /      \
                  /  FIRE  \
                 /__________\

                     (  )
                    (    )
                   (      )
                  (  /\    )
                 (  /  \    )
                (  / /\ \    )
               (__/ /  \ \____)

              🔥🔥🔥🔥🔥🔥🔥🔥🔥
            🔥 THE ROOM IS FILLED 🔥
                 WITH FIRE!
            🔥🔥🔥🔥🔥🔥🔥🔥🔥

                 GAME OVER


                 ''')
        elif choice_2 == "Blue door":
             print(r'''


                  BLUE DOOR

                     ______
                    | BLUE |
                    |______|
                        ||

                 GRRRRRRRRR!!!

              /\___/\
             (  o o  )
             /   ^   \
            /|       |\
             |  ___  |

          /\___/\    /\___/\
         ( >   < )  ( >   < )
          \  ^  /    \  ^  /
           |||||      |||||

         A PACK OF WILD BEASTS
            JUMPS OUT!

              GAME OVER

     
              ''')
        elif choice_2 == "Yellow door":
            print(r'''


               YOU CHOSE YELLOW

                    ________
                   |        |
                   | YELLOW |
                   |  DOOR  |
                   |________|
                        ||

                The door opens...


                  ''')
            print("Treasure Chest Full of Gold")
            print(r'''


                  ___________
                 /__________/|
                |          | |
                | TREASURE | |
                |__________|/
                 \$$$$$$$$/
                  \$$$$$$/
                   \$$$$/
                    \$$/

              GOLD AND JEWELS!


                 ''')
            print(r'''
####################################################
        # Developed by: Pankaj Pawar
   __   __            _    _ _       _
   \ \ / /           | |  | (_)     | |
    \ V /___  _   _  | |  | |_ _ __ | |
     \ // _ \| | | | | |/\| | | '_ \| |
     | | (_) | |_| | \  /\  / | | | |_|
     \_/\___/ \__,_|  \/  \/|_|_| |_(_)

         CONGRATULATIONS!

        YOU FOUND THE TREASURE!

               YOU WIN!

####################################################
                  
''')
            
        
    