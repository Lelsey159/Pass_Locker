#!/usr/bin/env python3.6
from accounts import Accounts
from password import Password


def create_account(first_name, last_name, user_name, password):
    accounts = Accounts(first_name, last_name, user_name, password)
    return accounts


def save_account(accounts):
    accounts.save_account()


def delete_account(accounts):
    accounts.delete_account()


def find_accounts(user_name):
    return Accounts.find_by_user_name(user_name)


def isexist_accounts(user_name):
    return Accounts.account_exists(user_name)


def display_accounts():
    return Accounts.display_accounts()


def create_page(page, password):
    passwords = Password(page, password)
    return passwords


def save_page(passwords):
    passwords.save_page()


def find_page(pager):
    return Password.find_by_page(pager)


def isexist_page(pager):
    return Password.page_exists(pager)


def delete_page(passwords):
    passwords.delete_page()


def display_pages():
    return Password.display_page()


def main():
    print('WELCOME TO PASSWORD LOCKER')
    print('Use the following numbers to pick their corresponding values')
    while True:

        print(" 1) LOGIN \n 2) SIGN UP \n 3) ABOUT PASSWORD LOCKER \n 4) DISPLAY ACCOUNTS \n 5) SIGN OUT")

        choice = int(input())
        if choice == 1:
            print('Enter username')
            username = input()
            print('Enter password')
            password = input()
            account = find_accounts(username)
            if account.user_name == username and account.password == password:

                print('logged in ')
                while True:

                    print(
                        f'Welcome {username}, Use the following numbers to select their corresponding          values')

                    print(
                        ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) Log out ')

                    log_choice = int(input())
                    if log_choice == 1:
                        print('New page')
                        print('*'*100)

                        print('Page name')
                        page = input()

                        print('password')
                        password = input()

                    # created and saved page
                        save_page(create_page(page, password))

                    elif log_choice == 2:
                        print("Enter the name of the page you want to delete")

                        page = input()
                        if isexist_page(page):
                            remove_page = (page)
                            delete_page(remove_page)

                        else:
                            print(f'I cant find {page}')

                    elif log_choice == 3:
                        if display_pages():
                            for pag in display_pages():
                                print(
                                    f'{pag.page}:{pag.password}'
                                )
                        else:
                            print('NO PASSWORD SAVED YET')
                            print('\n')

                    elif log_choice == 4:
                        print('adios')
                        break
            else:
                print('wrong credentials')

        if choice == 2:
            print('NEW ACCOUNT')
            print('*'*100)

            print('FIRSTNAME')
            first_name = input()

            print('LASTNAME')
            last_name = input()

            print('USERNAME')
            user_name = input()

            print('PASSWORD')
            password = input()

            save_account(create_account(
                first_name, last_name, user_name, password))
            # create and save a new account
            print('ACCOUNT CREATED')
            while True:

                print(
                    f'Welcome {user_name}, Use the following numbers to select their corresponding values')
                print(
                    ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) Log out ')

                log_choice = int(input())
                if log_choice == 1:
                    print('New page')
                    print('*'*100)

                    print('Page name')
                    page = input()

                    print('password')
                    password = input()

                    # created and saved page
                    save_page(create_page(page, password))

                elif log_choice == 2:
                    print("Enter the name of the page you want to delete")

                    page = input()
                    if isexist_page(page):
                        remove_page = (page)
                        delete_page(remove_page)

                    else:
                        print(f'I cant find {page}')

                elif log_choice == 3:
                    if display_pages():
                        for pag in display_pages():
                            print(
                                f'{pag.page}:{pag.password}'
                            )
                    else:
                        print('NO PASSWORD SAVED YET')

                elif log_choice == 4:
                    break

        elif choice == 3:
            print('ABOUT PASSWORD LOCKER')
            print(
                '''
            Password locker is an sort of script application that allows you to store  password from different ccounts. In case of many accounts on social media passlock can be used to store the different password from the social media  accounts.Instead of having to use one password for all your sites so that you can remember  easily,you can use different password and store them in password locker and only have to remember your password locker password. This can prove to be very helpful especially  against hackers.
                                    ''')

        elif choice == 4:
            if display_accounts():
                for account in display_accounts():
                    print(
                        f'{account.user_name}'
                    )
            else:
                print('NO ACCOUNTS')

        elif choice == 5:
            print('adios')
            break


if __name__ == '__main__':
    main()