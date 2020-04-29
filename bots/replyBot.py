import tweepy
import logging
from config import create_api
import time
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def checkJoeDTweet(api, since_id, replyList):
    logger.info("Checking JoeD tweets")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.user_timeline, id="Joe_DeFlorio", since_id=since_id, count=1).items():
        new_since_id = max(tweet.id, new_since_id)

        if ('RT @' not in tweet.text):
            logger.info(f"Replying to tweet")
            reply = random.choice(replyList)
            api.update_status(status=reply, in_reply_to_status_id=tweet.id)

    return new_since_id

def main():
    api = create_api()
    tweet = api.user_timeline(id="Joe_DeFlorio", count=1)

    since_id = tweet[0].id

    replies = ["@Joe_DeFlorio He dont miss", "@Joe_DeFlorio Fire", "@Joe_DeFlorio Facts", "@Joe_DeFlorio LMAOOOOO", "@Joe_DeFlorio 🔥🔥🔥🔥🔥🔥🔥🔥", "@Joe_DeFlorio 😂😂😂😂😂"]

    while True:
        since_id = checkJoeDTweet(api, since_id, replies)
        logger.info("Waiting...")
        time.sleep(10)

if __name__ == "__main__":
    main()
