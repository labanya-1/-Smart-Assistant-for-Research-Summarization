
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util

# Load models
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
semantic_model = SentenceTransformer("all-MiniLM-L6-v2")


# 🔍 Answering logic with justification
def ask_question_from_doc(question, context):
    result = qa_pipeline(question=question, context=context)
    answer = result["answer"]
    score = result["score"]

    # Get justification sentence + score
    justification, justification_score = get_justification_snippet(answer, context)

    return (
        f"**Answer:** {answer}\n\n"
        f"**Confidence:** {round(score * 100, 2)}%\n\n"
        f"📌 **Based on:** _{justification}_\n"
        f"🔍 **Justification Score:** {round(justification_score * 100, 2)}%"
    )


# ✨ Helper: Find best matching sentence with highlighting
def get_justification_snippet(answer, context):
    sentences = context.split(".")
    answer_emb = semantic_model.encode(answer, convert_to_tensor=True)

    best_score = 0
    best_sent = ""

    for sent in sentences:
        sent = sent.strip()
        if sent:
            sent_emb = semantic_model.encode(sent, convert_to_tensor=True)
            score = util.pytorch_cos_sim(answer_emb, sent_emb).item()
            if score > best_score:
                best_score = score
                best_sent = sent

    # Highlight the answer if possible
    if answer.lower() in best_sent.lower():
        start = best_sent.lower().find(answer.lower())
        end = start + len(answer)
        highlighted = best_sent[:start] + f"**{best_sent[start:end]}**" + best_sent[end:]
    else:
        highlighted = best_sent

    return highlighted if highlighted else "No exact supporting sentence found.", best_score


# 🧠 Challenge Mode Questions
def generate_logic_questions(document_text):
    return [
        "What is the main idea of the document?",
        "What problem is the research trying to solve?",
        "What is the conclusion or result mentioned?"
    ]


# 🧠 Evaluate User Answer Semantically
def evaluate_user_answer(document_text, question, user_answer):
    correct_answers = {
        "What is the main idea of the document?": "The impact of sleep on cognitive performance",
        "What problem is the research trying to solve?": "Negative impact of poor sleep on students’ GPA, memory, and focus",
        "What is the conclusion or result mentioned?": "There is a strong correlation between longer, quality sleep and higher GPA"
    }

    expected = correct_answers.get(question, "")
    if not expected:
        return f"❌ No reference answer found for this question."

    # Semantic similarity
    embedding1 = semantic_model.encode(expected, convert_to_tensor=True)
    embedding2 = semantic_model.encode(user_answer, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embedding1, embedding2).item()

    if similarity > 0.7:
        return "✅ Correct! Your answer aligns with the document."
    else:
        return f"❌ Not quite. Expected something like: '{expected}'. Try reading that section again."
