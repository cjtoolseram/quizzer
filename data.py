from urllib import response
import requests

parameters = {
    "amount": 50,
    "type": "boolean",
    "difficulty": "hard"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

data = response.json()

question_data = data["results"]