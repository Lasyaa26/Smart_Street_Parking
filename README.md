# 🚗 Smart Street Parking

A **Smart and Effective Realtime Management of Street Parking** solution that helps users find, book, and pay for parking slots using real-time data, IoT integration, and dynamic pricing.

---

## 📜 Problem Statement
The system aims to:
- Identify and book the nearest available parking slot.
- Scan vehicle number plates upon entry and log entry time.
- Calculate charges dynamically based on weather conditions, rush, and weekends.
- Allow users to pay via the app during exit.
- Apply extra charges for late departure or cancellations.

This solution falls under the **Smart Automation** theme of the Smart India Hackathon.

---

## 🛠 Tech Stack
**Backend:**
- Python
- FastAPI (or Django as alternative)

**Frontend:**
- HTML, CSS, JavaScript
- Google Maps API for location display

**Database:**
- PostgreSQL / MySQL

**AI/ML:**
- OpenCV + EasyOCR/Tesseract for Automatic Number Plate Recognition (ANPR)

**APIs:**
- Google Maps API — locate parking lots
- OpenWeatherMap API — enable dynamic pricing

**IoT Integration (Simulated for Prototype):**
- CCTV / Camera for ANPR

---

## 📂 Project Structure
```

Smart\_Street\_Parking/
│
├── backend/
│   ├── main.py                 # FastAPI entry point
│   ├── database.py             # Database connection
│   ├── models.py               # Database models
│   ├── routes/
│   │   ├── parking.py          # Parking-related APIs
│   │   └── booking.py          # Booking APIs
│   ├── services/
│   │   ├── pricing.py          # Dynamic pricing logic
│   │   └── anpr.py             # Number plate recognition
│   ├── utils/
│   │   └── helpers.py          # Helper functions
│
├── frontend/
│   ├── index.html              # Main UI page
│   ├── app.js                  # Frontend logic
│   ├── styles.css              # Styling
│
├── tests/                      # Unit tests
│   ├── test\_parking.py
│   ├── test\_booking.py
│
├── README.md
├── requirements.txt
└── .gitignore

````

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Smart_Street_Parking.git
cd Smart_Street_Parking
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv

# Activate:
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Backend Server

```bash
uvicorn backend.main:app --reload
```

Server will be running at: **`http://127.0.0.1:8000`**

### 5️⃣ Run the Frontend

Open `frontend/index.html` in your browser.

---

## 📌 Features

* 🔍 **Real-time parking availability**
* 🗺 **Google Maps integration**
* 📸 **Automatic Number Plate Recognition**
* 💸 **Dynamic pricing based on conditions**
* 💳 **In-app payment simulation**
* 📊 **Historical data-based availability predictions**

---

## 📅 Roadmap

* [ ] Core backend APIs (`getParkingLots`, `bookSlot`, `calculatePrice`)
* [ ] Google Maps frontend integration
* [ ] ANPR number plate detection
* [ ] Database integration with PostgreSQL
* [ ] Dynamic pricing logic using Weather API
* [ ] Payment gateway simulation
* [ ] IoT hardware integration (optional for prototype)

---
