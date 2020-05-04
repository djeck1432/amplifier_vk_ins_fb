import os
from dotenv import load_dotenv
import datetime
import requests


def fetch_posts_ids(fb_token, group_id):
    url = f'https://graph.facebook.com/v6.0/{group_id}/feed'
    params = {'access_token': fb_token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    posts_ids = [post['id'] for post in response.json()['data']]
    return posts_ids


def fetch_posts_comments(fb_token, post_id):
    params = {'access_token': fb_token}
    response = requests.get(f'https://graph.facebook.com/v5.0/{post_id}/comments', params=params)
    response.raise_for_status()
    comments = response.json()['data']
    post_comments = [{'user_id': comment['from']['id'],
                      'created_time': comment['created_time'],
                      'message': comment['message']} for comment in comments
                     ]
    return post_comments


def fetch_comments_period(comments, period=30):
    last_comments = []
    for comment in comments:
        date,time = comment['created_time'].split('T')
        comment_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        now = datetime.datetime.now()
        timedelta = now - comment_date
        if timedelta.days <= period:
            last_comments.append(comment['user_id'])
    return last_comments


def fetch_post_reactions(fb_token, post_id):
    params = {'access_token': fb_token}
    response = requests.get(f'https://graph.facebook.com/v5.0/{post_id}/reactions', params=params)
    response.raise_for_status()
    reactions = response.json()['data']
    post_reactions = [{'user_id': reaction['id'],'type': reaction['type']} for reaction in reactions]
    return post_reactions


def fetch_post_details(fb_token, posts_ids):
    users_ids = []
    users_likes = []
    for post_id in posts_ids:
        post_comments = fetch_posts_comments(fb_token, post_id)
        comments_period = fetch_comments_period(post_comments)
        post_reactions = fetch_post_reactions(fb_token, post_id)
        if comments_period is not None:
            users_ids.append(comments_period)
        if post_reactions is not None:
            users_likes.append(post_reactions)
    return users_ids,users_likes


def run_fb():
    load_dotenv()
    fb_token = os.getenv('FACEBOOK_TOKEN')
    fb_group_id = os.getenv('FACEBOOK_GROUP_ID')
    posts_ids = fetch_posts_ids(fb_token, fb_group_id)
    users_ids, users_likes = fetch_post_details(fb_token, posts_ids)
    print(f'{users_ids}\n{users_likes}')


if __name__ == '__main__':
    run_fb()
