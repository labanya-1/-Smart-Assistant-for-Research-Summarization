# utils/qa_engine.py

from transformers import pipeline

# Load QA model
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def ask_question_from_doc(question, context):
    result = qa_pipeline(question=question, context=context)
    answer = result['answer']
    score = result['score']
    return f"**Answer:** {answer}\n\n**Confidence:** {round(score * 100, 2)}%"

def generate_logic_questions(document_text):
    questions = [
        "What is the main idea of the document?",
        "What problem is the research trying to solve?",
        "What is the conclusion or result mentioned?"
    ]
    return questions

from difflib import SequenceMatcher

def evaluate_user_answer(document_text, question, user_answer):
    correct_answers = {
        "What is the main idea of the document?": "The impact of sleep on cognitive performance",
        "What problem is the research trying to solve?": "Negative impact of poor sleep on students’ GPA, memory, and focus",
        "What is the conclusion or result mentioned?": "There is a strong correlation between longer, quality sleep and higher GPA"
    }

    user_answer = user_answer.strip().lower()
    expected = correct_answers.get(question, "").lower()
    similarity = SequenceMatcher(None, user_answer, expected).ratio()

    if similarity > 0.6:
        return "✅ Correct! Your answer aligns with the document."
    else:
        return f"❌ Not quite. Expected something like: '{expected}'. Try reading that section again."
