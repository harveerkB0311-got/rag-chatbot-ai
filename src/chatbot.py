from retriever import KnowledgeRetriever


class RAGChatbot:
    def __init__(self):
        self.retriever = KnowledgeRetriever()

    def answer_question(self, question: str) -> dict:
        results = self.retriever.retrieve(question, top_k=1)

        if not results:
            return {
                "question": question,
                "answer": "I could not find relevant information in the knowledge base.",
                "source": None
            }

        source_text, score = results[0]

        if score < 0.05:
            return {
                "question": question,
                "answer": "I could not find a strong match in the knowledge base. Please ask a more specific question.",
                "source": source_text
            }

        answer = f"Based on the knowledge base: {source_text}"

        return {
            "question": question,
            "answer": answer,
            "source": source_text
        }
