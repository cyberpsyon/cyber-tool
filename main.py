import requests
import sys
import pyfiglet
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner(title):
    print(pyfiglet.figlet_format(title, "slant"))

def red_team_menu():
    clear_screen()
    show_banner("Red Team Menu")
    menu = """
    [1] Subdomain Enumeration
    [2] Directory Enumeration
    [3] Network Scanner
    [4] Port Scanner
    [5] Hash Cracker
    [6] SSH Brute Force
    [7] Web Login Form Brute Force
    [8] SQL Injection Exploit
    [9] Back to Main Menu
    [10] Exit
    """
    print(menu)
    red_choice = input("Enter your choice: ")
def blue_team_menu():
    clear_screen()
    show_banner("Blue Team Menu")
    menu = """
    [1] Hash Identifier
    [2] Password Strength Checker
    [3] Base64 Encoder/Decoder
    [4] Port Scanner
    [5] Log Parser
    [6] File Integrity Checker
    [7] Email Header Analyzer
    [8] JWT Inspector
    [9] Back to Main Menu
    [10] Exit
    """
    print(menu)
    blue_choice = input("Enter your choice: ")
def main():
    clear_screen()
    show_banner("RBDuoSec")
    print("[1] Red Team Tools\n[2] Blue Team Tools\n[3] Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        red_team_menu()
    elif choice == "2":
        blue_team_menu()
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()




