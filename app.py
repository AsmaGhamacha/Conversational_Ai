import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import streamlit as st
from datetime import datetime
from rag_pipeline import rag_respond
from codecarbon import EmissionsTracker
import time
import csv
from PIL import Image

import base64 #to center the image


st.set_page_config(page_title="AI Study Buddy", layout="wide")
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f8e8f8 0%, #e9f3ff 100%);
        font-family: 'Georgia', serif;
    }
    .stTextInput>div>div>input {
        background-color: #ffffffdd;
        color: #444;
    }
    </style>
    """, unsafe_allow_html=True
)

st.title("AI Study Assistant")
st.subheader("Ask me anything about Artificial Intelligence!😁")

if "history" not in st.session_state: #chat history
    st.session_state.history = []

user_input = st.text_input("Your question:", key="input")#input


#a log file to keep history of every prompt and its response (making sure that the file is created)
os.makedirs("logs", exist_ok=True)
log_path = "logs/gui_log.csv"
if not os.path.exists(log_path):
    with open(log_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Query", "Answer", "CO2 (g)", "Energy (kWh)", "Duration (s)"])

#running response and the emission tracker (new input)
if user_input:
    st.write("sit still and let me think...")

    tracker = EmissionsTracker(output_file="logs/codecarbon_gui.csv", log_level="error")
    tracker.start()
    start_time = time.time()

    answer = rag_respond(user_input)

    emissions_data = tracker.stop()
    end_time = time.time()

    duration = round(end_time - start_time, 2)
    co2 = round(emissions_data, 6)
    energy = round(emissions_data.energy_consumed, 6) if hasattr(emissions_data, "energy_consumed") else "N/A"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    #Save interaction
    entry = {
        "query": user_input,
        "answer": answer,
        "co2": co2,
        "energy": energy,
        "duration": duration
    }
    st.session_state.history.append(entry)

    with open(log_path, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, user_input, answer, co2, energy, duration])

#the display of the response and the history of the conversation
for entry in reversed(st.session_state.history):
    st.markdown(f"**🤷🏻‍♂️🤷🏻‍♀️You:** {entry['query']}")
    st.markdown(f"**🤖Agent:** {entry['answer']}")
    with st.expander("Impact report"):
        st.write(f"**CO₂:** {entry['co2']} g")
        st.write(f"**Energy:** {entry['energy']} kWh")
        st.write(f"**Duration:** {entry['duration']} seconds")

st.markdown("---")
st.markdown("<center><small>Made with 💖 for academic AI exploration by Asma GHAMACHA</small></center>", unsafe_allow_html=True)


def get_base64_image(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load image as base64
image_base64 = get_base64_image("assets/AlanTuring_Chibi.png")

# Display centered image with caption
st.markdown(
    f"""
    <div style='text-align: center; margin-top: 30px;'>
        <img src="data:image/png;base64,{image_base64}" width="120"/><br><br>
        <div style='font-size:20px; font-weight: bold;'>AI isn't scary, unless it runs out of GPU🥲</div>
        <div style='font-size:14px;'>(By Alan Turing... Probably)</div>
    </div>
    """,
    unsafe_allow_html=True
)
