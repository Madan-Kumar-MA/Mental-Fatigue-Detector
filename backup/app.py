import streamlit as st
import time
from joblib import load
import numpy as np

st.title("Mental Fatigue Detector")
st.write("Type in the box below. When done, click 'Analyze Fatigue'.")

if 'key_times' not in st.session_state:
    st.session_state.key_times = []
if 'hold_times' not in st.session_state:
    st.session_state.hold_times = []
if 'last_key_time' not in st.session_state:
    st.session_state.last_key_time = None

user_input = st.text_area("Type here:", height=200, key="text_input")

# Simulate key timing based on typing events (Streamlit can't capture real keypress times)
def simulate_typing_metrics(text):
    # For demo: fake timings based on text length
    n = len(text)
    if n < 5:
        return None, None
    avg_hold = 0.15 + 0.05 * np.random.rand()  # Simulate hold time
    typing_speed = n / (2 + np.random.rand())  # Simulate speed
    return avg_hold, typing_speed

if st.button("Analyze Fatigue"):
    avg_hold, typing_speed = simulate_typing_metrics(user_input)
    if avg_hold is None:
        st.warning("Please type more text before analyzing.")
    else:
        features = np.array([[avg_hold, typing_speed]])
        model = load("fatigue_model.joblib")
        prediction = model.predict(features)[0]
        result = "🧠 Fatigued!" if prediction == 1 else "✅ Not Fatigued"
        st.success(f"Result: {result}")
        st.info(f"Hold Time: {avg_hold:.4f} | Speed: {typing_speed:.2f}")
