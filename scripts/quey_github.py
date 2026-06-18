import os
import requests
from datetime import datetime

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
USERNAME = os.environ.get("GITHUB_USER")

if not USERNAME:
    USERNAME = requests.get(
        "https://api.github.com/user",
        headers={"Authorization": f"Bearer {GITHUB_TOKEN}"}
    ).json()["login"]

query = """
query($login:String!) {
  user(login:$login) {
    contributionsCollection {
      contributionCalendar {
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}"
}

response = requests.post(
    "https://api.github.com/graphql",
    json={"query": query, "variables": {"login": USERNAME}},
    headers=headers
)

data = response.json()

weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]

days = []
for week in weeks:
    for d in week["contributionDays"]:
        days.append({
            "date": d["date"],
            "count": d["contributionCount"]
        })

# last 7 days only
days = days[-7:]

print(days)
