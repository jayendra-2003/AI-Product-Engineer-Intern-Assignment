# 🏆 AI-Powered Sports Quiz Generation Agent

## 📌 Project Overview

The **AI-Powered Sports Quiz Generation Agent** is a Retrieval-Augmented Generation (RAG) application that automatically creates engaging, factually accurate multiple-choice sports quizzes for social media and educational platforms.

The system combines:

* 🧠 Large Language Model (LLM)
* 📚 ChromaDB Vector Database
* 🌐 Web Search
* 🔍 Retrieval-Augmented Generation (RAG)

to generate unique quizzes while minimizing hallucinations by grounding responses in retrieved knowledge.

---

## ✨ Features

* Select a sport (Cricket, Football, Tennis, Basketball, Badminton, etc.)
* Choose quiz difficulty (Easy, Medium, Hard)
* Generate 5 multiple-choice quiz questions
* Regenerate fresh quizzes
* Uses ChromaDB for semantic knowledge retrieval
* Uses web search to fetch recent sports information
* Provides:

  * Four answer options
  * Correct answer
  * Short explanation

---

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* OpenAI GPT
* OpenAI Embeddings
* ChromaDB
* Tavily Search API
* python-dotenv

---

## 📂 Project Structure

```text
sports-quiz-agent/
│
├── app.py
├── config.py
├── generator.py
├── retriever.py
├── web_search.py
├── ingest.py
│
├── data/
│   ├── cricket.txt
│   ├── football.txt
│   ├── tennis.txt
│   ├── badminton.txt
│   └── basketball.txt
│
├── chroma_db/
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sports-quiz-agent.git

cd sports-quiz-agent
```

---

### 2. Create a virtual environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key

TAVILY_API_KEY=your_tavily_api_key
```

---

## 📚 Preparing the Knowledge Base

Add sports knowledge files inside the `data/` folder.

Example:

```
data/
    cricket.txt
    football.txt
    tennis.txt
    badminton.txt
    basketball.txt
```

Run the ingestion script to create the ChromaDB vector database.

```bash
python ingest.py
```

---

## ▶️ Running the Application

Start the Streamlit dashboard.

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🚀 How It Works

### Step 1

User selects

* Sport
* Difficulty Level

↓

### Step 2

Retriever searches ChromaDB

↓

### Step 3

Web Search fetches recent sports information

↓

### Step 4

Both contexts are combined

↓

### Step 5

The LLM generates a fresh sports quiz

↓

### Step 6

The application displays

* 5 Questions
* 4 Options
* Correct Answer
* Explanation

---

## 🧠 RAG Pipeline

```
Sports Documents
        │
        ▼
     ingest.py
        │
        ▼
     ChromaDB
        │
        ▼
   retriever.py
        │
        ├──────────────┐
        ▼              │
 Retrieved Context     │
                       │
                 web_search.py
                       │
                Latest Sports Info
                       │
                       ▼
               Prompt Construction
                       │
                       ▼
              OpenAI Language Model
                       │
                       ▼
              Generated Sports Quiz
```

---

## 📸 Dashboard Features

* Sport Selection
* Difficulty Selection
* Generate Quiz
* Regenerate Quiz
* Multiple Choice Questions
* Correct Answers
* Explanations

---

## 🎯 Sample Output

**Sport:** Cricket

**Difficulty:** Medium

**Question 1**

Who captained India to victory in the 2011 ICC Cricket World Cup?

A. Virat Kohli

B. MS Dhoni

C. Rohit Sharma

D. Sourav Ganguly

**Correct Answer**

B. MS Dhoni

**Explanation**

MS Dhoni led India to victory in the 2011 ICC Cricket World Cup and hit the winning six in the final against Sri Lanka.

---

## 📈 Future Enhancements

* User authentication
* Score tracking
* Timed quizzes
* AI-generated sports images
* Multiplayer quiz mode
* Voice-based quiz interaction
* Support for additional sports
* Export quizzes as PDF or social media posts

---

## 👨‍💻 Author

**Jayendra Dakarapu**

Backend Developer | Java | Spring Boot | AI & RAG Enthusiast

---

## 📄 License

This project is developed for educational and demonstration purposes.
