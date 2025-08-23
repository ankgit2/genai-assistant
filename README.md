# 🧠 GenAI Assistant – Smart Document Summarizer & QA Tool

An AI-powered assistant that reads uploaded documents (PDF/TXT), summarizes them, answers questions contextually, and challenges users with logic-based quizzes — all powered by **Azure OpenAI GPT**.

---

## 📌 Features

- 📄 Upload PDF documents
- ✍️ Auto-summary (≤ 150 words)
- 🤖 Ask Anything: free-form question answering based on document content
- 🧩 Challenge Me: generates  logic-based questions and evaluates user responses
- 📚 Justified responses: each answer includes a reference to where it came from in the document
- 🧠 Memory: remembers previous questions and answers for follow-up context
- 🌐 Fully local web-based UI using Streamlit

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/genai-assistant.git
cd genai-assistant


2. Install Dependencies

pip install -r requirements.txt



3. Setup Environment Variables
Create a .env file with your Azure credentials:

AZURE_OPENAI_API_KEY=your-azure-api-key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-35-turbo

(So,You can refer to .env.example for the format.)


4. Run the App
streamlit run app.py
Then open your browser to http://localhost:8501.


🧠 Application Architecture

[ User Uploads PDF ] 
        ↓
[ Text Extracted (PyPDF2) ]
        ↓
[ Azure GPT (via AzureOpenAI SDK) ]
        ↓
[ Streamlit UI Presents: Summary, QA, Quiz ]


-Frontend/UI: Streamlit

-LLM: Azure OpenAI (gpt-35-turbo)

-PDF Parsing: PyPDF2

-Memory: session_state



🗂️ Project Structure


genai-assistant/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
└── utils/
    ├── summarizer.py
    ├── qa_engine.py
    └── document_parser.py
```
---



<img width="1919" height="1018" alt="Screenshot 2025-07-06 161735" src="https://github.com/user-attachments/assets/6cb2b9e0-64ea-4e00-9fdd-264b47abfe38" />


---
