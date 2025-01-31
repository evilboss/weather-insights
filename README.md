# Weather Insights Project

## Overview
The Weather Insights Project processes and analyzes weather data from a CSV file to generate key insights. This project calculates the highest temperatures, identifies cities with significant temperature fluctuations, and computes averages for both individual cities and the dataset as a whole.

## Features
1. **Highest Temperature by City:** Identify the maximum temperature recorded for each city.
2. **Temperature Fluctuation:** Detect cities where the temperature fluctuation exceeds a specified threshold.
3. **Average Temperature:** Calculate the average temperature for all cities and the entire dataset.
4. **Highest Temperature by Date:** Find the city with the highest temperature for each date.
5. **Clean and Reusable Code:** The script includes error handling and is optimized for maintainability.

## Project Structure
```
weather_insights_project/
├── main.py                # Main Python script
├── requirements.txt        # Project dependencies
├── .gitignore              # Git ignore file
└── data/
    └── weather_data.csv    # Sample CSV file with weather data
```

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd weather_insights_project
   ```

2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Place your CSV file containing weather data in the `data/` directory.
   The CSV file should have the following columns:
    - `city`
    - `date`
    - `temperature_fahrenheit`

2. Run the script:
   ```sh
   python main.py
   ```

3. The script will print insights, including highest temperatures, city averages, and more.

## Example Output
```json
{
    "highest_temperature_by_city": {
        "New York": 100,
        "Los Angeles": 98
    },
    "highest_temperature_by_date": {
        "2024-09-01": "New York",
        "2024-09-02": "Los Angeles"
    },
    "cities_with_high_fluctuation": [
        "Chicago",
        "Houston"
    ],
    "city_averages": {
        "New York": 74.5,
        "Los Angeles": 71.0
    },
    "average_temperature": 72.8
}
```

## Dependencies
- `pandas`
