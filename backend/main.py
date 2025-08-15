from fastapi import FastAPI
from backend.routes.anpr import router as anpr_router  # correct import

app = FastAPI(title="Smart Street Parking API")

# Include ANPR router
app.include_router(anpr_router)

# Dummy Parking Lots Data
parking_lots_data = [
    {"id": 1, "name": "Main Street Lot", "lat": 17.4456, "lng": 78.3912, "available_slots": 5, "price_per_hour": 50},
    {"id": 2, "name": "City Center Lot", "lat": 17.4460, "lng": 78.3920, "available_slots": 0, "price_per_hour": 60},
]

@app.get("/parking/getParkingLots")
async def get_parking_lots():
    return parking_lots_data

@app.post("/booking/bookSlot")
async def book_slot(parking_id: int, user_name: str):
    for lot in parking_lots_data:
        if lot["id"] == parking_id:
            if lot["available_slots"] > 0:
                lot["available_slots"] -= 1
                return {"message": f"Slot booked successfully for {user_name} at {lot['name']}"}
            else:
                return {"message": "No slots available"}, 400
    return {"message": "Parking lot not found"}, 404
