import requests.exceptions
import threading
from account import Account
from combos import Combos


def account_sequence(credentials):
    attempt = 1

    credentials = credentials.split(':', 1)

    while attempt <= 3:
        account = Account(credentials[0], credentials[1])

        try:
            login_res = account.login()

            if login_res == 1:
                vote_res = account.vote(post_id, vote_option)

                if vote_res == 1:
                    combos.update_success()
                    break

                elif vote_res == 0:
                    combos.update_failed()
                    break

            else:
                combos.update_failed()
                break

        except requests.exceptions.ProxyError:
            attempt += 1

        except requests.exceptions.ReadTimeout:
            attempt += 1

        except requests.exceptions.SSLError:
            attempt += 1

        except requests.exceptions.ConnectionError:
            attempt += 1


if __name__ == '__main__':
    c = 0

    combos_path = input('Insert path to combo list file: ')
    post_id = input('Insert the id of the post you would like to vote: ')
    vote_option = int(input('Specify the vote option: '))

    combos = Combos()
    combos.parse_combos(combos_path)

    if combos.combo_list:
        while c < len(combos.combo_list):
            if threading.active_count() < 15:
                threading.Thread(target=account_sequence, args=(combos.combo_list[c],)).start()

                c += 1
