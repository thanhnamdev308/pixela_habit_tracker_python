"""
Define menu and functionality of the program
"""

import pixela_api_handler as pixela
import json
from os import system
from requests import Response


# __________Utility functions__________

def print_response(response: Response) -> None:
    """
    Print response in pretty JSON format
    """

    try:
        print(json.dumps(response.json(), indent=2, default=str))
    except json.decoder.JSONDecodeError:
        print(response.text)


def draw_header() -> None:
    clear_screen()
    header = f"""Pixela Habit Tracker

Your username: {pixela.get_username()}
Your API token: {pixela.get_token()}

See your profile at: https://pixe.la/@{pixela.get_username()}
__________"""
    print(header)


def clear_screen() -> None:
    """
    Clear console
    """

    system("clear")


# __________Draw menu functions__________

def draw_main_menu() -> None:
    """
    Draw the main menu
    """

    draw_header()
    menu_text = f"""
MAIN MENU
What do you want to do?

1. Go to USER menu
2. Go to USER PROFILE menu
3. Go to GRAPH menu
4. Go to PIXEL menu
5. Log in another account
6. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-6): ")
        if user_input in ("1", "2", "3", "4", "5", "6"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            draw_user_menu()
        case 2:
            draw_userprofile_menu()
        case 3:
            draw_graph_menu()
        case 4:
            draw_pixel_menu()
        case 5:
            log_in()
        case 6:
            clear_screen()
            quit()


def draw_user_menu() -> None:
    """
    Draw the USER menu
    """

    draw_header()
    menu_text = f"""
USER menu
What do you want to do?

1. Create an account
2. Update API token
3. Delete your account
4. Go back
5. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-5): ")
        if user_input in ("1", "2", "3", "4", "5"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            create_account()
        case 2:
            update_api_token()
        case 3:
            delete_account()
        case 4:
            draw_main_menu()
        case 5:
            clear_screen()
            quit()


def draw_userprofile_menu() -> None:
    """
    Draw the USER PROFILE menu
    """

    draw_header()
    menu_text = f"""
USER PROFILE menu
What do you want to do?

1. View a user profile
2. Update your profile
3. Go back
4. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-4): ")
        if user_input in ("1", "2", "3", "4"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    # TODO: implement USER PROFILE menu choices
    match choice:
        case 1:
            view_user_profile()
        case 2:
            update_user_profile()
        case 3:
            draw_main_menu()
        case 4:
            clear_screen()
            quit()


def draw_graph_menu() -> None:
    """
    Draw the GRAPH menu
    """

    draw_header()
    menu_text = f"""
GRAPH menu
What do you want to do?

1. Create a graph
2. List all of your graphs
3. Get your graph information
4. Delete a graph
5. Get a graph HTML
6. Show all pixel of a graph
7. Show a graph statistics
8. Go back
9. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-5): ")
        if user_input in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    # TODO: implement GRAPH menu choices
    match choice:
        case 1:
            create_graph()
        case 2:
            get_all_graph()
        case 3:
            get_graph_def()
        case 4:
            delete_graph()
        case 5:
            display_graph()
        case 6:
            get_graph_pixels()
        case 7:
            get_graph_stats()
        case 8:
            draw_main_menu()
        case 9:
            clear_screen()
            quit()


def draw_pixel_menu() -> None:
    """
    Draw the PIXEL menu
    """

    draw_header()
    menu_text = f"""
PIXEL menu
What do you want to do?

1. Post a pixel
2. Get a pixel statistics
3. Update a pixel statistics
4. Delete a pixel
5. Go back
6. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-6): ")
        if user_input in ("1", "2", "3", "4", "5", "6"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            post_pixel()
        case 2:
            get_pixel()
        case 3:
            update_pixel()
        case 4:
            delete_pixel()
        case 5:
            draw_main_menu()
        case 6:
            clear_screen()
            quit()


# __________Functionality__________

def log_in() -> None:
    """
    This function let user log in
    with username and token
    """

    clear_screen()
    print("Welcome to my Pixela user interface!")
    print("About Pixela, visit: https://pixe.la/")

    username = input("""
Input your username:
(If you are new, just choose your username)\n""")
    pixela.set_username(username)

    while True:
        token = input("""
