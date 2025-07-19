import praw
import pandas as pd
import json
import logging


# --- Logging Configuration ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RedditConnector:
    def __init__(self, client_id, client_secret, user_agent, username=None, password=None):
        self.reddit_obj = praw.Reddit(client_id=client_id,
                                       client_secret=client_secret,
                                       user_agent=user_agent,
                                       username=username,
                                       password=password)

    def get_subreddit_posts(self, subreddit_name, limit=100, comments_limit=100):
        subreddit_data = []
        try:
            subreddit = self.reddit_obj.subreddit(subreddit_name)
            for submission in subreddit.top(limit=limit):
                if submission.selftext.strip():
                    # Fetch top-level comments (replace MoreComments with actual comments)
                    submission.comments.replace_more(limit=0)
                    comments = [
                        comment.body
                        for comment in submission.comments.list()[:comments_limit]
                        if hasattr(comment, "body") and "[deleted]" not in comment.body and "[removed]" not in comment.body
                    ]
                    subreddit_data.append({
                        "subreddit": subreddit_name,
                        "title": submission.title,
                        "score": submission.score,
                        "id": submission.id,
                        "url": submission.url,
                        "comms_num": submission.num_comments,
                        "created": submission.created_utc,
                        "body": submission.selftext,
                        "comments": comments  # <-- Add comments here
                    })
        except Exception as e:
            logger.error(f"Error fetching data for r/{subreddit_name}: {e}")
        return subreddit_data