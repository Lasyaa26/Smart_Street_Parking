import streamlit as st
import requests
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Smart Street Parking", layout="wide")

st.title("🚗 Smart Street Parking")
st.write("Find and book available parking slots in real-time.")

# Backend API URL
PARKING_API = "http://127.0.0.1:8000/parking/getParkingLots"
BOOKING_API = "http://127.0.0.1:8000/booking/bookSlot"

try:
    response = requests.get(PARKING_API)
    if response.status_code == 200:
        parking_lots = response.json()

        # Convert to DataFrame
        df = pd.DataFrame(parking_lots)

        # Rename 'lng' to 'lon' for Streamlit compatibility
        df = df.rename(columns={"lng": "lon"})

        # Add color coding: Green if available, Red if full
        df["color"] = df["available_slots"].apply(lambda x: [0, 255, 0] if x > 0 else [255, 0, 0])

        # Pydeck Layer for markers
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position='[lon, lat]',
            get_color='color',
            get_radius=50,
            pickable=True,
        )

        # View settings
        view_state = pdk.ViewState(
            latitude=df["lat"].mean(),
            longitude=df["lon"].mean(),
            zoom=14,
            pitch=0,
        )

        # Tooltip
        tooltip = {
            "html": "<b>{name}</b><br/>Slots Available: {available_slots}",
            "style": {"backgroundColor": "steelblue", "color": "white"}
        }

        # Render map
        st.subheader("📍 Parking Locations")
        st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip))

        # Booking Section
        st.subheader("📋 Parking Lot Details & Booking")
        for _, row in df.iterrows():
            col1, col2, col3 = st.columns([3, 2, 2])
            with col1:
                st.write(f"**{row['name']}** — {row['available_slots']} slots available — 💰 ₹{row['price_per_hour']} / hour")
            with col2:
                st.write(f"📍 Location: ({row['lat']}, {row['lon']})")
            with col3:
                if row['available_slots'] > 0:
                    user_name = st.text_input(f"Your Name for booking {row['id']}", key=f"name_{row['id']}")
                    if st.button(f"Book Now - {row['id']}"):
                        if user_name.strip():
                            booking_response = requests.post(
                                BOOKING_API,
                                params={"parking_id": row['id'], "user_name": user_name}
                            )
                            if booking_response.status_code == 200:
                                st.success(booking_response.json()["message"])
                            else:
                                st.error("Booking failed. Try again.")
                        else:
                            st.warning("Please enter your name before booking.")
                else:
                    st.warning("No slots available")

    else:
        st.error(f"Failed to fetch parking lot data. Status code: {response.status_code}")

except requests.exceptions.ConnectionError:
    st.error("⚠ Backend server is not running. Please start it first.")

st.subheader("📷 ANPR Simulation - Number Plate Recognition")
uploaded_file = st.file_uploader("Upload car number plate image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:8000/anpr/processPlate", files=files)

    if response.status_code == 200:
        result = response.json()
        if "error" in result:
            st.error(result["error"])
        else:
            st.success(result["message"])
            if "price_per_hour" in result:  # Entry case
                st.info(f"💰 Price per Hour: ₹{result['price_per_hour']}")
            if "duration_hours" in result:  # Exit case
                st.info(f"🕒 Duration: {result['duration_hours']} hrs")
                st.info(f"💰 Bill Amount: ₹{result['bill_amount']}")
    else:
        st.error("Error processing the image.")
