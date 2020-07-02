# -*- coding: utf-8 -*-
import vk_api


def main():
    login = input('Логин ')
    password = input('Пароль ')
    login, password = login, password
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    response = vk.users.get()
    my_id = response[0]['id']
    posts = vk.wall.get(count=100)
    for post in posts['items']:
        vk.wall.delete(post_id=post['id'])
    print(posts)

if __name__ == '__main__':
    main()