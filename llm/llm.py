import requests

# Ollama ssh privatekey : ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIAFAPjJGsBeldNZtvfGoQOL6SJMbpOKxiZojsRwAa+w

class LLM:
    def __init__(self, model_name="llama3", llm_base_url="http://localhost:11434"):
        self.prompts = {
            "list_of_subreddits" : "llm/prompts/list_of_subreddits.txt"
        }
        self.model = model_name
        self.base_url = llm_base_url

    def read_prompt_file(self, prompt_id):
        if prompt_id not in self.prompts.keys():
            raise ValueError(f"Prompt ID '{prompt_id}' not found.")
        with open(self.prompts[prompt_id], 'r') as file:
            return file.read().strip()

    def get_llm_response(self, user_prompt, context=None):
        url = f"{self.base_url}/api/chat"
        messages = []
        if context:
            messages.append({"role": "system", "content": context})
        messages.append({"role": "user", "content": user_prompt})
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["message"]["content"].strip()

if __name__ == "__main__":
    # Example usage
    # Ensure the LLM can read prompts
    llm_obj = LLM()
    user_prompt = "Give me 3 subreddits that can help me code in python"
    prompt = llm_obj.read_prompt_file("list_of_subreddits")
    print(f"Prompt: {prompt}")
    print(llm_obj.get_llm_response(prompt + user_prompt))