# Leetcode 2114

def most_words_found(sentences):
    return max(len(s.split()) for s in sentences)
sentences = ["Hello world", "I love coding", "This is a test sentence"]
print(most_words_found(sentences))