
def PatternCount(text, pattern):
    count = 0
    for i in range(0,len(text)-len(pattern) + 1):
        if text[i:len(pattern)+1] == pattern:
            count = count + 1
    return count

def FrequentWords(text, k):
    FrequentPatterns = []
    for i in range(0, len(text) - k + 1):
        pattern = text[i : k + 1]
        count = PatternCount(text, pattern)
    maxCount = max(count)
    for i in range(0, len(text) - k + 1):
        if count == maxCount:
            FrequentPatterns.extend(count)
            list(set(FrequentPatterns))

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k=4

print(FrequentWords(text, k))