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
from threadsense_lib.threadsense import ThreadSense

# --- Logging Configuration ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = ThreadSense(secrets_file="access/secrets.json", llm_model="llama3", llm_base_url="http://localhost:11434")
llm_obj = LLM(model_name="llama3", llm_base_url="http://localhost:11434")

user_prompt = input("Enter your question for the LLM: ")
try:
    prompt = llm_obj.read_prompt_file("list_of_subreddits")
    context = "You are an expert on Reddit communities. Only respond with subreddit names."
    subreddits_to_fetch = [s.strip() for s in llm_obj.get_llm_response(prompt + user_prompt, context=context).split(",")]
    logger.info(f"LLM Response: {subreddits_to_fetch}")
except Exception as e:
    logger.error(f"Error fetching subreddits list: {e}")

posts = app.fetch_posts_from_subreddits(subreddits_to_fetch, limit=10)
if posts:
    app.save_posts_to_csv(posts, filename="subreddit_posts.csv")
    logger.info("Posts fetched and saved successfully.")
else:
    logger.warning("No posts were fetched.")


def example_usage():
    # Example usage
    subreddits_to_fetch = ["python", "AskReddit", "LifeProTips"]  # Replace with your list
    posts = app.fetch_posts_from_subreddits(subreddits_to_fetch, limit=10)
    
    if posts:
        app.save_posts_to_csv(posts, filename="subreddit_posts.csv")
        logger.info("Posts fetched and saved successfully.")
    else:
        logger.warning("No posts were fetched.")

#if __name__ == "__main__":
#    example_usage()

