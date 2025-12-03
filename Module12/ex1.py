import requests

url = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()

    print("Here's a random Chuck Norris joke for you:")
    print(data['value'])

except requests.exceptions.Timeout:
    print("The request timed out. Try again later.")

except requests.exceptions.HTTPError as e:
    print("HTTP error occurred:", e)

except requests.exceptions.RequestException as e:
    print("Something went wrong:", e)
