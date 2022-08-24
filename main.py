import requests.exceptions

from account import Account
from combos import Combos


if __name__ == '__main__':
    # credentials = input('Insert username and password: ')
    # credentials = credentials.split(':', 1)

    combos_path = input('Insert path to combo list file: ')
    post_id = input('Insert the id of the post you would like to vote: ')

    combos = Combos()
    combos.parse_combos(combos_path)

    if combos.combo_list:
        for combo in combos.combo_list:
            attempt = 1

            while attempt <= 3:
                credentials = combo.split(':', 1)

                account = Account(credentials[0], credentials[1])

                try:
                    login_res = account.login()

                    if login_res == 1:
                        vote_res = account.vote(post_id)

                        if vote_res == 1:
                            combos.update_success()

                            break

                        elif vote_res == 0:
                            combos.update_failed()
                            break

                except requests.exceptions.ProxyError:
                    attempt += 1

                except requests.exceptions.ReadTimeout:
                    attempt += 1