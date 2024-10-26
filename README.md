

# Real-Time Weather Monitoring System

## Project Overview

The **Real-Time Weather Monitoring System** is a web application that continuously retrieves weather data from OpenWeatherMap for major Indian metro cities. It provides real-time data, daily summaries, and alerts based on configurable temperature thresholds. The system includes a frontend UI, a backend API built with Flask, and an SQLite database for storing historical weather data.

### Features
- **Real-Time Data Retrieval**: Fetches weather data for specified cities at regular intervals.
- **Daily Summaries**: Calculates daily averages, maximum, and minimum temperatures.
- **Alerts**: Configurable alert thresholds that trigger notifications when exceeded.
- **Data Visualization**: A chart-based UI displaying real-time weather trends and daily summaries.

---

## Project Structure
- **Frontend**: Built with HTML, JavaScript, and Chart.js for weather data visualization.
- **Backend**: Flask-based API to fetch and process weather data.
- **Database**: SQLite for storing historical weather data and thresholds.

---

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/chaitrareddy1/weather-app
   cd weather-monitoring-app
   ```

2. **Obtain OpenWeatherMap API Key**:
   - Register at [OpenWeatherMap](https://openweathermap.org/) to get a free API key.
   - Replace `"your_api_key"` in `weather_app.py` with your API key.

3. **Install Dependencies**:
   Ensure Python and Flask are installed, then install additional dependencies.
   ```bash
   pip install flask requests schedule
   ```

4. **Database Setup**:
   Initialize the SQLite database by running the schema file:
   ```bash
   sqlite3 weather_data.db < weather_schema.sql
   ```

5. **Start the Backend Server**:
   ```bash
   python weather_app.py
   ```

6. **Access the Frontend**:
   Open `weather.html` in a web browser.

---

## API Endpoints

1. **GET /weather**
   - **Description**: Fetch current weather data for a specified city.
   - **Params**: `?city=<city_name>`
   - **Response**: `{ "temp": 30.5, "condition": "Clear", "humidity": 50 }`

2. **POST /threshold**
   - **Description**: Set or update temperature alert thresholds.
   - **Body**: `{ "city": "Delhi", "threshold": 35 }`
   - **Response**: `{ "message": "Threshold set successfully" }`

3. **GET /alert**
   - **Description**: Check if any city’s weather data exceeds the configured threshold.
   - **Response**: `{ "alerts": ["Delhi: 37°C"] }`

---

## Non-Functional Considerations

- **Security**:
  - **API Key Management**: Securely store the OpenWeatherMap API key using environment variables.
  - **Rate Limiting**: Prevent API overuse by limiting requests to critical endpoints.
  - **Input Validation**: Validate city names and temperature threshold values.

- **Performance**:
  - **Scheduled Fetching**: Use scheduled data fetching to reduce server load.
  - **Database Optimization**: Index city and timestamp columns to improve data retrieval speed.
  - **Efficient Aggregation**: Summaries and roll-ups are calculated once per day, reducing redundant computations.

- **Scalability**:
  - **Flexible City Management**: Easily add or remove cities in the backend configuration.
  - **Alert Notifications**: Future support for email or SMS alerts for threshold breaches.

- **Maintainability**:
  - **Modular Design**: Separate data retrieval, processing, and alerting functions.
  - **Logging**: Track data retrieval, processing, and alerts for easier debugging and optimization.

---

## Future Enhancements

- **Additional Weather Parameters**: Include wind speed, pressure, and more in the summaries.
- **Historical Data Visualization**: Add UI for displaying trends over time.
- **Mobile App Integration**: Create a mobile interface for real-time weather alerts.

---

This README provides a comprehensive guide for setting up, using, and enhancing the **Real-Time Weather Monitoring System**. Contributions are welcome via pull requests or issue submissions.
