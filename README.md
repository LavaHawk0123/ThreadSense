# ThreadSense

ThreadSense is a Python project that leverages Large Language Models (LLMs) and the Reddit API to help users discover relevant subreddits and fetch top posts based on their queries. It demonstrates integration of LLMs (such as Llama 3 via Ollama) with Reddit data, and provides a modular, extensible codebase for building Reddit-powered applications.

---

## Features

- **LLM-powered subreddit discovery:** Uses a local LLM (via Ollama) to suggest relevant subreddits for any user prompt.
- **Reddit API integration:** Fetches top posts from suggested subreddits using PRAW.
- **Prompt engineering:** Easily customize LLM prompts for different use cases.
- **CSV export:** Saves fetched posts to a CSV file for further analysis.
- **Modular design:** Clean separation of LLM, Reddit, and application logic.

---

## Project Structure

```
ThreadSense/
├── app.py
├── llm/
│   ├── llm.py
│   └── prompts/
│       └── list_of_subreddits.txt
├── reddit_connector/
│   ├── reddit_connector.py
│   └── __init_.py
├── threadsense_lib/
│   ├── threadsense.py
│   └── __init__.py
├── access/
│   ├── secrets_template.json
│   └── secrets.json (ignored by git)
├── requirements.txt
├── .gitignore
├── README.md
└── subreddit_posts.csv (output)
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ThreadSense.git
cd ThreadSense
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up Reddit API credentials

- Copy `access/secrets_template.json` to `access/secrets.json`.
- Fill in your Reddit API credentials in `secrets.json`:
  - `client_id`, `client_secret`, `user_agent`, `username`, `password`

### 4. Set up Ollama and Llama 3

- [Install Ollama](https://ollama.com/download) for your OS.
- Pull the Llama 3 model:
  ```bash
  ollama pull llama3
  ```
- Start Ollama (if not already running):
  ```bash
  ollama serve
  ```

### 5. Run the application

```bash
python app.py
```

- Enter your question when prompted (e.g., "I want to learn Python").
- The app will suggest relevant subreddits, fetch top posts, and save them to `subreddit_posts.csv`.

---

## Customization

- **LLM Prompts:** Edit `llm/prompts/list_of_subreddits.txt` to change how the LLM suggests subreddits.
- **Reddit Fetching:** Modify `reddit_connector/reddit_connector.py` to change how posts are fetched (e.g., use `hot`, `new`, etc.).
- **Output:** Change the output CSV filename in `app.py` or `threadsense_lib/threadsense.py`.

---

## Requirements

- Python 3.7+
- [Ollama](https://ollama.com/) (for local LLM inference)
- Reddit API credentials (create an app at https://www.reddit.com/prefs/apps)
- See `requirements.txt` for Python dependencies:
  - `praw`
  - `requests`
  - `pandas`

---

## Security

- **Never commit your `access/secrets.json`!**  
  This file is in `.gitignore` by default. Only share `secrets_template.json`.

---

## License

This project is licensed under the MIT License.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

---

## Acknowledgements

- [Ollama](https://ollama.com/) for local LLM serving
- [PRAW](https://praw.readthedocs.io/) for