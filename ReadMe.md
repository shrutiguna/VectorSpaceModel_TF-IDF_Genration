# TFIDF_Gen

**TFIDF_Gen** is a Python project designed to process a corpus of 30 US presidential inaugural addresses, compute TF-IDF vectors for the documents, and determine the most relevant document for a given query using cosine similarity.

## Key Features:
1. **Corpus Processing**: Reads 30 `.txt` files from the `US_Inaugural_Addresses` folder containing inaugural addresses.
2. **Text Preprocessing**:
   - Converts text to lowercase for uniformity.
   - Tokenizes text using `RegexpTokenizer`.
   - Removes common English stopwords with NLTK's stopword corpus.
   - Applies stemming to tokens using the Porter Stemmer to standardize word forms.
3. **TF-IDF Calculation**:
   - **TF (Term Frequency)**: Computes the normalized term frequency of words in each document.
   - **IDF (Inverse Document Frequency)**: Calculates the importance of words across the corpus.
4. **Query Handling**:
   - Processes the query by applying the same text preprocessing steps.
   - Generates a query vector and computes cosine similarity with document vectors.
5. **Cosine Similarity**: Identifies the document with the highest similarity score for the given query.

## Functions:
- `getidf(token)`: Returns the inverse document frequency of a token. If the token doesn't exist, returns `-1`.
- `getweight(filename, token)`: Provides the normalized TF-IDF weight of a token in a specified document or `0` if absent.
- `query(qstring)`: Accepts a query string and returns a tuple with the most relevant document filename and its cosine similarity score.

This project, implemented in `TFIDF_Gen.py`, demonstrates core text processing techniques and the application of the Vector Space Model for efficient information retrieval.
