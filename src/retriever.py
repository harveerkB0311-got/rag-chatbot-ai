from pathlib import Path
from typing import List, Tuple

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_PATH = BASE_DIR / "data" / "knowledge_base.txt"


class KnowledgeRetriever:
    def __init__(self, knowledge_path: Path = KNOWLEDGE_PATH):
        self.knowledge_path = knowledge_path
        self.documents = self._load_documents()
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.document_vectors = self.vectorizer.fit_transform(self.documents)

    def _load_documents(self) -> List[str]:
        text = self.knowledge_path.read_text(encoding="utf-8")
        documents = [paragraph.strip() for paragraph in text.split("\n\n") if paragraph.strip()]
        return documents

    def retrieve(self, query: str, top_k: int = 1) -> List[Tuple[str, float]]:
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.document_vectors).flatten()

        ranked_indexes = similarities.argsort()[::-1][:top_k]

        results = []
        for index in ranked_indexes:
            results.append((self.documents[index], float(similarities[index])))

        return results
