# ⚡ AI-Powered Smart Energy Consumption Monitoring and Optimization System

## 📌 Project Overview
Energy consumption in buildings such as homes, offices, and educational institutions is increasing due to inefficient usage, growing occupancy, and changing environmental conditions. Traditional energy monitoring systems mainly provide historical data and lack predictive and decision-support capabilities.

This project presents an **AI-powered smart energy consumption monitoring system** that predicts energy usage, estimates electricity cost, analyzes consumption trends, and provides sustainability insights. The solution helps users make informed decisions to reduce energy wastage, lower electricity costs, and promote sustainable energy practices.

---

## 🎯 Objectives
- Predict energy consumption using machine learning  
- Analyze energy usage trends  
- Estimate electricity cost based on predicted usage  
- Provide actionable sustainability insights  
- Support energy-efficient decision-making  

---

## 🌍 Sustainable Development Goals (SDGs)
- **SDG 7 – Affordable and Clean Energy**  
- **SDG 13 – Climate Action**

---

## 🧠 AI & Technologies Used
- **Machine Learning Model:** Random Forest Regression  
- **Programming Language:** Python  
- **Web Interface:** Streamlit  
- **Libraries:**  
  - Pandas (data processing)  
  - NumPy (numerical operations)  
  - Scikit-learn (model training)  
  - Matplotlib (visualization)  
  - Joblib (model persistence)

---

## 📂 Project Structure
ai_energy_optimization_streamlit/
│
├── data/
│ └── energy_data.csv
│
├── model/
│ └── energy_model.pkl
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md

---

## 📊 Dataset Description
- **Format:** CSV  
- **Number of Records:** 250  
- **Features:**
  - Temperature (°C)
  - Humidity (%)
  - Occupancy
  - Hour of the day
  - Weekend indicator  
- **Target Variable:**
  - Energy consumption  

The dataset represents realistic energy usage scenarios in buildings.

---

## ⚙️ System Workflow
1. User provides input through the Streamlit interface  
2. Input data is processed and passed to the trained AI model  
3. The model predicts energy consumption  
4. Electricity cost is estimated  
5. Dynamic graphs and sustainability insights are generated  

---

## 🖥️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
2️⃣ Train the AI Model
python train_model.py

3️⃣ Run the Streamlit Application
streamlit run app.py


Open the application in your browser:

http://localhost:8501

📈 Features

AI-based energy consumption prediction

Interactive Streamlit web interface

Dynamic trend analysis and visualizations

Electricity cost estimation

Sustainability and energy-saving recommendations

🛡️ Responsible AI Considerations

No personal or sensitive data is used

Transparent and explainable AI predictions

Ethical and responsible use of AI

Focus on sustainability and awareness

🚀 Future Enhancements

Integration with real-time IoT energy meters

Carbon footprint estimation

Cloud deployment

Mobile application support

Smart alerts and notifications

👩‍💻 Author

Madhumitha Samala

📜 License

This project is developed for educational purposes as part of the
AI for Sustainability Virtual Internship (1M1B – IBM SkillsBuild).
