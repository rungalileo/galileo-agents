"""Weather tools."""
import random

CONDITIONS = ["sunny", "cloudy", "rainy", "partly cloudy", "foggy"]


def get_current_weather(city: str) -> dict:
    """Get current weather for a city (mock data)."""
    return {
        "city": city,
        "temperature_f": random.randint(45, 85),
        "conditions": random.choice(CONDITIONS),
        "humidity": random.randint(30, 80),
    }


def get_forecast(city: str, days: int = 3) -> dict:
    """Get weather forecast for a city (mock data)."""
    days = min(max(days, 1), 7)
    forecast = [
        {
            "day": i + 1,
            "high_f": random.randint(55, 90),
            "low_f": random.randint(40, 65),
            "conditions": random.choice(CONDITIONS),
        }
        for i in range(days)
    ]
    return {"city": city, "forecast": forecast}
