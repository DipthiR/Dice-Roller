import random
import time
import os
from colorama import init, Fore, Back, Style

# Initialize colorama for Windows support
init(autoreset=True)

# Dice face designs in ASCII Art
dice_art = {
    1: ("+-------+",
        "|       |",
        "|   ●   |",
        "|       |",
        "+-------+"),
    2: ("+-------+",
        "| ●     |",
        "|       |",
        "|     ● |",
        "+-------+"),
    3: ("+-------+",
        "| ●     |",
        "|   ●   |",
        "|     ● |",
        "+-------+"),
    4: ("+-------+",
        "| ●   ● |",
        "|       |",
        "| ●   ● |",
        "+-------+"),
    5: ("+-------+",
        "| ●   ● |",
        "|   ●   |",
        "| ●   ● |",
        "+-------+"),
    6: ("+-------+",
        "| ●   ● |",
        "| ●   ● |",
        "| ●   ● |",
        "+-------+")
}

# Clear terminal screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Function to simulate dice rolling animation
def rolling_animation():
    for _ in range(5):
        value = random.randint(1, 6)
        clear()
        print(Fore.GREEN + Style.BRIGHT + "Rolling the dice...")
        print(Fore.CYAN + "Let’s see what you got...\n")
        for line in dice_art[value]:
            print(Fore.YELLOW + line)
        time.sleep(0.3)

# Function to print the final result after rolling
def roll_dice():
    value = random.randint(1, 6)
    clear()
    print(Fore.YELLOW + Style.BRIGHT + f"\n🎲 You rolled a {value}! 🎉\n")
    for line in dice_art[value]:
        print(Fore.MAGENTA + line)
    print()

# Welcome message with stylish borders
def welcome():
    clear()
    print(Fore.RED + Style.BRIGHT + """
╔══════════════════════════════╗
║      🎲 DICE ROLLER GAME     ║
╚══════════════════════════════╝
""")
    print(Fore.GREEN + "Welcome to the exciting Dice Roller Game!")
    time.sleep(1)

# Customized goodbye message
def goodbye():
    print(Fore.CYAN + Style.BRIGHT + "\nThank you for playing! 🎉 Come back soon!\n")
    time.sleep(1)
    print(Fore.MAGENTA + "Remember, fortune favors the bold... Good luck next time! ✨")

# Main function to run the dice game
def main():
    welcome()
    while True:
        try:
            input(Fore.WHITE + "Press Enter to roll the dice (or Ctrl+C to quit)...")
            rolling_animation()  # Show rolling animation
            roll_dice()  # Show final rolled dice face
        except KeyboardInterrupt:
            goodbye()
            break

if __name__ == "__main__":
    main()
