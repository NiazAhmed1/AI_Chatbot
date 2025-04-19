## AI Chatbot with FastAPI + Next.js + Groq (Gemma2-9b-it)

This is a full-stack AI chatbot project using **FastAPI** for the backend and **Next.js** for the frontend. It leverages the **Groq API** with the `gemma2-9b-it` model to generate intelligent responses to user queries.

---

## 📁 Project Structure

AI-Chatbot-Project/ │ ├── backend/ │ ├── main.py # FastAPI server logic │ ├── .env # Contains GROQ_API_KEY (not committed) │ ├── requirements.txt # Backend dependencies │ ├── frontend/ │ └── ... # Next.js chatbot UI │ └── demo.mp4 # Demo video of the chatbot in action

---

## 🚀 Features

- 💬 Real-time AI chat interface
- ⚡ FastAPI backend with Groq's `gemma2-9b-it` model
- 🌐 Next.js frontend for interactive user experience
- 🔐 Secure `.env` configuration for API keys
- 🎥 Demo video included

---

## 🛠 Tech Stack

- **Frontend:** Next.js, React, Tailwind CSS
- **Backend:** FastAPI (Python)
- **Model:** Groq `gemma2-9b-it`
- **API Integration:** Groq API

# ⚙️ Backend Setup Instructions

### 1. Navigate to the Backend Directory

```bash
cd backend
```

### 2. Install dependencies

It's recommended to use a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up the .env file

Add your Groq API key in .env file:

```bash
API_KEY = your_groq_api_key_here
```

### 4. Run the FastAPI server

```bash
python main.py
```

# 💻 Frontend Setup (Next.js)

### 1. Navigate to the Frontend Directory

```bash
cd frontend
```

### 2. Install dependencies

```bash
npm install
```

### 3. Run the Next.js development server

```bash
npm run dev
```

The app will be available at http://localhost:3000

## 📽 Demo

A quick preview of the chatbot in action is included in [`demo.mp4`](./demo.mp4)

## 📌 Notes

- The backend sends the user query to the Groq model and returns the model's response.
- Ensure the FastAPI backend is running before interacting with the frontend.
- Keep your `.env` file private and never commit it to version control.
