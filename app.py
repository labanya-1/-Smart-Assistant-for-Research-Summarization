


# app.py

# import streamlit as st
# from utils.pdf_reader import extract_text_from_pdf
# from utils.summarizer import summarize_text
# from utils.qa_engine import ask_question_from_doc, generate_logic_questions, evaluate_user_answer

# # -------------- Streamlit Page Config --------------
# st.set_page_config(page_title="Smart Research Assistant", layout="wide")
# st.title("📄 Smart Assistant for Research Summarization")

# # -------------- Utility Functions --------------
# @st.cache_data
# def get_summary(text):
#     return summarize_text(text)

# @st.cache_data
# def get_logic_questions(text):
#     return generate_logic_questions(text)

# def trim_summary(summary, max_words=150):
#     words = summary.split()
#     return " ".join(words[:max_words]) + "..." if len(words) > max_words else summary

# def safe_percent(val):
#     try:
#         return f"{float(val):.2f}%"
#     except:
#         return "N/A"

# def display_summary():
#     trimmed = trim_summary(st.session_state.summary)
#     with st.expander("📌 Auto Summary", expanded=True):
#         st.info(trimmed)
#         st.caption(f"📝 Word Count: {len(trimmed.split())}/150")
#         st.download_button(
#             label="💾 Download Summary",
#             data=trimmed,
#             file_name="summary.txt",
#             mime="text/plain"
#         )

# def handle_ask_mode(raw_text):
#     st.subheader("❓ Ask Anything")
#     user_question = st.text_input("Ask a question based on the document")

#     if user_question:
#         with st.spinner("Finding the answer..."):
#             answer = ask_question_from_doc(user_question, raw_text)

#         if isinstance(answer, dict):
#             st.markdown(f"""
#             ✅ **Answer:** {answer.get('answer', 'N/A')}  
#             🔢 **Confidence:** {safe_percent(answer.get('confidence'))}  
#             📖 **Justification:** {answer.get('justification', 'N/A')}  
#             🔍 **Justification Score:** {safe_percent(answer.get('justification_score'))}
#             """)
#         else:
#             st.warning("Could not find a confident answer.")

# def handle_challenge_mode(raw_text):
#     st.subheader("🧠 Challenge Yourself!")
#     st.markdown("Click the button to generate logic-based questions from your document.")

#     if st.button("🎲 Generate Questions") or st.button("🔄 Regenerate Questions"):
#         with st.spinner("⚙️ Generating questions..."):
#             st.session_state.questions = get_logic_questions(raw_text)

#     if "questions" in st.session_state and st.session_state.questions:
#         with st.form("challenge_form"):
#             responses = {}
#             for i, q in enumerate(st.session_state.questions):
#                 st.markdown(f"**Q{i+1}: {q}**")
#                 responses[q] = st.text_input("Your answer", key=f"user_ans_{i}")
#             submitted = st.form_submit_button("✅ Submit Answers")

#         if submitted:
#             st.subheader("🧾 Feedback")
#             for q, user_ans in responses.items():
#                 if user_ans.strip():
#                     with st.spinner("🔍 Evaluating..."):
#                         feedback = evaluate_user_answer(raw_text, q, user_ans)
#                     if "Correct" in feedback:
#                         st.success(f"**{q}**\n\n✅ {feedback}")
#                     else:
#                         st.warning(f"**{q}**\n\n⚠️ {feedback}")

# # -------------- File Upload & Processing --------------
# uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

# if uploaded_file:
#     if (
#         "uploaded_file_name" not in st.session_state
#         or st.session_state.uploaded_file_name != uploaded_file.name
#     ):
#         st.session_state.raw_text = None
#         st.session_state.summary = None
#         st.session_state.questions = None
#         st.session_state.qa_history = []
#         st.session_state.uploaded_file_name = uploaded_file.name

#     st.success(f"Uploaded: {uploaded_file.name}")
#     file_type = uploaded_file.type

#     if st.session_state.raw_text is None:
#         try:
#             if file_type == "application/pdf":
#                 st.session_state.raw_text = extract_text_from_pdf(uploaded_file)
#             elif file_type == "text/plain":
#                 st.session_state.raw_text = uploaded_file.read().decode("utf-8")
#             else:
#                 st.error("Unsupported file type.")
#                 st.stop()
#         except Exception as e:
#             st.error(f"Error reading file: {e}")
#             st.stop()

#     raw_text = st.session_state.raw_text

#     if st.session_state.summary is None:
#         with st.spinner("Generating summary..."):
#             st.session_state.summary = get_summary(raw_text)

#     display_summary()

#     mode = st.radio("Choose interaction mode", ["Ask Anything", "Challenge Me"])

#     if mode == "Ask Anything":
#         handle_ask_mode(raw_text)
#     elif mode == "Challenge Me":
#         handle_challenge_mode(raw_text)

# else:
#     st.info("📥 Please upload a PDF or TXT file to get started.")

# # -------------- Footer --------------
# st.markdown("<hr><center><small>🚀 Made with ❤️ by Labanya Roy </small></center>", unsafe_allow_html=True)



import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.summarizer import summarize_text
from utils.qa_engine import ask_question_from_doc, generate_logic_questions, evaluate_user_answer

# -------------- Streamlit Page Config --------------
st.set_page_config(page_title="Smart Research Assistant", layout="wide")
st.title("📄 Smart Assistant for Research Summarization")

