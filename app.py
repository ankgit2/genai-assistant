# app.py

import streamlit as st
from utils.document_parser import extract_text_from_pdf
from utils.summarizer import generate_summary
from utils.qa_engine import ask_question, generate_challenges

st.set_page_config(page_title="GenAI Assistant", layout="wide")

st.title("📄 GenAI Assistant - Powered by Azure GPT with Memory 🧠")

# --- Initialize memory ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        st.session_state.document_text = extract_text_from_pdf(uploaded_file)

    # --- Auto Summary ---
    st.subheader("🧠 Auto Summary")
    if st.button("Generate Summary"):
        with st.spinner("Summarizing..."):
            summary = generate_summary(st.session_state.document_text)
            st.success("Summary:")
            st.write(summary)

    # --- Ask Anything (with memory) ---
    st.subheader("❓ Ask Anything")
    user_question = st.text_input("Enter your question")

    if st.button("Get Answer"):
        with st.spinner("Generating answer..."):
            # Combine prior chat with current question
            full_prompt = ""
            for turn in st.session_state.chat_history:
                full_prompt += f"User: {turn['question']}\nAssistant: {turn['answer']}\n"

            full_prompt += f"User: {user_question}"

            answer, source = ask_question(st.session_state.document_text, full_prompt)

            # Save to chat memory
            st.session_state.chat_history.append({"question": user_question, "answer": answer})

            # Show the latest answer
            st.markdown(f"**Answer:** {answer}")
            st.caption(f"_Source: {source}_")

    # --- Display chat history ---
    if st.session_state.chat_history:
        st.markdown("### 🧾 Chat History")
        for i, turn in enumerate(reversed(st.session_state.chat_history), 1):
            st.markdown(f"**Q{i}:** {turn['question']}")
            st.markdown(f"**A{i}:** {turn['answer']}")
            st.markdown("---")

    # --- Challenge Me Quiz ---
    st.subheader("📝 Challenge Me")
    if st.button("Generate Quiz"):
        with st.spinner("Creating logic questions..."):
            challenges = generate_challenges(st.session_state.document_text)

        for i, challenge in enumerate(challenges):
            user_answer = st.text_input(f"Q{i+1}: {challenge['question']}", key=f"quiz_{i}")
            if user_answer:
                correct, feedback = challenge['evaluate'](user_answer)
                st.markdown(f"✅ {feedback}" if correct else f"❌ {feedback}")
