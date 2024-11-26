# shadowops/cli.py

import sys
from shadowops.manager import setup_shadowops, uninstall_shadowops

def display_menu():
    print("\nShadowOps Setup Menu:")
    print("1. Install ShadowOps")
    print("2. Uninstall ShadowOps")
    print("3. Exit")

def handle_choice(choice):
    if choice == '1':
        setup_shadowops()
    elif choice == '2':
        uninstall_shadowops()
    elif choice == '3':
        print("Exiting ShadowOps Setup.")
        sys.exit(0)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

def main():
    if len(sys.argv) > 1:
        # Handle command-line arguments
        arg = sys.argv[1].lower()
        if arg in ['install', 'i']:
            setup_shadowops()
        elif arg in ['uninstall', 'u']:
            uninstall_shadowops()
        else:
            print("Invalid argument. Use 'install' or 'uninstall'.")
    else:
        # Interactive Menu
        while True:
            display_menu()
            choice = input("Enter your choice: ").strip()
            handle_choice(choice)

