🌊 FloatChat – AI Ocean Data Chatbot

FloatChat is an AI-powered chatbot for ocean data analysis.
Instead of writing complex code, users can ask questions in simple English and the system will automatically analyze the dataset and generate answers or visualizations.

The project is designed to make scientific data exploration easy and interactive.

🚀 What This Project Does

FloatChat allows users to:

Ask questions about ocean data
Get instant statistical answers
Automatically generate graphs and visualizations
Explore datasets without writing code
For example, a user can ask:
"Show the temperature trend by date"
And the system will automatically generate the correct plot.

🧠 How It Works

The user types a question in the chatbot interface.
The system understands the question using AI models.
If the question needs analysis:
Python code is generated automatically.
The code runs on the dataset.

The system returns:

A text answer, or
A generated visualization.

🧰 Major Technologies Used
Backend
Python
FastAPI – API for handling chatbot requests
OpenAI API – Understanding questions and generating code
Ollama (Llama3) – Local AI fallback model
Data Processing
Pandas – Data analysis
NumPy – Numerical operations
Visualization
Matplotlib
Seaborn
Frontend
Streamlit – Chat interface and visualization display

📊 Features
💬 Natural language data queries
📈 Automatic chart generation
📉 Statistical calculations (mean, max, min, etc.)

🌊 Ocean dataset analysis
🧠 AI-powered data interpretation
🖥 Interactive web interface

📁 Project Structure
FloatChat
│
├── hackvibe_merged.py     # Backend API and AI logic
├── chatbot_ui3.py         # Streamlit chatbot interface
├── dataset.csv            # Ocean dataset
└── README.md
▶️ How to Run the Project
1️⃣ Install Dependencies
pip install fastapi uvicorn pandas numpy matplotlib seaborn streamlit openai
2️⃣ Start the Backend API
uvicorn hackvibe_merged:app --reload
3️⃣ Run the Chat Interface
streamlit run chatbot_ui3.py
4️⃣ Ask Questions

Example questions:
Plot temperature vs pressure
Show daily nitrate trend
What is the mean temperature?
Show columns in the dataset

🎯 Goal of the Project
The goal of FloatChat is to make scientific datasets easier to explore using AI.
Instead of learning complex data tools, users can simply chat with the data.

🌍 Future Improvements
Support more datasets
Add advanced visualizations

Improve AI understanding

Deploy as a cloud web application