Input your API token:
(The token must be a string of all kind of characters
that is between 8 and 128 characters in length.)\n""")
        token_length = len(token)
        if 8 <= token_length <= 128:
            break
        else:
            print("Token has invalid length!")
    pixela.set_token(token)


def create_account() -> None:
    """
    Call function in pixela_api_handler.py
    to create an account
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Create an account with current username
2. Log in for another username and API token
3. Go back
4. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-4): ")
        if user_input in ("1", "2", "3", "4"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            response = pixela.create_user()
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            create_account()
        case 2:
            log_in()
            create_account()
        case 3:
            draw_user_menu()
        case 4:
            clear_screen()
            quit()


def update_api_token() -> None:
    """
    Call function in pixela_api_handler.py
    to update api token
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Update API token of current username
2. Log in for another username and API token
3. Go back
4. Exit

    """
    print(menu_text)
    while True:
        user_input = input("Your choice (1-4): ")
        if user_input in ("1", "2", "3", "4"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            new_token = input("\nInput your new token: ")
            response = pixela.update_token(new_token)
            if response.status_code == 200:
                print("\nSUCCESS")
                pixela.set_token(new_token)
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            update_api_token()
        case 2:
            log_in()
            create_account()
        case 3:
            draw_user_menu()
        case 4:
            clear_screen()
            quit()


def delete_account() -> None:
    """
    Call function in pixela_api_handler.py
    to delete this user account
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Delete current account
2. Go back
3. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            response = pixela.delete_user()
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            delete_account()
        case 2:
            draw_user_menu()
        case 3:
            clear_screen()
            quit()


def view_user_profile() -> None:
    """
    Call function in pixela_api_handler.py
    to get view a user profile
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. View a user profile (get link)
2. Go back
3. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            user_profile = input("Input name of the user profile: ")
            response = pixela.view_user_profile(user_profile)
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            view_user_profile()
        case 2:
            draw_userprofile_menu()
        case 3:
            clear_screen()
            quit()


def update_user_profile() -> None:
    """
    Call function in pixela_api_handler.py
    to update user profile
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Update your profile
2. Go back
3. Exit

"""

    choose_mode_text = f"""
What do you want to update?

1. Display name
2. Gravatar icon email
3. Tile
4. Timezone
5. About URL
6. Pinned graph ID

"""

    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            print(choose_mode_text)
            while True:
                user_choice = input("Your choice (1-6): ")
                if user_choice in ("1", "2", "3", "4", "5", "6"):
                    break
                else:
                    print("Invalid choice, choose again.")

            mode_num = int(user_choice)
            mode = ""
            match mode_num:
                case 1:
                    mode = "displayName"
                case 2:
                    mode = "gravatarIconEmail"
                case 3:
                    mode = "title"
                case 4:
                    mode = "timezone"
                case 5:
                    mode = "aboutURL"
                case 6:
                    mode = "pinnedGraphID"

            new_value = input("Input new value: ")
            response = pixela.update_user_profile(mode, new_value)
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            update_user_profile()
        case 2:
            draw_userprofile_menu()
        case 3:
            clear_screen()
            quit()


def create_graph() -> None:
    """
    Call function in pixela_api_handler.py
    to create a graph
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Create a graph
2. Go back
3. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            graph_id = input("Input your graph ID: ")
            graph_name = input("Input your graph name: ")
            graph_unit = input("Input your graph unit (hour, km,...): ")
            graph_type = input("Choose your graph data type (input \"int\" or \"float\"): ")
            graph_color = input(
                "Choose your graph color (input shibafu (green), momiji (red),\nsora (blue), ichou (yellow), "
                "ajisai (purple) or kuro (black)): ")
            response = pixela.create_graph(graph_id, graph_name, graph_unit, graph_type, graph_color)
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            create_graph()
        case 2:
            draw_graph_menu()
        case 3:
            clear_screen()
            quit()


def get_all_graph() -> None:
    """
    Call function in pixela_api_handler.py
    to get all user's graphs' definition
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. List all of your graphs
2. Go back
3. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            response = pixela.get_all_graph()
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            get_all_graph()
        case 2:
            draw_graph_menu()
        case 3:
            clear_screen()
            quit()


def get_graph_def() -> None:
    """
    Call function in pixela_api_handler.py
    to get a specific graph's definition
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Get your graph information
2. Go back
3. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            graph_id = input("Input your graph id: ")
            response = pixela.get_graph_def(graph_id)
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            get_graph_def()
        case 2:
            draw_graph_menu()
        case 3:
            clear_screen()
            quit()


def delete_graph() -> None:
    """
    Call function in pixela_api_handler.py
    to delete a graph
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Delete graph
2. Go back
3. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            graph_id = input("Input your graph id: ")
            response = pixela.delete_graph(graph_id)
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            delete_graph()
        case 2:
            draw_graph_menu()
        case 3:
            clear_screen()
            quit()


def display_graph() -> None:
    """
    Call function in pixela_api_handler.py
    to get a graph's HTML
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Get a graph HTML
2. Go back
3. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            graph_id = input("Input your graph id: ")
            response = pixela.display_graph(graph_id)
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            display_graph()
        case 2:
            draw_graph_menu()
        case 3:
            clear_screen()
            quit()


def get_graph_pixels() -> None:
    """
    Call function in pixela_api_handler.py
    to get all of a graph's pixels
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Get all of your graph's pixels
2. Go back
3. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            graph_id = input("Input your graph id: ")
            response = pixela.get_graph_pixels(graph_id)
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            get_graph_pixels()
        case 2:
            draw_graph_menu()
        case 3:
            clear_screen()
            quit()


def get_graph_stats() -> None:
    """
    Call function in pixela_api_handler.py
    to get a graph's statistics
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Get your graph's statistics
2. Go back
3. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            graph_id = input("Input your graph id: ")
            response = pixela.get_graph_stats(graph_id)
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            get_graph_stats()
        case 2:
            draw_graph_menu()
        case 3:
            clear_screen()
            quit()


def post_pixel() -> None:
    """
    Call function in pixela_api_handler.py
    to post a pixel to a graph
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Post a pixel to a graph
2. Go back
3. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            graph_id = input("Input your graph id: ")
            date = input("Input date (follow the format yyyyMMdd): ")
            quantity = input("Input the quantity: ")
            response = pixela.post_pixel(graph_id, date, quantity)
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            post_pixel()
        case 2:
            draw_pixel_menu()
        case 3:
            clear_screen()
            quit()


def get_pixel() -> None:
    """
    Call function in pixela_api_handler.py
    to get a pixel info of a graph
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Get a pixel information
2. Go back
3. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            graph_id = input("Input your graph id: ")
            date = input("Input date (follow the format yyyyMMdd): ")
            response = pixela.get_pixel(graph_id, date)
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            get_pixel()
        case 2:
            draw_pixel_menu()
        case 3:
            clear_screen()
            quit()


def update_pixel() -> None:
    """
    Call function in pixela_api_handler.py
    to update a pixel's quantity
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Update a pixel's quantity
2. Go back
3. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            graph_id = input("Input your graph id: ")
            date = input("Input date (follow the format yyyyMMdd): ")
            quantity = input("Input the new quantity: ")
            response = pixela.update_pixel(graph_id, date, quantity)
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            update_pixel()
        case 2:
            draw_pixel_menu()
        case 3:
            clear_screen()
            quit()


def delete_pixel() -> None:
    """
    Call function in pixela_api_handler.py
    to delete a pixel
    """

    draw_header()
    menu_text = f"""
What do you want to do?

1. Delete a pixel
2. Go back
3. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-3): ")
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            clear_screen()
            graph_id = input("Input your graph id: ")
            date = input("Input date (follow the format yyyyMMdd): ")
            response = pixela.delete_pixel(graph_id, date)
            if response.status_code == 200:
                print("\nSUCCESS")
            else:
                print("\nFAILED")

            print_response(response)
            input("\nPress Enter to continue…")
            delete_pixel()
        case 2:
            draw_pixel_menu()
        case 3:
            clear_screen()
            quit()


def not_available_feature(menu: str) -> None:
    """
    Call this function for unfinished features
    """

    draw_header()
    menu_text = f"""
Sorry, this feature is currently not available

1. Go back
2. Exit

"""
    print(menu_text)
    while True:
        user_input = input("Your choice (1-2): ")
        if user_input in ("1", "2"):
            break
        else:
            print("Invalid choice, choose again.")

    choice = int(user_input)
    match choice:
        case 1:
            if menu == "USER":
                draw_user_menu()
            elif menu == "USER PROFILE":
                draw_userprofile_menu()
            elif menu == "GRAPH":
                draw_graph_menu()
            elif menu == "PIXEL":
                draw_pixel_menu()
            else:
                draw_main_menu()
        case 2:
            clear_screen()
            quit()
