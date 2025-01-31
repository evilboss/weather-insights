import pandas as pd

# Define the function to process weather data and generate insights
def process_weather_data(file_path: str, fluctuation_threshold: float = 10.0):
    try:
        # Load the CSV file
        data = pd.read_csv(file_path)

        # Ensure required columns exist
        required_columns = ['city', 'date', 'temperature_fahrenheit']
        if not all(col in data.columns for col in required_columns):
            raise ValueError("CSV file is missing one or more required columns: 'city', 'date', 'temperature_fahrenheit'")

        # 1. Highest Temperature by City
        highest_temp_by_city = data.groupby('city')['temperature_fahrenheit'].max().to_dict()

        # 2. Temperature Fluctuation
        temp_range_by_city = data.groupby('city')['temperature_fahrenheit'].agg(lambda x: x.max() - x.min())
        cities_with_high_fluctuation = temp_range_by_city[temp_range_by_city > fluctuation_threshold].index.tolist()

        # 3. Average Temperature by City
        avg_temp_by_city = data.groupby('city')['temperature_fahrenheit'].mean().to_dict()

        # 4. Highest Temperature by Date
        max_temp_per_date = data.groupby('date')['temperature_fahrenheit'].max().reset_index()

        # Merge with the original data to get the city name associated with the max temperature
        max_temp_with_city = pd.merge(max_temp_per_date, data, on=['date', 'temperature_fahrenheit'])

        # Extract the result as a dictionary
        highest_temp_by_date = max_temp_with_city.set_index('date')['city'].to_dict()


# 5. Average Temperature across all data
        overall_avg_temperature = data['temperature_fahrenheit'].mean()

        # Compile the results
        insights = {
            "highest_temperature_by_city": highest_temp_by_city,
            "highest_temperature_by_date": highest_temp_by_date,
            "cities_with_high_fluctuation": cities_with_high_fluctuation,
            "city_averages": avg_temp_by_city,
            "average_temperature": overall_avg_temperature
        }

        return insights

    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to the CSV file
file_path = './data/weather_data.csv'

# Process the weather data and print the insights
weather_insights = process_weather_data(file_path)
if weather_insights:
    import json
    print(json.dumps(weather_insights, indent=4))
