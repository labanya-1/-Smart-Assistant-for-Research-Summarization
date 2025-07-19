
# from transformers import pipeline
# from sentence_transformers import SentenceTransformer, util

# # Load models
# qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
# semantic_model = SentenceTransformer("all-MiniLM-L6-v2")


# # 🔍 Answering logic with justification
# def ask_question_from_doc(question, context):
#     result = qa_pipeline(question=question, context=context)
#     answer = result["answer"]
#     score = result["score"]

#     # Get justification sentence + score
#     justification, justification_score = get_justification_snippet(answer, context)

#     return (
#         f"**Answer:** {answer}\n\n"
#         f"**Confidence:** {round(score * 100, 2)}%\n\n"
#         f"📌 **Based on:** _{justification}_\n"
#         f"🔍 **Justification Score:** {round(justification_score * 100, 2)}%"
#     )


# # ✨ Helper: Find best matching sentence with highlighting
# def get_justification_snippet(answer, context):
#     sentences = context.split(".")
#     answer_emb = semantic_model.encode(answer, convert_to_tensor=True)

#     best_score = 0
#     best_sent = ""

#     for sent in sentences:
#         sent = sent.strip()
#         if sent:
#             sent_emb = semantic_model.encode(sent, convert_to_tensor=True)
#             score = util.pytorch_cos_sim(answer_emb, sent_emb).item()
#             if score > best_score:
#                 best_score = score
#                 best_sent = sent

#     # Highlight the answer if possible
#     if answer.lower() in best_sent.lower():
#         start = best_sent.lower().find(answer.lower())
#         end = start + len(answer)
#         highlighted = best_sent[:start] + f"**{best_sent[start:end]}**" + best_sent[end:]
#     else:
#         highlighted = best_sent

#     return highlighted if highlighted else "No exact supporting sentence found.", best_score


# # 🧠 Challenge Mode Questions
# def generate_logic_questions(document_text):
#     return [
#         "What is the main idea of the document?",
#         "What problem is the research trying to solve?",
#         "What is the conclusion or result mentioned?"
#     ]


# # 🧠 Evaluate User Answer Semantically
# def evaluate_user_answer(document_text, question, user_answer):
#     correct_answers = {
#         "What is the main idea of the document?": "The impact of sleep on cognitive performance",
#         "What problem is the research trying to solve?": "Negative impact of poor sleep on students’ GPA, memory, and focus",
#         "What is the conclusion or result mentioned?": "There is a strong correlation between longer, quality sleep and higher GPA"
#     }

#     expected = correct_answers.get(question, "")
#     if not expected:
#         return f"❌ No reference answer found for this question."

#     # Semantic similarity
#     embedding1 = semantic_model.encode(expected, convert_to_tensor=True)
#     embedding2 = semantic_model.encode(user_answer, convert_to_tensor=True)
#     similarity = util.pytorch_cos_sim(embedding1, embedding2).item()

#     if similarity > 0.7:
#         return "✅ Correct! Your answer aligns with the document."
#     else:
#         return f"❌ Not quite. Expected something like: '{expected}'. Try reading that section again."












# from transformers import pipeline
# from sentence_transformers import SentenceTransformer, util

# # Load models
# qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
# semantic_model = SentenceTransformer("all-MiniLM-L6-v2")

# # 🔍 Answering logic with justification
# def ask_question_from_doc(question, context):
#     result = qa_pipeline(question=question, context=context)
#     answer = result["answer"]
#     score = result["score"]

#     # Use full sentence if answer is too short
#     if len(answer.split()) < 4:
#         answer = get_justification_snippet(answer, context)[0]

#     # Get justification sentence + score
#     justification, justification_score = get_justification_snippet(answer, context)

#     return (
#         f"\n\n\U0001F4D0 **Question:** {question}\n"
#         f"\u2705 **Answer:** {answer}\n"
#         f"🔹 **Confidence:** {round(score * 100, 2)}%\n"
#         f"📖 **Justification:** {justification}\n"
#         f"🔍 **Justification Score:** {round(justification_score * 100, 2)}%"
#     )


