import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk
from collections import Counter
from nltk.util import ngrams
import string
import os

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")

class TextAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.text = self.read_file()
        self.tokens = []
        self.cleaned_tokens = []
        self.stems = []
        self.lemmas = []

    def read_file(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                return file.read()
        except:
            print(f"Error reading {self.file_name}")
            return ""

    def preprocess(self):
        stop_words = set(stopwords.words("english"))
        self.tokens = word_tokenize(self.text.lower())

        self.cleaned_tokens = [
            word for word in self.tokens
            if word not in stop_words and word not in string.punctuation and word.isalpha()
        ]

    def stem_words(self):
        stemmer = PorterStemmer()
        self.stems = [stemmer.stem(word) for word in self.cleaned_tokens]

    def lemmatize_words(self):
        lemmatizer = WordNetLemmatizer()
        self.lemmas = [lemmatizer.lemmatize(word) for word in self.cleaned_tokens]

    def most_common_tokens(self):
        return Counter(self.lemmas).most_common(20)

    def named_entity_count(self):
        tagged = pos_tag(word_tokenize(self.text))
        tree = ne_chunk(tagged)

        count = 0
        for item in tree:
            if hasattr(item, "label"):
                count += 1
        return count

    def trigram_analysis(self):
        trigrams = list(ngrams(self.cleaned_tokens, 3))
        return Counter(trigrams).most_common(20)

    def analyze(self):
        self.preprocess()
        self.stem_words()
        self.lemmatize_words()

        print("\n==========", self.file_name, "==========")

        print("\nTop 20 words:")
        for word, count in self.most_common_tokens():
            print(word, count)

        print("\nNamed Entities:", self.named_entity_count())

        print("\nTop Trigrams:")
        for tri, count in self.trigram_analysis():
            print(tri, count)


def compare_texts():
    files = ["Text_1.txt", "Text_2.txt", "Text_3.txt", "Text_4.txt"]

    analyzers = {}
    for f in files:
        analyzer = TextAnalyzer(f)
        analyzer.preprocess()
        analyzers[f] = analyzer

    t4 = set(analyzers["Text_4.txt"].trigram_analysis())

    for f in ["Text_1.txt", "Text_2.txt", "Text_3.txt"]:
        other = set(analyzers[f].trigram_analysis())
        match = t4.intersection(other)

        print(f"\nText_4 vs {f} -> matches:", len(match))


def main():
    files = ["Text_1.txt", "Text_2.txt", "Text_3.txt", "Text_4.txt"]

    for f in files:
        if os.path.exists(f):
            TextAnalyzer(f).analyze()
        else:
            print(f, "not found")

    compare_texts()


if __name__ == "__main__":
    main()
  
