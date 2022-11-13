sentences = ["alice and bob love leetcode",
             "i think so too", "this is great thanks very much"]

maximum = [sentences[i].count(" ")+1 for i in range(len(sentences))]
print(max(maximum))
