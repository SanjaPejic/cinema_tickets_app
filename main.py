from ui.menus import display_auth_menu, display_user_menu

if __name__ == '__main__':
    logged_user = display_auth_menu()
    print(f"\nWelcome, {logged_user.name} {logged_user.surname}!")
    display_user_menu(logged_user)
