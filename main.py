import os
import requests
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = "Rizwan102003"  # change this to your username

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def list_repositories():
    url = f"https://api.github.com/users/{USERNAME}/repos"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        repos = response.json()
        print(f"\n📦 Public Repositories of {USERNAME}:\n")
        for repo in repos:
            print(f"- {repo['name']}: {repo['html_url']}")
    else:
        print("❌ Failed to fetch repositories.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

if __name__ == "__main__":
    list_repositories()
