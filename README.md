# 📰 AI News Agent

An **AI-powered news research and writing agent** that automatically **fetches, analyzes, and generates high-quality news articles** using a multi-agent architecture and Generative AI.

This project demonstrates how **AI agents can collaborate** to research topics, summarize insights, and produce structured news content with minimal human effort.

---

## 🚀 Features

- 🔍 **AI News Research Agent**

  Gathers and analyzes news-related information on a given topic
  
- ✍️ **AI News Writing Agent**

  Converts research output into clear, readable news articles

- 🤝 **Multi-Agent Workflow**

  Separate agents for research and content generation

- ⚙️ **Modular Design**

  Easy to extend with new agents or tools

- 🧠 **Generative AI Powered**

  Uses Google Gemini for intelligent reasoning and writing

---

## 🏗️ Architecture 
AI-News-Agent/

│

├── crewgooglegemini/

│   ├── agents.py        # Defines AI agents

│   ├── tasks.py         # Research & writing tasks

│   ├── tools.py         # Agent tools

│   ├── crew.py          # Main execution file

│

├── requirements.txt     # Project dependencies

├── .gitignore           # Ignored files

├── Notes.txt            # Development notes

└── README.md            # Project documentation

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

git clone https://github.com/Kasyap18/AI-News-Agent.git

cd AI-News-Agent

### 2️⃣ Create and activate a virtual environment

python -m venv venv

venv\Scripts\activate

### 3️⃣ Install dependencies

pip install -r requirements.txt

### 4️⃣ Configure environment variables

Create a .env file in the project root:

env

GOOGLE_API_KEY=your_api_key_here

---

### ▶️ How to Run

python crewgooglegemini/crew.py

The system will:

Research the given news topic

Analyze relevant information

Generate a complete news article

---

### 🧪 Use Cases
Automated news generation

AI journalism experiments

Learning multi-agent systems

Generative AI portfolio project

Internship and academic demonstrations

---

### 🛠️ Tech Stack
Python

Google Gemini (Generative AI)

Agent-based Architecture

Crew-style workflows

Environment variable configuration

--- 

###  🌱 Future Enhancements
Web interface (Streamlit / React)

Database storage for articles

Fact-checking agent

Multiple news category support

API-based deployment

Instead of diagrams, the architecture is explained as a clear execution flow:

