"""
import logging
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('prawcore')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
"""
import logging
import pandas as pd
import json
from llm.llm import LLM
from reddit_connector.reddit_connector import RedditConnector

# --- Logging Configuration ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ThreadSense:
    def __init__(self, secrets_file="access/secrets.json", llm_model="llama3", llm_base_url="http://localhost:11434"):
        self.llm = LLM(model_name=llm_model, llm_base_url=llm_base_url)
        self.reddit_connector = None
        self.secrets = self.get_user_credentials(secrets_file)
        self.initialize_reddit_connector()

    def get_user_credentials(self, secrets_file='access/secrets.json'):
        """Load user credentials from a JSON file."""
        if not secrets_file:
            raise ValueError("Secrets file path must be provided.")
        try:
            with open(secrets_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Secrets file '{secrets_file}' not found.")

    def initialize_reddit_connector(self):
        try:
            if not self.secrets:
                raise ValueError("User credentials are not loaded.")
        except ValueError as e:
            logger.error(e)
            return
        if not self.reddit_connector:
            logger.info("Initializing Reddit Connector with provided credentials.")
        else:
            logger.info("Reddit Connector already initialized.")
        # Initialize Reddit Connector with the loaded credentials
        try:
            self.reddit_connector = RedditConnector(
                client_id=self.secrets["client_id"],
                client_secret=self.secrets["client_secret"],
                user_agent=self.secrets["user_agent"],
                username=self.secrets.get("username"),
                password=self.secrets.get("password")
            )
        except KeyError as e:
            logger.error(f"Missing key in secrets: {e}")

    def fetch_posts_from_subreddits(self, subreddits_list: list, limit=100):
        if not self.reddit_connector:
            raise ValueError("Reddit connector is not initialized.")
        if not subreddits_list:
            raise ValueError("Subreddits list cannot be empty.")
        all_posts = []
        for subreddit_name in subreddits_list:
            logger.info(f"Fetching data for subreddit: {subreddit_name} with limit: {limit}")
            posts = self.reddit_connector.get_subreddit_posts(subreddit_name, limit)
            all_posts.extend(posts)
        return all_posts

    def save_posts_to_csv(self, posts, filename="subreddit_posts.csv"):
        if not posts:
            logger.warning("No posts to save.")
            return
        df = pd.DataFrame(posts)
        df.to_csv(filename, index=False)
        logger.info(f"Posts saved to {filename}")






