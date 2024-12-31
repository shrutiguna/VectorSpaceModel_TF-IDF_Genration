import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
import os
import io
import math
corpusroot = "C:\\Users\\Shruti Gunasekaran\\Desktop\\dm proj1\\P1\\US_Inaugural_Addresses"
preprocessed_doc = []
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
for filename in os.listdir(corpusroot):
 file_path = os.path.join(corpusroot, filename)
 if filename.startswith("0") or filename.startswith('1'):
    with io.open(file_path, 'r', encoding='utf-8') as file:
        doc = file.read().lower()
 tokens = tokenizer.tokenize(doc)
 #stop words removal
 filtered_tokens = [token for token in tokens if token not in 
stop_words]
 # Stemming
 stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
 preprocessed_doc.append(stemmed_tokens)
document_frequencies = {}
for document in preprocessed_doc:
 for token in set(document):
    document_frequencies[token] = document_frequencies.get(token, 0) + 1
def calculate_tf(tokens):
 tf = {}
 for token in tokens:
    tf[token] = tf.get(token, 0) + 1
 max_frequency = max(tf.values()) if tf else 1
 tf_normalized = {token: freq / max_frequency for token, freq in tf.items()}
 return tf_normalized
def calculate_idf(corpus, tokens):
 idf = {}
 for token in tokens:
    count = sum(1 for doc in corpus if token in doc)
 idf[token] = math.log(len(corpus) / count) if count > 0 else -1
 return idf
def getidf(token):
 return idf.get(token, -1)
def getweight(filename, token):
 document_tfidf = tfidf_vectors[document_indices[filename]]
 return document_tfidf.get(token, 0)
def query_preprocess(query):
 query_tokens = tokenizer.tokenize(query.lower())
 query_filtered_tokens = [token for token in query_tokens if token not in 
stop_words]
 query_stemmed_tokens = [stemmer.stem(token) for token in query_filtered_tokens]
 return query_stemmed_tokens
def calculate_similarity(query_vector, document_vector):
 dot_product = sum(query_vector.get(token, 0) * document_vector.get(token, 0) 
for token in set(query_vector))
 query_normalized = math.sqrt(sum(value ** 2 for value in 
query_vector.values()))
 document_normalized = math.sqrt(sum(value ** 2 for value in 
document_vector.values()))
 cosine_similarity = dot_product / (query_normalized * document_normalized) if query_normalized != 0 and document_normalized!= 0 else 0
 return cosine_similarity
idf = calculate_idf(preprocessed_doc, document_frequencies.keys())
tfidf_vectors = []
for document in preprocessed_doc:
 tf = calculate_tf(document)
 tfidf = {token: tf[token] * idf[token] for token in set(document) if token in 
idf}
 tfidf_vectors.append(tfidf)
document_indices = {filename: index for index, filename in 
enumerate(os.listdir(corpusroot)) if filename.endswith(".txt")}
def query(query):
 
 query_tokens = query_preprocess(query)
 query_tf = calculate_tf(query_tokens)
 query_vector = {token: tf * getidf(token) for token, tf in query_tf.items() if 
getidf(token) != -1}
 similarities = []
 for document_tfidf in tfidf_vectors:
    similarity = calculate_similarity(query_vector, document_tfidf)
 similarities.append(similarity)
 max_similar = max(range(len(similarities)), key=similarities.__getitem__)
 max_similar_document = os.listdir(corpusroot)[max_similar]
 similarity_score = similarities[max_similar]
 return max_similar_document, similarity_score
print("%.12f" % getidf('british'))
print("%.12f" % getidf('union'))
print("%.12f" % getidf('war'))
print("%.12f" % getidf('military'))
print("%.12f" % getidf('great'))
print("--------------")
print("%.12f" % getweight('02_washington_1793.txt', 'arrive'))
print("%.12f" % getweight('07_madison_1813.txt', 'war'))
print("%.12f" % getweight('12_jackson_1833.txt', 'union'))
print("%.12f" % getweight('09_monroe_1821.txt', 'british'))
print("%.12f" % getweight('05_jefferson_1805.txt', 'public'))
print("--------------")
print("(%s, %.12f)" % query("pleasing people"))
print("(%s, %.12f)" % query("british war"))
print("(%s, %.12f)" % query("false public"))
print("(%s, %.12f)" % query("people institutions"))
print("(%s, %.12f)" % query("violated willingly"))