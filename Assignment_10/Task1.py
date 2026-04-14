import requests

def fetch_chuck_norris_joke():
    """Fetch and print a random Chuck Norris joke from the API."""
    try:
        response = requests.get('https://api.chucknorris.io/jokes/random')
        response.raise_for_status()
        
        joke_data = response.json()
        joke = joke_data['value']
        
        print(joke)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")