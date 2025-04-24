# Create a program that asks user for a question, then ask for 4 possible answer and the correct answer.
# Write the collected data to a text file.
# Ask another question until the user chose to exit.

# (Optional) Install library/libraries that you'll use in the program.

# Import dependencies
from colorama import init, Fore, Style, Back
import os

# Initialize colorama
init(autoreset=True)

# Custom prompt format
def user_input(prompt, color=Fore.YELLOW):
    return input(color + prompt + Fore.RESET)

# Quiz creator menu banner
def menu_banner():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 50)
    print("|" + " " * 48)
    print(Fore.YELLOW + Style.BRIGHT + "🧠 Welcome to the Quiz Creator ! 🧠")
    print(f"\nPress {Fore.GREEN}{Style.BRIGHT}1{Fore.RESET}to {Fore.GREEN}{Style.BRIGHT}CONTINUE{Fore.RESET}")
    print(f"Press {Fore.RED}{Style.BRIGHT}2{Fore.RESET}to {Fore.RED}{Style.BRIGHT}CONTINUE{Fore.RESET}")
    print("|" + " " * 48)
    print("=" * 50)

def quiz_creator():
    menu_banner()

if __name__ == "__main__":
    quiz_creator()