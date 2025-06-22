import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.summarizer import summarize_text
from utils.qa_engine import ask_question_from_doc, generate_logic_questions, evaluate_user_answer

st.set_page_config(page_title="Smart Research Assistant", layout="wide")
st.image("https://cdn-icons-png.flaticon.com/512/4712/4712106.png", width=70)
st.title("📄 Smart Assistant for Research Summarization")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    # Clear old states on new upload
    if (
        "uploaded_file_name" not in st.session_state
        or st.session_state.uploaded_file_name != uploaded_file.name
    ):
        st.session_state.raw_text = None
        st.session_state.summary = None
        st.session_state.questions = None
        st.session_state.qa_history = []
        st.session_state.uploaded_file_name = uploaded_file.name

    file_type = uploaded_file.type
    st.success(f"Uploaded: {uploaded_file.name}")

    if st.session_state.raw_text is None:
        if file_type == "application/pdf":
            st.session_state.raw_text = extract_text_from_pdf(uploaded_file)
        elif file_type == "text/plain":
            st.session_state.raw_text = uploaded_file.read().decode("utf-8")
        else:
            st.error("Unsupported file type.")
            st.stop()

    raw_text = st.session_state.raw_text

    if st.session_state.summary is None:
        with st.spinner("Generating summary..."):
            st.session_state.summary = summarize_text(raw_text)

    with st.expander("📌 Auto Summary (click to view)", expanded=True):
        st.info(st.session_state.summary)
        st.caption(f"📝 Word Count: {len(st.session_state.summary.split())}/150")

    mode = st.radio("Choose interaction mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        st.subheader("❓ Ask Anything")
        user_question = st.text_input("Ask a question based on the document")

        if user_question:
            with st.spinner("Finding the answer..."):
                answer = ask_question_from_doc(user_question, raw_text)
                st.session_state.qa_history.append((user_question, answer))
            st.markdown(answer)

        if st.session_state.qa_history:
            st.markdown("---")
            st.subheader("📚 Previous Q&A")
            for q, a in reversed(st.session_state.qa_history):
                st.markdown(f"**Q:** {q}")
                st.markdown(a)
                st.markdown("—")

    elif mode == "Challenge Me":
        st.subheader("🧠 Challenge Yourself!")
        st.markdown("Click the button to generate logic-based questions from your document.")

        if st.button("🎲 Generate Questions"):
            with st.spinner("⚙️ Generating questions..."):
                st.session_state.questions = generate_logic_questions(raw_text)

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
                        if "correct" in feedback.lower():
                            st.success(f"**{q}**\n\n✅ {feedback}")
                        else:
                            st.warning(f"**{q}**\n\n⚠️ {feedback}")

else:
    st.info("📥 Please upload a PDF or TXT file to get started.")
st.markdown("<hr><center><small>🚀 Made with ❤️ by Labanya Roy </small></center>", unsafe_allow_html=True)

