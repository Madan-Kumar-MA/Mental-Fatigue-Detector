import tkinter as tk
import time
from joblib import load
import numpy as np

key_times = []
hold_times = []
last_key_time = None

def on_key_press(event):
    global last_key_time
    current_time = time.time()
    key_times.append(current_time)
    if last_key_time:
        hold_times.append(current_time - last_key_time)
    last_key_time = current_time

def analyze_typing():
    if len(hold_times) < 5:
        result_label.config(text="Please type more text before analyzing.")
        return

    avg_hold = np.mean(hold_times)
    typing_speed = len(key_times) / (key_times[-1] - key_times[0] + 1e-5)

    features = np.array([[avg_hold, typing_speed]])
    model = load("fatigue_model.joblib")
    prediction = model.predict(features)[0]

    result = "🧠 Fatigued!" if prediction == 1 else "✅ Not Fatigued"
    result_label.config(text=f"Result: {result}\nHold Time: {avg_hold:.4f} | Speed: {typing_speed:.2f}")

# GUI setup
root = tk.Tk()
root.title("Mental Fatigue Detector")

tk.Label(root, text="Type here:").pack()

text_box = tk.Text(root, height=10, width=50)
text_box.pack()
text_box.bind("<KeyPress>", on_key_press)

tk.Button(root, text="Analyze Fatigue", command=analyze_typing).pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
