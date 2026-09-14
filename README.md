# 🩺 Intelligent Medical RAG Assistant

A full-stack Retrieval-Augmented Generation (RAG) web application designed for accurate medical document querying and smart Q&A, powered by local LLMs.

---

## 🚀 Architecture & Tech Stack

* **Backend:** FastAPI, Python, LangChain/ChromaDB (Vector Store)
* **Frontend:** Streamlit (Interactive Chat UI)
* **AI Model:** Ollama (llama3.2:3b running locally)
* **Testing:** Pytest (Unit Testing)
* **Containerization:** Docker Support

---

## 📂 Project Structure

rag-assistant-project/
├── backend/
│   ├── app/
│   │   ├── api/        # API Routes & Endpoints
│   │   ├── core/       # Configurations & Settings
│   │   ├── schemas/    # Pydantic Data Models
│   │   └── services/   # RAG Pipeline & Retrieval Logic
│   ├── main.py         # FastAPI Entry Point
│   └── ...
├── frontend/
│   ├── app.py          # Streamlit User Interface
│   ├── api_client.py   # Backend Communication Client
│   └── ...
├── tests/              # Unit & Integration Tests
├── .env.example        # Environment Variables Template
├── Dockerfile          # Container Configuration
└── README.md

---

## ⚙️ Setup & Installation Guide

### 1. Clone the Repository & Setup Environment
git clone <repository-url>
cd rag-assistant-project
python -m venv .venv
source .venv/Scripts/Activate  # On Windows use: .venv\Scripts\Activate

### 2. Install Dependencies
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt

### 3. Configure Environment Variables
Create a .env file in the backend directory based on .env.example:
OLLAMA_MODEL=llama3.2:3b
CHROMA_DB_DIR=chroma_db

---

## 🏃‍♂️ Running the Application

### Step 1: Start the Backend (FastAPI)
uvicorn backend.app.main:app --reload --port 8000
(The backend API will be live at http://localhost:8000)

### Step 2: Start the Frontend (Streamlit)
Open a new terminal, activate your virtual environment, and run:
streamlit run frontend/app.py
(The UI will automatically open in your browser at http://localhost:8501)

---

## 🧪 Running Tests
To verify the backend functionality and execute unit tests:
pytest