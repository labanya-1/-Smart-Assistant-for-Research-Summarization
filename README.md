# 🧠 Smart Assistant for Research Summarization

An AI-powered assistant that reads PDF/TXT documents, generates intelligent summaries, answers contextual questions, and challenges users with logic-based comprehension — all through an intuitive Streamlit interface.

Built with 🔥 Streamlit, 🤗 HuggingFace Transformers, and ⚙️ Sentence Transformers, this project is designed for **researchers, students, and educators** looking to extract insights quickly and interactively.

---

## 🚀 Features

- 📄 Upload and parse **PDF or TXT files**
- ✍️ Generate **automated summaries** of lengthy research documents
- 🤖 Ask **document-based natural language questions**
- 🧠 "Challenge Me" mode with **logic-driven Q&A + evaluation**
- 💬 View **conversation history** with answer confidence and justification
- 🔍 Get **semantic feedback** using sentence-level similarity scoring

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – for the interactive UI
- [HuggingFace Transformers](https://huggingface.co/) – summarization and Q&A
- [SentenceTransformers](https://www.sbert.net/) – for semantic similarity & justification
- PyMuPDF (`fitz`) – PDF text extraction
- Python (3.8+), NLTK, scikit-learn, Torch, NumPy

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

https://www.loom.com/share/ea871fffa88546e2a520e25ae6fd617d?sid=e0030a5e-4ad7-46c6-b38f-509d352f994f



💡 Future Possibilities
This prototype can be extended to support:

Operational SOP document summarization

Context-aware onboarding tools

Knowledge assistants for facility teams, educators, or compliance analysts


👩‍💻 Author
Built by Labanya Roy 


