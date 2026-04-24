# Assignment 9: NLTK

## Purpose
The purpose of this project is to use Python and NLTK to analyze text files. Natural Language Processing (NLP) helps computers understand human language by breaking text into smaller parts and finding patterns. :contentReference[oaicite:0]{index=0}  

In this project, I used different techniques like tokenization, stemming, lemmatization, named entity recognition, and trigram analysis to study four different texts.

---

## How the Program Works
The program reads each text file and processes it step by step:

- First, it breaks the text into words (tokenization)
- Then it removes common words and punctuation (cleaning)
- After that, it simplifies words using stemming and lemmatization
- It counts named entities like people or places
- Finally, it finds common 3-word patterns (trigrams)

These steps help turn unstructured text into something easier to understand and compare.

---

## Results

**Text 1 subject:**  
This text focuses on horror and dark themes. It includes fear, strange events, and supernatural ideas.

**Text 2 subject:**  
This text is about a fantasy world. It includes magic, adventure, and different characters.

**Text 3 subject:**  
This text talks about kingdoms, politics, and power struggles. It focuses on conflict and relationships between characters.

---

## Text 4 Author Guess
Based on trigram patterns and writing style, Text 4 is most similar to Text 3. Both texts focus on similar topics and have a close writing style. Because of this, it is likely that Text 4 was written by the same author as Text 3.

---

## Class Design
The program uses a class called `TextAnalyzer` to organize the code.

### Attributes
- `file_name` → stores the file name  
- `text` → stores the full text  
- `tokens` → list of words  
- `cleaned_tokens` → words after cleaning  
- `stems` → stemmed words  
- `lemmas` → lemmatized words  

### Methods
- `read_file()` → reads the file  
- `preprocess()` → cleans and tokenizes text  
- `stem_words()` → applies stemming  
- `lemmatize_words()` → applies lemmatization  
- `most_common_tokens()` → finds top words  
- `named_entity_count()` → counts named entities  
- `trigram_analysis()` → finds common trigrams  
- `analyze()` → runs full analysis  

---

## Limitations
This project uses basic NLP techniques, so it may not always be fully accurate. It only looks at word patterns and not deep meaning. A more advanced model could give better results.
