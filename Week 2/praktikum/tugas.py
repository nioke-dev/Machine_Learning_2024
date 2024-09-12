from sklearn.feature_extraction.text import TfidfVectorizer

with open('corpus.txt', 'r') as file:
    corpus = file.readlines()


# inisialisasi obyek TFidVectorizer
vect = TfidfVectorizer(stop_words='english')
# Pembobotan TF-IDF
resp = vect.fit_transform(corpus)

# Cetak Hasil
print(resp)

print(vect.get_feature_names_out())