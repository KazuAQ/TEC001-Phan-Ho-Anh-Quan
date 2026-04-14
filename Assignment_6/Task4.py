import string

def word_frequency_analysis(text):
    
    words = text.lower().split()
    
    words = [word.strip(string.punctuation) for word in words]
    words = [word for word in words if word]
    
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    top_5 = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5])
    
    total_words = len(words)
    top_5_count = sum(top_5.values())
    proportion = (top_5_count / total_words) * 100 if total_words > 0 else 0
    
    return {
        'top_5': top_5,
        'total_words': total_words,
        'proportion': proportion
    }