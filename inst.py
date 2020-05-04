import os
from dotenv import load_dotenv
from instabot import Bot
import datetime
import collections


def fetch_posts_ids(bot,inst_accaunt):
    user_id = bot.get_user_id_from_username(inst_accaunt)
    posts_ids = bot.get_user_medias(user_id, filtration=False)
    return posts_ids


def fetch_comments_users_ids(bot, post, period=90):
    comments_users_ids = []
    time_delta = datetime.datetime.now() - datetime.timedelta(days=period)
    post_comments = bot.get_media_comments_all(post)
    for comment in post_comments:
        formatted_date = datetime.datetime.fromtimestamp(comment['created_at'])
        if time_delta < formatted_date:
            comments_users_ids.append(comment['user_id'])
    return comments_users_ids


def fetch_all_users_ids_in_posts(bot, posts_ids):
    users = []
    posts_users = {}
    for post_number,post in enumerate(posts_ids):
        comments_users_ids = fetch_comments_users_ids(bot, post)
        users.extend(comments_users_ids)
        posts_users[post_number] = set(comments_users_ids)
    return users, posts_users


def get_posts_rating(posts_users, users):
    posts_rating = collections.defaultdict(int)
    users = set(users)
    for post_number, post in posts_users.items():
        for user_id in post:
            if user_id in users:
                posts_rating[user_id] += 1
    return posts_rating


def run_inst():
    load_dotenv()
    inst_password = os.getenv('INSTAGRAM_PASSWORD')
    inst_login = os.getenv('INSTAGRAM_LOGIN')
    inst_accaunt = os.getenv('INSTAGRAM_ACCAUNT')

    bot = Bot()
    bot.login(username=inst_login, password=inst_password)
    posts_ids = fetch_posts_ids(bot, inst_accaunt)
    users, posts_users = fetch_all_users_ids_in_posts(bot, posts_ids)
    users_rating = collections.Counter(users)
    posts_rating = get_posts_rating(posts_users,users)
    print(f'Comments Top:{users_rating}\n\nPosts Top:{posts_rating}')


if __name__ == '__main__':
    run_inst()
