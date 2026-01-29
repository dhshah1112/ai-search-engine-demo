import time
from typing import List, Dict

class SearchEngine:
    """
    A Hybrid Search Engine combining Vector Search (Semantic) 
    and Keyword Search (BM25).
    """
    
    def __init__(self):
        # Simulating our database connections
        self.vector_db_connected = True
        self.keyword_index_connected = True

    def hybrid_search(self, user_query: str) -> List[Dict]:
        """
        Performs the search in parallel and merges results using RRF.
        """
        print(f"Processing Query: {user_query}")
        
        # Step 1: Parallel Retrieval (Simulated)
        vector_results = self._get_vector_results(user_query)
        keyword_results = self._get_keyword_results(user_query)
        
        # Step 2: Merge Results using Reciprocal Rank Fusion (RRF)
        final_results = self._rrf_merge(vector_results, keyword_results)
        
        return final_results

    def _get_vector_results(self, query: str) -> List[Dict]:
        # TODO: Replace with actual Pinecone/Milvus call
        # This handles the "meaning" of the query (e.g., "fruit" matches "apple")
        return [
            {"id": "doc_A", "content": "Apples are red", "score": 0.95},
            {"id": "doc_B", "content": "Bananas are yellow", "score": 0.88}
        ]

    def _get_keyword_results(self, query: str) -> List[Dict]:
        # TODO: Replace with actual Elasticsearch/BM25 call
        # This handles exact matches (e.g., "Error 503")
        return [
            {"id": "doc_C", "content": "Error 503 occurred", "score": 10.5},
            {"id": "doc_A", "content": "Apples are red", "score": 5.2}
        ]

    def _rrf_merge(self, list_a: List[Dict], list_b: List[Dict]) -> List[Dict]:
        """
        Merges two lists based on Rank, not raw Score.
        Formula: Score = 1 / (Rank + k)
        """
        merged_map = {}
        k = 60
        
        # Process List A (Vectors)
        for rank, item in enumerate(list_a):
            doc_id = item['id']
            if doc_id not in merged_map:
                merged_map[doc_id] = 0.0
            merged_map[doc_id] += 1.0 / (rank + k)
            
        # Process List B (Keywords)
        for rank, item in enumerate(list_b):
            doc_id = item['id']
            if doc_id not in merged_map:
                merged_map[doc_id] = 0.0
            merged_map[doc_id] += 1.0 / (rank + k)
            
        # Sort by final RRF score
        sorted_docs = sorted(merged_map.items(), key=lambda x: x[1], reverse=True)
        return [{"id": doc[0], "rrf_score": doc[1]} for doc in sorted_docs]

if __name__ == "__main__":
    engine = SearchEngine()
    results = engine.hybrid_search("Test Query")
    print("Top Results:", results)