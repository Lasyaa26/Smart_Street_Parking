from fastapi import APIRouter, File, UploadFile
import easyocr
import cv2
import numpy as np
import time

router = APIRouter(prefix="/anpr", tags=["ANPR"])

# Store entry times for simulation
entry_records = {}

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

@router.post("/processPlate")
async def process_plate(file: UploadFile):
    contents = await file.read()

    # Convert to numpy array and decode image
    np_img = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # OCR detection
    results = reader.readtext(image)

    plate_number = None
    for res in results:
        text = res[1]
        if len(text) >= 5:  # crude filter
            plate_number = text.strip()
            break

    if not plate_number:
        return {"error": "No plate detected"}

    # Check if entry or exit
    if plate_number not in entry_records:
        # Entry
        entry_records[plate_number] = time.time()
        return {"message": f"Vehicle {plate_number} entry recorded."}
    else:
        # Exit - calculate duration
        entry_time = entry_records.pop(plate_number)
        duration_hours = (time.time() - entry_time) / 3600
        bill_amount = round(duration_hours * 50, 2)  # base rate

        return {
            "message": f"Vehicle {plate_number} exit recorded.",
            "duration_hours": round(duration_hours, 2),
            "bill_amount": bill_amount
        }
