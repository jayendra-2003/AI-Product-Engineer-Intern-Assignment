import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from retriever import retrieve_context
from web_search import search_web


class QuizGenerator:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4.1-mini",
            temperature=0.8,
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def build_prompt(self, sport, difficulty, context):

        template = """
You are an expert sports quiz creator.

Your task is to generate engaging multiple-choice quizzes.

Rules:
- Sport: {sport}
- Difficulty: {difficulty}
- Generate exactly 5 different questions.
- Every question must have four options:
    A
    B
    C
    D
- Mention the correct answer.
- Give a short explanation (1-2 lines).
- Use ONLY the retrieved context below.
- If context contains recent information, use it.
- Never invent facts.
- Every question should be unique.

Retrieved Context:

{context}

Output format:

Sport: ...

Difficulty: ...

Question 1:
Question:
A.
B.
C.
D.

Correct Answer:

Explanation:

Question 2:
...

Question 3:
...

Question 4:
...

Question 5:
...
"""

        return PromptTemplate.from_template(template).format(
            sport=sport,
            difficulty=difficulty,
            context=context
        )

    def generate_quiz(self, sport, difficulty):

        # Retrieve knowledge from ChromaDB
        vector_context = retrieve_context(
            query=f"{sport} {difficulty} sports quiz facts",
            k=5
        )

        # Retrieve latest information from web
        web_context = search_web(
            f"latest important {sport} facts records tournaments"
        )

        combined_context = f"""
========== VECTOR DATABASE ==========
{vector_context}

========== WEB SEARCH ==========
{web_context}
"""

        prompt = self.build_prompt(
            sport=sport,
            difficulty=difficulty,
            context=combined_context
        )

        response = self.llm.invoke(prompt)

        return response.content


if __name__ == "__main__":

    generator = QuizGenerator()

    quiz = generator.generate_quiz(
        sport="Cricket",
        difficulty="Medium"
    )

    print(quiz)