import random
import json
import time

class Writer:

    tokens = []

    def initalize(self,tokens_file): #writes tokens from txt file once at the start
        t = open(tokens_file, encoding="utf-8")
        for i in t:
            self.tokens.append(i.replace('\n', ''))
        t.close()

    def find_match(self, context):
        r = open('embedded_token_vectors.json', encoding="utf-8")
        embedded_token_vectors = json.load(r)
        r.close()

        context_vector = [0 for i in range(len(self.tokens))]
        for i in range(len(context)):
            context_vector[self.tokens.index(list(reversed(context))[i])] += 1/((i+1)**2)

        #normalization
        normalized_values = []
        highest_value = -1
        for j in context_vector:
            if j>highest_value:
                highest_value = j
        for j in context_vector:
            if not highest_value == 0:
                normalized_values.append(j/highest_value)
            else:
                normalized_values.append(0)
                #print(j/highest_value)
        context_vector = normalized_values

        best_match = None
        best_similarity = -1
        for token, vector in embedded_token_vectors.items():
            similarity = self.cosine_similarity(context_vector, vector)
            if similarity > best_similarity and not token == context[len(context)-1]:
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
    def tokenize_string(self, text):
        vocabulary = []
        v = open("tokens.txt", encoding="utf-8")
        for i in v:
            vocabulary.append(i.replace('\n', ''))

        sorted_vocab = sorted(vocabulary, key=len, reverse=True)
        tokens = []
        i = 0
        while i < len(text):
            matched = False
            for token in sorted_vocab:
                if text[i:i+len(token)] == token:
                    tokens.append(token)
                    i += len(token)
                    matched = True
                    break
            if not matched:
                tokens.append(text[i])
                i += 1
        print(tokens)
        return tokens

writer = Writer()
x = "Alice ate a sugarplum"
previous_tokens = writer.tokenize_string(x)
writer.initalize("tokens.txt")
while True:
    #print(previous_tokens[len(previous_tokens)-1], end="", flush=True)
    print(x, end="", flush=True)
    x = writer.find_match(previous_tokens)
    previous_tokens.append(x)
    #time.sleep(0.1)