import streamlit as st

from generator import QuizGenerator
from config import SPORTS, DIFFICULTIES

st.set_page_config(
    page_title="🏆 AI Sports Quiz Generator",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 AI-Powered Sports Quiz Generator")

st.write(
    "Generate engaging sports quizzes using "
    "Retrieval-Augmented Generation (RAG), "
    "ChromaDB, and Web Search."
)

# -------------------------
# Sidebar
# -------------------------

st.sidebar.header("Quiz Settings")

sport = st.sidebar.selectbox(
    "Select Sport",
    SPORTS
)

difficulty = st.sidebar.selectbox(
    "Difficulty",
    DIFFICULTIES
)

generator = QuizGenerator()

# -------------------------
# Generate Quiz
# -------------------------

if st.button("Generate Quiz"):

    with st.spinner("Generating quiz..."):

        quiz = generator.generate_quiz(
            sport=sport,
            difficulty=difficulty
        )

    st.success("Quiz Generated Successfully!")

    st.markdown(quiz)

# -------------------------
# Regenerate Quiz
# -------------------------

if st.button("Regenerate Quiz"):

    with st.spinner("Generating a fresh quiz..."):

        quiz = generator.generate_quiz(
            sport=sport,
            difficulty=difficulty
        )

    st.success("New Quiz Generated!")

    st.markdown(quiz)s