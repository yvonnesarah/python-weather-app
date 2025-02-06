import requests
from rich import print
from datetime import datetime

def display_temperatue(day, temperature, unit='C'):
  """Displays a temperature with day"""
  print(f"[blue]{day}[/blue]: {round(temperature)}º{unit}")

def display_current_weather(city):
  """Displays the current weather"""
  api_key = "8bcecf2b930c0252ec9aa584f9do621t"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

  response = requests.get(api_url)
  current_weather_data = response.json()
  current_weather_city = current_weather_data['city']
  current_weather_temperature = current_weather_data['temperature']['current']
  
  display_temperatue("Today", round(current_weather_temperature))

def display_forecast_weather(city_name):
  """Display the weather forecast of a city"""
  api_key = "8bcecf2b930c0252ec9aa584f9do621t"
  api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city_name}&key={api_key}"

  response = requests.get(api_url)
  forecast_weather_data = response.json()
  print("\n[green bold]Forecast:[/green bold]")
  for day in forecast_weather_data['daily']:
    timestamp = day['time']  
    date = datetime.fromtimestamp(timestamp)
    formatted_day = date.strftime("%A")
    temperature = day['temperature']['day']
    
    if date.date() != datetime.today().date():
      display_temperatue(formatted_day, round(temperature))

def credit():
  """Display a credit message"""
  print("\n[yellow]This app was built by Yvonne Adedeji[/yellow]")

def welcome():
  """Display a welcome"""
  print("[purple bold]Welcome to my weather app[/purple bold]")
  

welcome()
city_name = input("Enter a city: ")
city_name = city_name.strip()

if city_name:
  display_current_weather(city_name)
  display_forecast_weather(city_name)
  credit()
else:
  print("Please try again with a city")