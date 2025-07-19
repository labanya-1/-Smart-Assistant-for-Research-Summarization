
import nltk
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util

nltk.download('punkt')

# Load models once
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
semantic_model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text, max_tokens=450):
    sentences = nltk.sent_tokenize(text)
    chunks = []
    current_chunk = ""

    for sent in sentences:
        if len((current_chunk + " " + sent).split()) <= max_tokens:
            current_chunk += " " + sent
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sent
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def get_sentence_containing_answer(answer, context):
    sentences = nltk.sent_tokenize(context)
    answer_lower = answer.lower()
    for sent in sentences:
        if answer_lower in sent.lower():
            return sent
    # fallback to answer if no sentence found
    return answer

def ask_question_from_doc(question, context):
    try:
        chunks = chunk_text(context)
        best_answer = None
        best_score = 0
        best_chunk = ""

        for chunk in chunks:
            result = qa_pipeline(question=question, context=chunk)
            if result["score"] > best_score:
                best_answer = result["answer"]
                best_score = result["score"]
                best_chunk = chunk

        if best_answer is None:
            return {
                "answer": "",
                "confidence": 0,
                "justification": "No answer found.",
                "justification_score": 0
            }

        expanded_answer = get_sentence_containing_answer(best_answer, best_chunk)

        return {
            "answer": expanded_answer,
            "confidence": round(best_score * 100, 2),
            "justification": expanded_answer,
            "justification_score": round(best_score * 100, 2),
        }
    except Exception as e:
        return {
            "answer": "",
            "confidence": 0,
            "justification": f"Error: {str(e)}",
            "justification_score": 0,
        }

def generate_logic_questions(context):
    return [
        "What is the main idea of the document?",
        "What key problem does this research try to solve?",
        "What conclusion or finding does the document present?",
    ]

def evaluate_user_answer(reference_text, question, user_answer):
    expected_answer_dict = ask_question_from_doc(question, reference_text)
    if not expected_answer_dict or not expected_answer_dict["answer"]:
        return "⚠️ Cannot evaluate answer because no reference answer was found."

    expected_text = expected_answer_dict["answer"]

    emb_expected = semantic_model.encode(expected_text, convert_to_tensor=True)
    emb_user = semantic_model.encode(user_answer, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(emb_expected, emb_user).item()

    if similarity > 0.7:
        return "✅ Correct! Your answer matches well."
    else:
        return f"❌ Not quite. Expected something like: '{expected_text}'"

if __name__ == "__main__":
    sample_context = """
    Artificial Intelligence (AI) is used widely in daily life—from smart assistants like Alexa to healthcare innovations. It helps in automating tasks, improving efficiency, and supporting decision-making in sectors like education, finance, and transport.
    """
    question = "How is AI used in daily life?"
    answer = ask_question_from_doc(question, sample_context)
    print(answer)
