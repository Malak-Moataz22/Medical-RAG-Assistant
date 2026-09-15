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
## 📸 Application Screenshots

Here are some examples of the Medical RAG Assistant interface in action, demonstrating both valid medical document querying and proper handling of out-of-domain queries:

### 1. Medical Query (Happy Path)

* **Description:** The assistant accurately retrieves relevant medical information from the indexed documents and provides a grounded answer along with its source citations.
* **Screenshot:**
* EXAMPLE1
* <img width="1600" height="863" alt="image" src="https://github.com/user-attachments/assets/44037283-9d59-4f27-933a-704858a6d74c" />
*<img width="1600" height="859" alt="image" src="https://github.com/user-attachments/assets/a112a966-5e48-4194-9577-735c4afbdd7f" />

*EXAMPLE2
*<img width="1600" height="852" alt="image" src="https://github.com/user-attachments/assets/b500a994-2190-400a-af17-dedbc6266c0a" />
*<img width="1600" height="862" alt="image" src="https://github.com/user-attachments/assets/e8767c12-ca8d-4044-9abc-a352c932fec5" />
<img width="1600" height="862" alt="image" src="https://github.com/user-attachments/assets/2da5c1bf-0b1f-4bd9-aaee-7504ddd3cee9" />

### 2. General Query Handling (Out-of-Domain)

* **Description:** Demonstrates how the assistant safely handles non-medical questions, avoiding hallucinations and staying true to its specialized scope.
* **Screenshot:**
* <img width="1600" height="858" alt="image" src="https://github.com/user-attachments/assets/8431e11f-de2c-4fed-a7d3-718051ad0b84" />
