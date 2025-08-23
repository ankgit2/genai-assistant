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





#  images
<img width="1919" height="1018" alt="Screenshot 2025-07-06 161735" src="https://github.com/user-attachments/assets/4538c6b2-0bab-4f01-92b4-68dcbf64e0d0" />
<img width="1919" height="1041" alt="Screenshot 2025-07-06 153229" src="https://github.com/user-attachments/assets/cd26a33c-ba83-4f93-8516-990199d48d0e" />
<img width="1900" height="976" alt="Screenshot 2025-07-06 152917" src="https://github.com/user-attachments/assets/66e4b624-3fed-4abc-8ded-94d468d695ce" />
<img width="1919" height="531" alt="Screenshot 2025-07-06 132848" src="https://github.com/user-attachments/assets/7a77e531-d301-4193-847a-bd4040b4825c" />
