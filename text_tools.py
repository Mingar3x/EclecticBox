def remove_extra(file):
    r = open(file, encoding="utf-8")
    text = r.read().replace("\n", "").replace("[", "").replace("]", "")
    r.close()
    r = open(file, "w", encoding="utf-8")
    r.write(text)
    r.close()
    return text
remove_extra("prideprejustice.txt")

# preceding_token_counts = {}
#         for i in range(len(tokenized_text)):
#             token = tokenized_text[i]
#             previous_tokens = []
#             for j in range(context_window):
#                 if i-j>=0 and not i-j==i:
#                     previous_tokens.append(tokenized_text[i-j])
#             if token not in preceding_token_counts:
#                 preceding_token_counts[token] = []
#             preceding_token_counts[token].append(previous_tokens)
        
#         embedded_token_vectors = {} #not normalized yet btw that comes later
#         #matches token (string) to an array containing the number of times each 
#         #other token has appeared before it, wieghted by distance along context window.
#         for i in range(len(tokens)):
#             embedded_token_vectors[tokens[i]] = [0 for q in range(len(tokens))]
#         for i in range(len(tokens)):
#             if tokens[i] in preceding_token_counts:
#                 for j in range(len(preceding_token_counts[tokens[i]])):
#                     for k in range(len(preceding_token_counts[tokens[i]][j])):
#                         embedded_token_vectors[tokens[i]][tokens.index(preceding_token_counts[tokens[i]][j][k])]=embedded_token_vectors[tokens[i]][tokens.index(preceding_token_counts[tokens[i]][j][k])]+(1/(k+1))
#             print("embedded: "+ tokens[i]+ " , " + str(round(i/(len(tokens)-1)*100, 2))+ "% done")