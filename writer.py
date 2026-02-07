import random
import json
import time

class Writer:
    def find_match(self, context):
        r = open('embedded_token_vectors.json', encoding="utf-8")
        embedded_token_vectors = json.load(r)
        r.close()
        if context in embedded_token_vectors:
            context_vector = embedded_token_vectors[context]
            best_match = None
            best_similarity = -1
            for token, vector in embedded_token_vectors.items():
                similarity = self.cosine_similarity(context_vector, vector)
                if similarity > best_similarity and not token == context:
                    best_similarity = similarity
                    best_match = token
            return best_match
    def cosine_similarity(self, vec1, vec2):
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude_vec1 = sum(a ** 2 for a in vec1) ** 0.5
        magnitude_vec2 = sum(b ** 2 for b in vec2) ** 0.5
        if magnitude_vec1 == 0 or magnitude_vec2 == 0:
            return 0
        return dot_product / (magnitude_vec1 * magnitude_vec2)


writer = Writer()
x = "White "
while True:
    x = writer.find_match(x)
    print(x)
    time.sleep(0.2)