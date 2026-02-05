#import numpy as np
import random
class NeuralMatrix:
    def create_token_vocabulary(input_text, target_vocabulary_size):
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
        print(final_token_vocabulary)


    t = open("alice.txt").read() #input
    x = 400 #output array length
    create_token_vocabulary(t, x)
        
