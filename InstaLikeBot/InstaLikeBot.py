"""
This template is written by @timgrossmann
What does this quickstart script aim to do?
- This script is automatically executed every 6h on my server via cron
"""

import random
import config
from instapy import InstaPy
from instapy import smart_run

# login credentials
# insta-username = ''
# insta-password = ''

dont_likes = ['sex', 'nude', 'naked', 'beef', 'pork', 'seafood',
              'egg', 'chicken', 'cheese', 'sausage', 'lobster',
              'fisch', 'schwein', 'lamm', 'rind', 'kuh', 'meeresfrüchte',
              'schaf', 'ziege', 'hummer', 'yoghurt', 'joghurt', 'dairy',
              'meal', 'food', 'eat', 'pancake', 'cake', 'dessert',
              'protein', 'essen', 'mahl', 'breakfast', 'lunch',
              'dinner', 'turkey', 'truthahn', 'plate', 'bacon',
              'sushi', 'burger', 'salmon', 'shrimp', 'steak',
              'schnitzel', 'goat', 'oxtail', 'mayo', 'fur', 'leather',
              'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy',
              'breakfast', 'dinner', 'lunch']

friends = ['list of friends I do not want to interact with']

like_tag_list = ['food','italy','girl','ragazza','Messina','Sicilia','spottedmessina','messina','ragazzaitaliana',
				 'paesaggio','single','love','amicizie','atm','cairoli','Vialegiostra','ragazzasingle','webdevelopment']

# prevent posts that contain some plantbased meat from being skipped
ignore_list = ['vegan', 'veggie', 'plantbased']

accounts = ['accounts with similar content']

# get a session!
session = InstaPy(username=config.Iusername,
                  password=config.Ipassword,
                  headless_browser=True)

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=False,
                                    max_followers=15000)

    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=False, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    # activity
    session.like_by_tags(random.sample(like_tag_list, 3),
                         amount=random.randint(50, 100), interact=True)


