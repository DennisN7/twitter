from config.config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

import tweepy
import json
import os

def fetch_tweets(username, output_dir='output'):
    # Authenticate to the API
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Fetch tweets
    tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended").items():
        tweets.append({
            "created_at": tweet.created_at,
            "text": tweet.full_text
        })

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save tweets to a JSON file
    output_file = os.path.join(output_dir, f"{username}_tweets.json")
    with open(output_file, "w") as file:
        json.dump(tweets, file, indent=4, default=str)

    print(f"Saved {len(tweets)} tweets from @{username} to {output_file}")

if __name__ == "__main__":
    fetch_tweets("kabetes")

