<div align="center">
  <h1>Weather Forecast Application</h1>
</div>

This repository contains a simple weather forecast application built using Python, Streamlit, and the OpenWeatherMap API. The application allows users to get current weather data by city name or zip code and displays the weather information in a user-friendly format.

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [API Key](#api-key)


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/saboye/weather-forecast-app.git
    cd weather-forecast-app
    ```

2. Install the required packages:
    ```sh
    pip install requests streamlit
    ```

3. Set up your OpenWeatherMap API key:
    - Sign up on [OpenWeatherMap](https://openweathermap.org/) and obtain an API key.
    - Replace `"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"` in the code with your API key.

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Choose to input by city name or zip code, select the desired temperature units, and view the weather data.

## Code Explanation

### `get_lat_lon(city_name)`

This function obtains the latitude and longitude for a given city name by sending a request to the OpenWeatherMap Geocoding API.

### `get_weather(lat, lon, units)`

This function fetches the current weather data for a given latitude and longitude using the OpenWeatherMap API.

### `get_weather_by_zip(zip_code, units)`

This function fetches the current weather data for a given zip code using the OpenWeatherMap API.

### `display_weather(weather_data)`

This function displays the weather data using Streamlit, showing details such as temperature, pressure, humidity, and weather description.

### `main()`

This is the main function that sets up the Streamlit application, handles user inputs, fetches weather data, and displays the results.

## API Key

You need an API key from OpenWeatherMap to run this application. Sign up on [OpenWeatherMap](https://openweathermap.org/) to get your free API key. Replace the placeholder in the code with your actual API key:

```python
API_KEY = "YOUR_API_KEY_HERE"
