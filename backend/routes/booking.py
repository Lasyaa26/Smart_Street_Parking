from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/booking", tags=["Booking"])

# Temporary storage for booked slots (no database yet)
bookings = []

@router.post("/bookSlot")
def book_slot(parking_id: int, user_name: str):
    booking_id = len(bookings) + 1
    booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    booking = {
        "booking_id": booking_id,
        "parking_id": parking_id,
        "user_name": user_name,
        "time": booking_time
    }
    bookings.append(booking)
    return {"status": "success", "message": "Slot booked successfully!", "booking": booking}
