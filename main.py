from account import Account


if __name__ == '__main__':
    credentials = input('Insert username and password: ')
    credentials = credentials.split(':', 1)

    account = Account(credentials[0], credentials[1])

    login_success = account.login()
    print(login_success)

    if login_success == 1:
        account.vote('t3_wtd8ag', 'https://www.reddit.com/r/ModernWarfareII/comments/wtd8ag/am_i_the_only_one_who_dont_like_symmetrical_3/')
