import requests
from colorama import Fore, Style
import os


def validate_username(username):
    url = f"https://auth.roblox.com/v1/usernames/validate?birthday=2006-09-21T07:00:00.000Z&context=Signup&username={username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['code'] == 0:
            print(f"{Fore.GREEN}The username '{username}' is valid and available{Style.RESET_ALL}")
            with open('valid.txt', 'a') as file:
                file.write(username + '\n')
        elif data['code'] == 1:
            print(f"{Fore.RED}The username '{username}' is already in use{Style.RESET_ALL}")
        elif data['code'] == 2:
            print(f"{Fore.RED}The username '{username}' is not appropriate for Roblox{Style.RESET_ALL}")
        elif data['code'] == 10:
            print(f"{Fore.YELLOW}The username '{username}' might contain private information{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Unable to access Roblox API{Style.RESET_ALL}")


def validate_usernames_from_file(filename):
    with open(filename, "r") as file:
        usernames = file.read().splitlines()
    for username in usernames:
        validate_username(username)


while True:
    print()
    os.system('cls' if os.name == 'nt' else 'clear') # clear console
    print(f"{Fore.BLUE}██   ██  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  ")
    print(f" ██ ██  ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ ")
    print(f"  ███   ██      ███████ █████   ██      █████   █████   ██████  ")
    print(f" ██ ██  ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ ")
    print(f"██   ██  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ {Style.RESET_ALL}")
    print()
    print(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Choose an option:")
    print(f"{Fore.MAGENTA}[{Fore.RESET}1{Fore.MAGENTA}]{Fore.RESET} Manually enter a username")
    print(f"{Fore.MAGENTA}[{Fore.RESET}2{Fore.MAGENTA}]{Fore.RESET} Check a list of usernames from a file")
    print(f"{Fore.MAGENTA}[{Fore.RESET}0{Fore.MAGENTA}]{Fore.RESET} Exit")
    choice = input(f"{Fore.MAGENTA}[{Fore.RESET}>{Fore.MAGENTA}]{Fore.RESET} ")
    if choice == '1':
        username = input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Enter a username: ")
        validate_username(username)
    elif choice == '2':
        filename = input(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} Enter the filename of the usernames file (must include .txt): ")
        validate_usernames_from_file(filename)
    elif choice == '0':
        break
    else:
        print(f"{Fore.RED}Invalid choice{Style.RESET_ALL}")