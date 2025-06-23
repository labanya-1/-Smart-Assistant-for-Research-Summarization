# -Smart-Assistant-for-Research-Summarization
🧠 Smart Assistant for Research Summarization An AI-powered assistant that reads PDF/TXT documents, generates auto summaries, answers context-based questions, and challenges users with logic-based questions. Built with Streamlit, Transformers, and Sentence Transformers.


An AI-powered Streamlit web app that helps users **summarize research papers**, **ask document-based questions**, and **generate logical comprehension questions** with feedback. Ideal for researchers, students, and educators!

---

## 🚀 Features

- 📄 **Upload PDF or TXT files**
- ✍️ **Auto-summary** generation of uploaded research content
- 🤖 **Ask Anything** – question-answering based on the document
- 🎯 **Challenge Me** – logic-based question generation + evaluation
- 💬 **Conversation history** and feedback display
- 🧠 Powered by NLP, transformers, and language models

---

## 🔧 Tech Stack

- [Streamlit](https://streamlit.io/)
- Python (3.8+)
- PyMuPDF (`fitz`) – for PDF parsing
- HuggingFace Transformers
- scikit-learn, Torch, NumPy
- Custom logic for Q&A and feedback

---

## 📂 Project Structure
smart_assistant/
├── app.py # Main Streamlit app
├── requirements.txt # Required dependencies
├── utils/
│ ├── pdf_reader.py # Extract text from PDFs
│ ├── summarizer.py # Auto summarization
│ └── qa_engine.py # Q&A, logic Qs, evaluation
└── pages/ # (Optional) Extra pages if multipage


## ▶️ Run Locally

1. Clone the repository:

   git clone https://github.com/labanya-1/-Smart-Assistant-for-Research-Summarization.git
   cd -Smart-Assistant-for-Research-Summarization
   Create and activate a virtual environment (optional but recommended):
   
 2.Create and activate a virtual environment (optional but recommended):
 python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows

3. Install dependencies:
   pip install -r requirements.txt

4.Run the app:
streamlit run app.py


loom demo walkthrough

https://www.loom.com/share/f6cbc8fcd1ef491182acd866794b0d0e?sid=ec712010-465a-4300-b0a9-e14da287d640


👩‍💻 Author
Built by Labanya Roy 


