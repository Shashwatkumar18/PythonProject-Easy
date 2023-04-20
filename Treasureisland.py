import sys

print("\nWelcome To Treasure Island !\nYour Mission is to Find The Treasure! ")

print("""
  _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   |
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\---/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`


""")

q1 = str(input("\nLeft or Right? "))

if q1.lower() == "right":
    print("Game Over!")
    sys.exit()
else:
    print("\nYou Entered the Game!")

q2 = str(input("\nWait or Swim? "))

if q2.lower() == "swim":
    print("\nGame Over!")
    sys.exit()
else:
    print("\nShip arrived. You Reached the island!")

q3 = str(input("\nThere is a Mansion. Which Door You Want to Enter?\n\nRED-BLUE-WHITE ??? "))

if q3.lower() == "white":
    print("\nYou Won!")
else:
    print("\nGame Over!")
    sys.exit()


print("""\n

                  _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           |'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\_||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\_/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'







""")