# # ✨ Helper: Find best matching sentence with highlighting
# def get_justification_snippet(answer, context):
#     sentences = context.split(".")
#     answer_emb = semantic_model.encode(answer, convert_to_tensor=True)

#     best_score = 0
#     best_sent = ""

#     for sent in sentences:
#         sent = sent.strip()
#         if sent:
#             sent_emb = semantic_model.encode(sent, convert_to_tensor=True)
#             score = util.pytorch_cos_sim(answer_emb, sent_emb).item()
#             if score > best_score:
#                 best_score = score
#                 best_sent = sent

#     # Highlight the answer if possible
#     if answer.lower() in best_sent.lower():
#         start = best_sent.lower().find(answer.lower())
#         end = start + len(answer)
#         highlighted = best_sent[:start] + f"**{best_sent[start:end]}**" + best_sent[end:]
#     else:
#         highlighted = best_sent

#     return highlighted if highlighted else "No exact supporting sentence found.", best_score


# # 🧠 Logic-based questions
# def generate_logic_questions(document_text):
#     return [
#         "What is the main idea of the document?",
#         "What problems is the article discussing?",
#         "How is AI helping across different industries?",
#         "What are some challenges or ethical issues with AI?",
#         "What is the conclusion or future outlook on AI?"
#     ]


# # 🧠 Answer Evaluation

# def evaluate_user_answer(context, question, user_answer):
#     ref_answer = qa_pipeline(question=question, context=context)["answer"]

#     emb1 = semantic_model.encode(ref_answer, convert_to_tensor=True)
#     emb2 = semantic_model.encode(user_answer, convert_to_tensor=True)
#     similarity = util.pytorch_cos_sim(emb1, emb2).item()

#     if similarity > 0.7:
#         return "✅ Correct! Your answer aligns with the document."
#     else:
#         return f"❌ Not quite. Expected something like: '{ref_answer}'. Try reading that section again."





# # utils/qa_engine.py
# from transformers import pipeline
# import re

# # Load QnA model
# qa_pipeline = pipeline("question-answering")

# # Answer from context
# def ask_question_from_doc(question, context):
#     result = qa_pipeline(question=question, context=context)
#     answer = result["answer"]
#     score = result["score"]

#     justification, justification_score = get_justification_snippet(answer, context)

#     return (
#         f"Question: {question}\n"
#         f"Answer: {answer}\n"
#         f"Confidence: {round(score * 100, 2)}%\n"
#         f"Justification: {justification}\n"
#         f"Justification Score: {round(justification_score * 100, 2)}%"
#     )

# # Extract justification

# def get_justification_snippet(answer, context):
#     sentences = re.split(r'(?<=[.!?]) +', context)
#     best_sentence = ""
#     best_score = 0

#     for sentence in sentences:
#         match_score = sum(1 for word in answer.lower().split() if word in sentence.lower())
#         if match_score > best_score:
#             best_score = match_score
#             best_sentence = sentence

#     justification_score = best_score / len(answer.split()) if answer else 0
#     return best_sentence, justification_score

# # Dummy implementations for now
# def generate_logic_questions(text):
#     return [
#         "What is the main topic discussed in the document?",
#         "Mention one benefit of the technology described?"
#     ]

# def evaluate_user_answer(context, question, user_answer):
#     # Simple evaluation: does the answer appear in context?
#     if user_answer.lower() in context.lower():
#         return "Correct answer."
#     return "Try again. Your answer seems unrelated to the document."

# # For standalone test
# if __name__ == "__main__":
#     question = "How is AI used in healthcare?"
#     context = "In healthcare, AI helps doctors analyze images, predict outcomes, and assist in surgeries."
#     print(ask_question_from_doc(question, context))





# def ask_question_from_doc(question, context):
#     if "creative" in question.lower():
#         return {
#             "question": question,
#             "answer": "It can generate music, write poetry, and assist in graphic design — blending human creativity with machine precision.",
#             "confidence": 78.64,
#             "justification": "It can generate music, write poetry, and assist in graphic design — blending human creativity with machine precision.",
#             "justification_score": 100.0
#         }
#     else:
#         return {
#             "question": question,
#             "answer": "Answer not found in document.",
#             "confidence": 0.0,
#             "justification": "Not enough context to answer the question.",
#             "justification_score": 0.0
#         }


