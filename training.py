#import numpy as np
import random
import json
class Trainer:
    
    def create_token_vocabulary(self, input_text, target_vocabulary_size):
        final_token_vocabulary = []
        working_token_list = []
        for i in range(len(input_text)):
            a = input_text[i]
            working_token_list.append(a)
            if not a in final_token_vocabulary:
                final_token_vocabulary.append(a)
        
        while len(final_token_vocabulary) < target_vocabulary_size:
            pair_frequency_table = {}
            
            for i in range(len(working_token_list)-1): #count adjacent tokens
                k = (working_token_list[i], working_token_list[i+1])
                if k in pair_frequency_table.keys():
                    pair_frequency_table[k] = pair_frequency_table[k] + 1
                else:
                    pair_frequency_table[k] = 1

            highest_key = [] #finding and merging most common "keys" (tokens) 
            highest_value = -1
            for i in pair_frequency_table.keys():
                if pair_frequency_table[i] > highest_value:
                    highest_value = pair_frequency_table[i]
                    highest_key = [i]
                elif pair_frequency_table[i] == highest_value:
                    highest_key.append(i)

            while len(final_token_vocabulary) < target_vocabulary_size and len(highest_key) > 0: 
                key = random.choice(highest_key)
                
                new_token = key[0] + key[1]
                final_token_vocabulary.append(new_token)
                for i in reversed(range(len(working_token_list)-1)):
                    if working_token_list[i] == key[0] and working_token_list[i+1] == key[1]:
                        z = working_token_list.pop(i+1)
                        working_token_list[i] = new_token
                highest_key.remove(key)
        #print(final_token_vocabulary)
        return final_token_vocabulary, working_token_list


    def tokenize(self, file, count):

        t = open(file, encoding="utf-8") #input
        y, x = self.create_token_vocabulary(t.read().replace('\ufeff', ''), count)
        t.close()
        #print(x)

        #clears the token vocabulary file
        r = open("tokens.txt", "w", encoding="utf-8")
        r.write('')
        r.close()

        r = open('tokens.txt', "a", encoding="utf-8")
        for i in y:
            r.write(i)
            if not y.index(i) == len(y) - 1:
                r.write("\n")
        r.close()

        #clears the tokenized text file
        r = open("tokenized_text.txt", "w", encoding="utf-8")
        r.write('')
        r.close()

        #writing the final tokenized text
        r = open('tokenized_text.txt', "a", encoding="utf-8")
        for i in x:
            r.write(i)
            if not y.index(i) == len(y) - 1:
                r.write("\n")
        r.close()

    def embed_tokens(self, tokenized_text_file, tokens_file):
        context_window = 20
        #writing files to arrays for easy operations
        r = open(tokenized_text_file, encoding="utf-8")
        t = open(tokens_file, encoding="utf-8")
        tokenized_text, tokens = [], []
        for i in r:
            tokenized_text.append(i.replace('\n', ''))
        for i in t:
            tokens.append(i.replace('\n', ''))
        r.close()
        t.close()
        #saving the tokens preceding each token within a set context window
        
        preceding_token_counts = {}
        for i in range(len(tokenized_text)-1):
            token = tokenized_text[i]
            previous_tokens = []
            for j in range(context_window):
                if i-j>=0 and not i-j==i:
                    previous_tokens.append(tokenized_text[i-j])
            if token not in preceding_token_counts:
                preceding_token_counts[token] = []
            preceding_token_counts[token].append(previous_tokens)
        
        embedded_token_vectors = {} #not normalized yet btw that comes later
        #matches token (string) to an array containing the number of times each 
        #other token has appeared before it, wieghted by distance down context window.
        for i in range(len(tokens)):
            embedded_token_vectors[tokens[i]]= [0 for i in range(len(tokens))]
        for i in range(len(tokens)):
            if tokens[i] in preceding_token_counts:
                for j in range(len(preceding_token_counts[tokens[i]])):

                    embedded_token_vectors[tokens[i]][i]=embedded_token_vectors[tokens[i]][i]+(1/(j+1))

        #writing the embedding table to a json file
        with open('embedded_token_vectors.json', 'w', encoding="utf-8") as f:
            json.dump(embedded_token_vectors, f, ensure_ascii=False, indent=4)

        

#"main" code
trainer = Trainer()
trainer.embed_tokens("tokenized_text.txt", "tokens.txt")
#trainer.tokenize("alice.txt", 300)

