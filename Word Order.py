n = int(input().strip())
counter = {}
words = []
for i in range(n):
  word = input().strip()
  if word in counter:
    counter[word] += 1
  else:
    counter[word] = 1
    words.append(word)
    
print(len(words))
for word in words:
    print(counter[word],end=' ') 

