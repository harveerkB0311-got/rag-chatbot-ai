from chatbot import RAGChatbot


def main():
    chatbot = RAGChatbot()

    print("RAG Chatbot is ready. Type 'exit' to stop.\n")

    while True:
        question = input("Ask a question: ")

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        response = chatbot.answer_question(question)

        print("\nAnswer:")
        print(response["answer"])
        print("-" * 60)


if __name__ == "__main__":
    main()
