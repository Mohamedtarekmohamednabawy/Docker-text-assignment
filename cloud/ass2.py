import re
import nltk
from collections import Counter
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

nltk.download('stopwords')

with open("random_paragraphs.txt", 'r') as file:
    text = file.read()

stop_words = set(stopwords.words('english'))
words = re.findall(r'\b\w+\b', text.lower())
filtered_words = [word for word in words if word not in stop_words]

word_counts = Counter(filtered_words)

words = list(word_counts.keys())
frequencies = list(word_counts.values())


sorted_indices = sorted(range(len(frequencies)), key=lambda i: frequencies[i], reverse=True)
sorted_words = [words[i] for i in sorted_indices]
sorted_frequencies = [frequencies[i] for i in sorted_indices]

print("Top 20 Word Frequencies:")
for word, frequency in zip(sorted_words[:20], sorted_frequencies[:20]):
    print(f"{word}: {frequency}")

# Plot histogram
plt.figure(figsize=(10, 6))
plt.bar(sorted_words[:20], sorted_frequencies[:20], color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 20 Word Frequencies')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig(r'C:\Users\HP\Documents\Nabawy\cloud\plot.png')