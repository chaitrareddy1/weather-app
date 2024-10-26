CREATE TABLE weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temperature REAL,
    condition TEXT,
    humidity INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
