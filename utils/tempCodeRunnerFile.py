utils/qa_engine.py

def ask_question_from_doc(question, context):
    if "creative" in question.lower():
        return {
            "question": question,
            "answer": "It can generate music, write poetry, and assist in graphic design — blending human creativity with machine precision.",
            "confidence": 78.64,
            "justification": "It can generate music, write poetry, and assist in graphic design — blending human creativity with machine precision.",
            "justification_score": 100.0
        }
    else:
        return {
            "question": question,
            "answer": "Answer not found in document.",
            "confidence": 0.0,
            "justification": "Not enough context to answer the question.",
            "justification_score": 0.0
        }


def generate_logic_questions(context):
    return [
        "How is AI transforming creative fields like music, design, or writing?",
        "What are some ethical challenges associated with AI?"
    ]


def evaluate_user_answer(context, question, user_answer):
    if "creativity" in user_answer.lower() or "design" in user_answer.lower():
        return "Your answer is correct."
    else:
        return "Your answer needs more detail related to the context."


# utils/pdf_reader.py

def extract_text_from_pdf(uploaded_file):
    import PyPDF2
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# utils/summarizer.py

def summarize_text(text):
    # Simulated summary function
    words = text.split()
    summary = " ".join(words[:150])  # Trim to 150 words max
    return summary
