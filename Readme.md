#  Code Explainer AI (Web App)

##  Overview
Code Explainer AI is a web-based application that helps users understand programming code easily.  
Users can paste any code snippet, and the system generates a clear explanation using AI.

---

##  Features
-  Explains code in simple language
-  Line-by-line explanation
-  Beginner-friendly summary
-  Web-based interface (Flask)
-  Fast AI responses using Groq API

---

##  Problem Statement
Many beginners struggle to understand programming code due to complex syntax and lack of clear explanations.  
This project aims to simplify code understanding using AI.

---

##  Solution
This application allows users to input code and receive:
- What the code does  
- Step-by-step explanation  
- Easy summary  

---

##  Tech Stack
- Python  
- Flask  
- Groq API (LLaMA model)  
- HTML, CSS  

---

## 🔑 API Key Setup

This project requires a Groq API key to run.

### Steps:
1. Get your API key from Groq
2. Set it as an environment variable

**Windows:**
set GROQ_API_KEY=your_api_key_here
**Mac/Linux:**
export GROQ_API_KEY=your_api_key_here
3. Run the project


## PROJECT STEUCTURE
code-explainer-ai/
│
│── app.py                  # Backend (Flask + Groq API)
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
│── .gitignore              # Ignore sensitive & unwanted files
│── PROJECT_REPORT.pdf      # Your final report
│── .env.example            # Example for API key setup
│
├── templates/
│     └── index.html        # Frontend HTML
│
├── static/
│     └── style.css         # Styling file
│
└── screenshots/            # (Optional but recommended)
      ├── homepage.png
      ├── input.png
      └── output.png