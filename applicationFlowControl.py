from datetime import datetime

def show_menu():
    print("\n--- JENCUR6918's Spreadsheet Automation Menu ---")

    # Put single-line print menu options into a list
    menuOptions = ["1. Input data", "2. View current data", "3. Generate report", "4. Quit"]

    # Loop to go through list and print each menu option
    for item in menuOptions:
        print(item)
        
while True:
    show_menu()
    choice = input("Choose a number from the Automation Menu \n")

    selection_time = datetime.now()
    formatted_time = selection_time.strftime("%Y-%m-%d %H:%M:%S")


    if choice in ["1", "2", "3", "4"]:
        print(f"\nYou selected option {choice} at {formatted_time}")

        if choice == "4":
            break
 
    else:
        print("Error: Invalid choice selected.")
        



