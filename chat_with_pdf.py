import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Chat with PDF", layout="centered")
st.title("🤖 Chat with PDF Summary or Text")


# ---------- Load Model ----------
@st.cache_resource
def load_qa_pipeline():
    return pipeline("question-answering", model="distilbert-base-cased-distilled-squad")


qa_pipeline = load_qa_pipeline()

# ---------- Session State Initialization ----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------- File Upload ----------
uploaded_file = st.file_uploader("Upload PDF Text or Summary (.txt)", type=["txt"])
if uploaded_file:
    context = uploaded_file.read().decode("utf-8")
    st.success("✅ Context loaded. You can now ask questions.")

    # ---------- Chat Input ----------
    user_query = st.text_input("💬 Ask something about the PDF:")
    if st.button("Send") and user_query:
        with st.spinner("🤖 Thinking..."):
            answer = qa_pipeline(question=user_query, context=context)
            # Save to chat history
            st.session_state.chat_history.append(("You", user_query))
            st.session_state.chat_history.append(("Bot", answer["answer"]))

    # ---------- Display Chat History ----------
    if st.session_state.chat_history:
        st.markdown("---")
        st.subheader("📜 Chat History")
        for sender, message in st.session_state.chat_history:
            if sender == "You":
                st.markdown(f"**🧑 {sender}:** {message}")
            else:
                st.markdown(f"**🤖 {sender}:** {message}")
