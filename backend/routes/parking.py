from fastapi import APIRouter
from backend.services.pricing import calculate_dynamic_price

router = APIRouter(prefix="/parking", tags=["Parking"])

# Mock parking data (lat/lon included for Open-Meteo)
parking_lots = [
    {
        "id": 1,
        "name": "City Center Parking",
        "lat": 17.4456,
        "lon": 78.3912,
        "available_slots": 5
    },
    {
        "id": 2,
        "name": "Mall Road Parking",
        "lat": 17.4500,
        "lon": 78.4000,
        "available_slots": 2
    }
]

@router.get("/getParkingLots")
def get_parking_lots():
    # Add dynamic pricing for each parking lot
    for lot in parking_lots:
        lot["price_per_hour"] = calculate_dynamic_price(
            available_slots=lot["available_slots"],
            city_lat=lot["lat"],
            city_lon=lot["lon"]
        )
    return parking_lots
