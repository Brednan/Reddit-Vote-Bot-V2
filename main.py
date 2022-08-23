from account import Account


if __name__ == '__main__':
    credentials = input('Insert username and password: ')
    credentials = credentials.split(':', 1)

    account = Account(credentials[0], credentials[1])

    login_success = account.login()

    if login_success == 1:
        account.vote('t3_wvj33u')
