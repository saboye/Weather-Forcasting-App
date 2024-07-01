import requests
import streamlit as st

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
GEO_URL = f"https://api.openweathermap.org/geo/1.0/direct?q"
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def get_lat_lon(city_name):
    """
    Obtain latitude and longitude for a given city name.

    This function sends a request to the OpenWeatherMap Geocoding API to
    get the geographic coordinates (latitude and longitude) of a city.

    Args:
    city_name (str): The name of the city for which to find the coordinates.

    Returns:
    tuple: A tuple containing the latitude and longitude of the city.

    Raises:
    Exception: If no geocoding data is found for the specified city.
    """
    # Constructing the complete geocode URL with city name and API key
    city_url = f"{GEO_URL}={city_name}&limit=1&appid={API_KEY}"

    # Sending a request to the geocode API
    response = requests.get(city_url)

    # Raises an exception for HTTP error codes
    response.raise_for_status()
    data = response.json()

    # Returning the latitude and longitude if data is found
    if data:
        return data[0]['lat'], data[0]['lon']
    else:
        raise Exception(f"No geocoding data found for {city_name}")


def get_weather(lat, lon, units):
    """
    Fetch the current weather data for a given latitude and longitude.

    This function sends a request to the OpenWeatherMap API to get the current
    weather data based on geographic coordinates.

    Args:
    lat (float): Latitude of the location.
    lon (float): Longitude of the location.
    units (str): Units of measurement (e.g., 'metric', 'imperial').

    Returns:
    dict: A dictionary containing weather data.
    """
    # Constructing the complete weather API URL with coordinates, units, and API key
    weather_url = f"{BASE_URL}?lat={lat}&lon={lon}&units={units}&appid={API_KEY}"

    # Sending a request to the weather API
    response = requests.get(weather_url)
    # Raises an exception for HTTP error codes
    response.raise_for_status()
    return response.json()


def get_weather_by_zip(zip_code, units):
    """
    Fetch the current weather data for a given zip code.

    This function sends a request to the OpenWeatherMap API using a zip code
    to obtain the current weather data for that area. The units of measurement
    for the weather data (e.g., 'metric') can also be specified.

    Args:
    zip_code (str): The zip code for the desired location.
    units (str): Units of measurement (e.g., 'metric').

    Returns:
    dict or None: A dictionary containing the weather data if the request is
    successful, or None if the request fails.
    """
  
    # Constructing the complete weather API URL with zip code, units, and API key
    zip_url =f"{BASE_URL}?zip={zip_code}&appid={API_KEY}&units={units}"
    response = requests.get(zip_url)
    if response.status_code == 200:
        # Return the JSON response if successful
        return response.json()
    else:
        # Return None if the request failed
        return None


def display_weather(weather_data):
    """
    Display weather data using Streamlit.

    This function takes weather data as input and displays various aspects of the
    weather (such as temperature, pressure, humidity, etc.) in a user-friendly
    format using Streamlit library. It handles any KeyError exceptions to manage cases
    where expected data might be missing in the weather_data input.

    Args:
    weather_data (dict): A dictionary containing weather data.

    Returns:
    None: This function does not return anything. It only displays data on a Streamlit app.
    """
    try:
        # Extracting and formatting the necessary information from weather_data
        location = f"{weather_data['name']},{weather_data['sys']['country']}"
        current_temp = weather_data['main']['temp']
        feels_like_temp = weather_data['main']['feels_like']
        low_temp = weather_data['main']['temp_min']
        high_temp = weather_data['main']['temp_max']
        pressure = weather_data['main']['pressure']
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']

        # Displaying the weather information using Streamlit
        st.write(f"Weather for {location}")
        st.write(f"  Current Temp: {current_temp}°")
        st.write(f"  Feels Like: {feels_like_temp}°")
        st.write(f"  Low Temp: {low_temp}°")
        st.write(f"  High Temp: {high_temp}°")
        st.write(f"  Pressure: {pressure} hPa")
        st.write(f"  Humidity: {humidity}%")
        st.write(f"  Description: {weather_description.capitalize()}")

    except KeyError:
        # Handling cases where expected data fields are missing
        st.write("Error processing the weather data. Please try again later.")


def main():
    # Setting the configuration for the Streamlit page
    st.set_page_config(
        page_title="Weather Forecast Application",
        page_icon="🌧️️",
        layout="centered"
    )
    # Adding a custom background image to the Streamlit app
    st.markdown(
        f"""
             <style>
             .stApp {{
                 background: url("https://images.unsplash.com/photo-1638272181967-7d3772a91265");
                 background-size: cover
             }}
             
             </style>
             """,
        unsafe_allow_html=True
    )
    # Hiding the default footer of the Streamlit app
    st.markdown(
        """
        <style>
        footer {
            visibility: hidden;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
    # Displaying the title and other headers
    st.title("☀️ 🌧️ 🌈 🌂 ❄️")
    st.markdown("<h1 style='color: purple;'>Bellevue University</h1>", unsafe_allow_html=True)
    st.subheader("DSC 510 - Term Project")
    st.subheader("Author:  Samuel Aboye")
    st.subheader("Weather Forecast App")
    # User input for choosing between city or zip code
    choice = st.radio("Choose input method:", ("City", "Zip Code"),horizontal=True)

    # User input for choosing temperature units
    units_choice = st.radio("Select temperature units:", ("Celsius", "Fahrenheit", "Kelvin"))

    # Assigning units based on user choice
    if units_choice == "Celsius":
        units = "metric"
    elif units_choice == "Fahrenheit":
        units = "imperial"
    else:
        units = "standard"

    # Handling user input for city name and displaying weather
    if choice == "City":
        city_name = st.text_input("Enter city name:")  # Text input for city name
        if city_name:
            try:
                latitude, longitude = get_lat_lon(city_name)  # Getting coordinates for the city
                weather_data = get_weather(latitude, longitude, units)  # Fetching weather data
                if weather_data:
                    display_weather(weather_data)  # Displaying weather data
                else:
                    st.write("Error retrieving weather data for the given location. Please try again later.")
            except Exception as e:
                st.write(f"An error occurred: {e}")

    # Handling user input for zip code and displaying weather
    else:
        zip_code = st.text_input("Enter zip code:")  # Text input for zip code
        if zip_code:
            weather_data = get_weather_by_zip(zip_code,units)  # Fetching weather data by zip code
            if weather_data:
                display_weather(weather_data)  # Displaying weather data
            else:
                st.write(
                    "Error retrieving weather data for the given zip code. Please check the zip code or try again"
                    "later")


if __name__ == "__main__":
    main()
