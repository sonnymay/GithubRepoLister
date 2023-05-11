import requests
import json

def get_github_repos(user):
    """
    Get a list of repositories for a specific GitHub user.
    """
    url = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Error: API request failed with status code {response.status_code}")

    return response.json()

def main():
    user = input("Enter the GitHub username: ")
    repos = get_github_repos(user)
    
    print(f"Repositories for {user}:")
    for repo in repos:
        print(f"Name: {repo['name']}, URL: {repo['html_url']}")

if __name__ == "__main__":
    main()
