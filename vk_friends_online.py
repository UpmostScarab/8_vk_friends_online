import vk
import getpass


APP_ID =  '5218358'  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return input('Логин: ')


def get_user_password():
    return getpass.getpass('Пароль: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    return api.friends.get(fields=['online'])
    # например, api.friends.get()


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print('%s %s' % (friend['first_name'],friend['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