# def generate_logic_questions(context):
#     return [
#         "How is AI transforming creative fields like music, design, or writing?",
#         "What are some ethical challenges associated with AI?"
#     ]


# def evaluate_user_answer(context, question, user_answer):
#     if "creativity" in user_answer.lower() or "design" in user_answer.lower():
#         return "Your answer is correct."
#     else:
#         return "Your answer needs more detail related to the context."


# # utils/pdf_reader.py

# def extract_text_from_pdf(uploaded_file):
#     import PyPDF2
#     reader = PyPDF2.PdfReader(uploaded_file)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text()
#     return text


# # utils/summarizer.py

# def summarize_text(text):
#     # Simulated summary function
#     words = text.split()
#     summary = " ".join(words[:150])  # Trim to 150 words max
#     return summary



# import nltk
# from transformers import pipeline
# from sentence_transformers import SentenceTransformer, util

# nltk.download('punkt')

# # Load models once
# qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
# semantic_model = SentenceTransformer("all-MiniLM-L6-v2")

# def chunk_text(text, max_tokens=450):
#     sentences = nltk.sent_tokenize(text)
#     chunks = []
#     current_chunk = ""

#     for sent in sentences:
#         if len((current_chunk + " " + sent).split()) <= max_tokens:
#             current_chunk += " " + sent
#         else:
#             chunks.append(current_chunk.strip())
#             current_chunk = sent
#     if current_chunk:
#         chunks.append(current_chunk.strip())
#     return chunks

# def ask_question_from_doc(question, context):
#     try:
#         chunks = chunk_text(context)
#         best_answer = None
#         best_score = 0

#         for chunk in chunks:
#             result = qa_pipeline(question=question, context=chunk)
#             if result["score"] > best_score:
#                 best_answer = result["answer"]
#                 best_score = result["score"]

#         if best_answer is None:
#             return {
#                 "answer": "",
#                 "confidence": 0,
#                 "justification": "No answer found.",
#                 "justification_score": 0
#             }

#         # For now, justification = best_answer (you can improve later)
#         return {
#             "answer": best_answer,
#             "confidence": round(best_score * 100, 2),
#             "justification": best_answer,
#             "justification_score": round(best_score * 100, 2),
#         }
#     except Exception as e:
#         return {
#             "answer": "",
#             "confidence": 0,
#             "justification": f"Error: {str(e)}",
#             "justification_score": 0,
#         }

# def generate_logic_questions(context):
#     return [
#         "What is the main idea of the document?",
#         "What key problem does this research try to solve?",
#         "What conclusion or finding does the document present?",
#     ]

# def evaluate_user_answer(reference_text, question, user_answer):
#     expected_answer_dict = ask_question_from_doc(question, reference_text)
#     if not expected_answer_dict or not expected_answer_dict["answer"]:
#         return "⚠️ Cannot evaluate answer because no reference answer was found."

#     expected_text = expected_answer_dict["answer"]

#     emb_expected = semantic_model.encode(expected_text, convert_to_tensor=True)
#     emb_user = semantic_model.encode(user_answer, convert_to_tensor=True)
#     similarity = util.pytorch_cos_sim(emb_expected, emb_user).item()

#     if similarity > 0.7:
#         return "✅ Correct! Your answer matches well."
#     else:
#         return f"❌ Not quite. Expected something like: '{expected_text}'"

# if __name__ == "__main__":
#     sample_context = """
#     Artificial Intelligence (AI) is used widely in daily life—from smart assistants like Alexa to healthcare innovations. It helps in automating tasks, improving efficiency, and supporting decision-making in sectors like education, finance, and transport.
#     """
#     question = "How is AI used in daily life?"
#     answer = ask_question_from_doc(question, sample_context)
#     print(answer)




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
