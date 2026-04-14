import requests

def get_weather(city_name, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        response.raise_for_status() 
        
        data = response.json()
        
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        
        return {
            'description': description,
            'temperature': temperature
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    except KeyError:
        print("City not found. Please check the municipality name.")
        return None


def main():
    API_KEY = ""
    
    city = input("Enter the name of a municipality: ")
    
    weather = get_weather(city, API_KEY)
    
    if weather:
        print(f"\nWeather in {city}:")
        print(f"Condition: {weather['description'].capitalize()}")
        print(f"Temperature: {weather['temperature']:.1f}°C")


if __name__ == "__main__":
    main()