# -------------- Utility Functions --------------
@st.cache_data
def get_summary(text):
    return summarize_text(text)

@st.cache_data
def get_logic_questions(text):
    return generate_logic_questions(text)

def trim_summary(summary, max_words=150):
    words = summary.split()
    return " ".join(words[:max_words]) + "..." if len(words) > max_words else summary

def safe_percent(val):
    try:
        return f"{float(val):.2f}%"
    except:
        return "N/A"

def display_summary():
    trimmed = trim_summary(st.session_state.summary)
    with st.expander("📌 Auto Summary", expanded=True):
        st.info(trimmed)
        st.caption(f"📝 Word Count: {len(trimmed.split())}/150")
        st.download_button(
            label="💾 Download Summary",
            data=trimmed,
            file_name="summary.txt",
            mime="text/plain"
        )

def handle_ask_mode(raw_text):
    st.subheader("❓ Ask Anything")

    if "qa_history" not in st.session_state:
        st.session_state.qa_history = []

    user_question = st.text_input("Ask a question based on the document", key="question_input")

    if user_question:
        with st.spinner("Finding the answer..."):
            answer = ask_question_from_doc(user_question, raw_text)

        if isinstance(answer, dict):
            qna_entry = {
                "question": user_question,
                "answer": answer.get("answer", "N/A"),
                "justification": answer.get("justification", ""),
                "confidence": safe_percent(answer.get("confidence")),
                "justification_score": safe_percent(answer.get("justification_score")),
            }
            st.session_state.qa_history.append(qna_entry)

            st.markdown(f"✅ **Answer:** {qna_entry['answer']}")
            if qna_entry["justification"].strip() and qna_entry["justification"] != qna_entry["answer"]:
                st.markdown(f"📖 **Justification:** {qna_entry['justification']}")
            st.markdown(f"🔢 **Confidence:** {qna_entry['confidence']}")
            st.markdown(f"🔍 **Justification Score:** {qna_entry['justification_score']}")
        else:
            st.warning("Could not find a confident answer.")

    if st.session_state.qa_history:
        with st.expander("🕘 Previous Questions", expanded=False):
            for idx, qa in enumerate(reversed(st.session_state.qa_history)):
                st.markdown(f"**Q{len(st.session_state.qa_history) - idx}: {qa['question']}**")
                st.markdown(f"- ✅ **Answer:** {qa['answer']}")
                st.markdown(f"- 🔢 **Confidence:** {qa['confidence']}")
                st.markdown(f"- 📖 **Justification:** {qa['justification']}")
                st.markdown(f"- 🔍 **Justification Score:** {qa['justification_score']}")
                st.markdown("---")
            if st.button("🧹 Clear History"):
                st.session_state.qa_history = []
                st.rerun()

def handle_challenge_mode(raw_text):
    st.subheader("🧠 Challenge Yourself!")
    st.markdown("Click the button to generate logic-based questions from your document.")

    if st.button("🎲 Generate Questions"):
        with st.spinner("⚙️ Generating questions..."):
            st.session_state.questions = get_logic_questions(raw_text)

    if "questions" in st.session_state and st.session_state.questions:
        with st.form("challenge_form"):
            responses = {}
            for i, q in enumerate(st.session_state.questions):
                st.markdown(f"**Q{i+1}: {q}**")
                responses[q] = st.text_input("Your answer", key=f"user_ans_{i}")
            submitted = st.form_submit_button("✅ Submit Answers")

        if submitted:
            st.subheader("🧾 Feedback")
            for q, user_ans in responses.items():
                if user_ans.strip():
                    with st.spinner("🔍 Evaluating..."):
                        feedback = evaluate_user_answer(raw_text, q, user_ans)
                    if "Correct" in feedback:
                        st.success(f"**{q}**\n\n✅ {feedback}")
                    else:
                        st.warning(f"**{q}**\n\n⚠️ {feedback}")

# -------------- File Upload & Processing --------------
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    if (
        "uploaded_file_name" not in st.session_state
        or st.session_state.uploaded_file_name != uploaded_file.name
    ):
        st.session_state.raw_text = None
        st.session_state.summary = None
        st.session_state.questions = None
        st.session_state.qa_history = []
        st.session_state.uploaded_file_name = uploaded_file.name

    st.success(f"Uploaded: {uploaded_file.name}")
    file_type = uploaded_file.type

    if st.session_state.raw_text is None:
        try:
            if file_type == "application/pdf":
                st.session_state.raw_text = extract_text_from_pdf(uploaded_file)
            elif file_type == "text/plain":
                st.session_state.raw_text = uploaded_file.read().decode("utf-8")
            else:
                st.error("Unsupported file type.")
                st.stop()
        except Exception as e:
            st.error(f"Error reading file: {e}")
            st.stop()

    raw_text = st.session_state.raw_text

    if st.session_state.summary is None:
        with st.spinner("Generating summary..."):
            st.session_state.summary = get_summary(raw_text)

    display_summary()

    mode = st.radio("Choose interaction mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        handle_ask_mode(raw_text)
    elif mode == "Challenge Me":
        handle_challenge_mode(raw_text)

else:
    st.info("📥 Please upload a PDF or TXT file to get started.")

# -------------- Footer --------------
st.markdown("<hr><center><small>🚀 Made with ❤️ by Labanya Roy </small></center>", unsafe_allow_html=True)
