import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

# ========================
# Page Configuration
# ========================
st.set_page_config(
    page_title="AI Energy Optimization System",
    page_icon="⚡",
    layout="centered"
)

# ========================
# Load Model & Dataset
# ========================
model = joblib.load("model/energy_model.pkl")
data = pd.read_csv("data/energy_data.csv")

# ========================
# App Title
# ========================
st.title("⚡ AI-Powered Smart Energy Consumption Monitoring and Optimization System")

st.markdown("""
This system uses **Artificial Intelligence** to predict energy consumption,
estimate electricity cost, and analyze usage trends for **sustainable energy management**.
""")

st.divider()

# ========================
# User Input Section
# ========================
st.header("🔮 Energy Consumption Prediction")

temperature = st.slider("🌡 Temperature (°C)", 18, 45, 30)
humidity = st.slider("💧 Humidity (%)", 30, 90, 60)
occupancy = st.number_input("👥 Occupancy", min_value=1, max_value=500, value=100)
hour = st.slider("⏰ Hour of the Day", 0, 23, 12)
is_weekend = st.selectbox("📅 Is it Weekend?", ["No", "Yes"])

is_weekend_val = 1 if is_weekend == "Yes" else 0

# ========================
# Prediction + Graphs
# ========================
if st.button("🔮 Predict Energy Consumption"):

    # ---- Prediction ----
    input_data = np.array([[temperature, humidity, occupancy, hour, is_weekend_val]])
    prediction = round(model.predict(input_data)[0], 2)

    cost_per_unit = 6
    estimated_cost = round(prediction * cost_per_unit, 2)

    st.success(f"⚡ Predicted Energy Consumption: **{prediction} units**")
    st.info(f"💰 Estimated Electricity Cost: **₹{estimated_cost}**")

    if prediction > 500:
        st.warning(
            "⚠ High energy usage detected. Consider reducing occupancy or optimizing appliance usage."
        )
    else:
        st.success(
            "✅ Energy usage is within a sustainable and cost-efficient range."
        )

    st.divider()

    # ========================
    # Dynamic Graphs Section
    # ========================
    st.header("📊 Energy Consumption Analysis (Based on Your Input)")

    # Filter dataset based on selected context
    filtered_data = data[
        (data["hour"] == hour) &
        (data["is_weekend"] == is_weekend_val)
    ]

    # ---- Graph 1: Occupancy vs Energy ----
    st.subheader("👥 Occupancy vs Energy Consumption")

    fig1, ax1 = plt.subplots()
    ax1.scatter(filtered_data["occupancy"], filtered_data["energy_consumption"], alpha=0.6)
    ax1.set_xlabel("Occupancy")
    ax1.set_ylabel("Energy Consumption")
    ax1.set_title("Energy Usage Pattern for Selected Time")
    st.pyplot(fig1)

    # ---- Graph 2: Temperature vs Energy ----
    st.subheader("🌡 Temperature vs Energy Consumption")

    fig2, ax2 = plt.subplots()
    ax2.scatter(filtered_data["temperature"], filtered_data["energy_consumption"], alpha=0.6)
    ax2.set_xlabel("Temperature (°C)")
    ax2.set_ylabel("Energy Consumption")
    ax2.set_title("Impact of Temperature on Energy Usage")
    st.pyplot(fig2)

    # ---- Graph 3: Average Energy ----
    st.subheader("📈 Average Energy Consumption Comparison")

    avg_energy = filtered_data["energy_consumption"].mean()

    fig3, ax3 = plt.subplots()
    ax3.bar(["Average Usage", "Your Prediction"], [avg_energy, prediction])
    ax3.set_ylabel("Energy Consumption")
    ax3.set_title("Your Usage vs Historical Average")
    st.pyplot(fig3)

    st.divider()

    # ========================
    # Insights Section
    # ========================
    st.header("💡 AI-Generated Insights")

    st.markdown(f"""
- 🔹 For the selected hour (**{hour}:00**), energy usage is influenced mainly by **occupancy and temperature**.
- 🔹 Your predicted usage is **{'higher' if prediction > avg_energy else 'lower'} than the historical average**.
- 🔹 Optimizing energy use at this time can **reduce cost and environmental impact**.
    """)

    st.success("🌱 Data-driven decisions help achieve sustainable and efficient energy consumption.")
