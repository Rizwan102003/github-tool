# GitHub API Integration Tool

This is a simple command-line tool that integrates with the GitHub API to fetch and list all public repositories of a given GitHub user.

It uses:
- Python
- Personal Access Token (PAT)
- GitHub REST API (v3)

##  Features

- Authenticate with GitHub using a token
- Fetch and display all public repositories of a user

##  Requirements

- Python 3.6+
- GitHub Personal Access Token (PAT)

##  Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Rizwan102003/github-tool.git
   cd github-tool
   ```

2. Create a virtual environment (optional but recommended):
 ```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. Install dependencies:
 ```bash
pip install -r requirements.txt
```

4. Create a .env file and add your GitHub token:

```bash
GITHUB_TOKEN=your_personal_access_token_here
```

5. Update the USERNAME variable in main.py with your GitHub username.

6. Usage
Run the script:
```bash
python main.py
