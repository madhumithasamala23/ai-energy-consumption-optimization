⚡ AI-Powered Smart Energy Consumption Monitoring and Optimization System
📌 Project Overview

Energy consumption in buildings is increasing due to inefficient usage, growing occupancy, and changing environmental conditions. This project presents an AI-based smart energy monitoring system that predicts energy consumption, estimates electricity cost, analyzes trends, and provides sustainability insights. The system supports informed decision-making to reduce energy wastage, lower costs, and promote sustainable energy practices.

🎯 Objectives

Predict energy consumption using machine learning

Analyze energy usage patterns

Estimate electricity cost based on predicted usage

Provide actionable sustainability insights

Support energy-efficient decision-making

🌍 SDG Alignment

SDG 7 – Affordable and Clean Energy

SDG 13 – Climate Action

🧠 AI & Technologies Used

Machine Learning Model: Random Forest Regression

Programming Language: Python

Frontend Interface: Streamlit

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Joblib

📂 Project Structure
ai_energy_optimization_streamlit/
│
├── data/
│   └── energy_data.csv
│
├── model/
│   └── energy_model.pkl
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md

📊 Dataset Description

Format: CSV

Records: 250

Features:

Temperature

Humidity

Occupancy

Hour of the day

Weekend indicator

Target Variable:

Energy consumption

The dataset represents realistic building energy usage scenarios.

⚙️ How the System Works

User provides input through a Streamlit interface

Input data is processed and passed to the trained AI model

The model predicts energy consumption

Electricity cost is estimated

Dynamic graphs and sustainability insights are generated

🖥️ How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Train the Model
python train_model.py

3️⃣ Run the Streamlit App
streamlit run app.py


Open the app in your browser at:

http://localhost:8501

📈 Features

AI-based energy consumption prediction

Interactive Streamlit user interface

Dynamic trend analysis and visualizations

Electricity cost estimation

Sustainability recommendations

🛡️ Responsible AI Considerations

No personal or sensitive data is used

Transparent and explainable predictions

Ethical use of AI for sustainability

Focus on awareness and decision support

🚀 Future Scope

Integration with real-time IoT sensors

Carbon footprint estimation

Mobile and cloud deployment

Smart alerts and recommendations

👩‍💻 Author

Madhumitha Samala
B.Tech – Computer Science and Engineering

📜 License

This project is developed for educational and sustainability purposes as part of the AI for Sustainability Virtual Internship (1M1B – IBM SkillsBuild).
