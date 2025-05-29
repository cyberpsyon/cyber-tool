import requests
import sys
import pyfiglet
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

def display_menu():
    menu = """
    [1] Subdomain Enumeration
    [2] Directory Enumeration
    [3] Network Scanner
    [4] Port Scanner
    [5] Hash Cracker
    [6] SSH Brute Force
    [7] Web Login Form Brute Force
    [8] SQL Injection Exploit
    [9] Exit
    """
    print(menu)

def main():
    print(pyfiglet.figlet_format("Cyber Tool", "slant"))
    display_menu()
    choice = int(input("Enter your choice: "))

if __name__ == "__main__":
    main()




