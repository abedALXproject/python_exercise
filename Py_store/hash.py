

def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

words = ["apple", "banana", "cherry", "apple", "banana", "apple"]
counts = count_words(words)
print(counts)  # Output: {'apple': 3, 'banana': 2, 'cherry': 1}

