# 🤖 Chat with PDF

A lightweight chatbot built with **Streamlit** and **Hugging Face Transformers** that lets you ask questions about any PDF content or summary.

---

## 📌 Overview

This app allows users to:
- Upload a `.txt` file containing text from a PDF (extracted or summarized).
- Ask questions about the content.
- View a full chat history with all questions and answers.

It is designed to work seamlessly with the [AI PDF Summarizer](https://your-summarizer-app-url.streamlit.app) (replace with your real link), but it can work independently with any `.txt` document.

---

## 🚀 Live Demo

👉 [Try the chatbot here](https://your-chatbot-app-url.streamlit.app)

---

## 🧠 Powered By

- 🤗 [Hugging Face Transformers](https://huggingface.co/transformers)
- ⚡ [Streamlit](https://streamlit.io/)
- 📚 Model: [`distilbert-base-cased-distilled-squad`](https://huggingface.co/distilbert-base-cased-distilled-squad)

---

## 🛠️ How to Use

1. Visit the deployed app.
2. Upload a `.txt` file (from a PDF or summarizer).
3. Type your question in the input box.
4. Click **Send** to get an answer.
5. View full chat history below.

---

## 🧪 Run Locally

```bash
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
pip install -r requirements.txt
streamlit run chat_with_pdf.py
