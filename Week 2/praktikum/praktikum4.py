from sklearn.preprocessing import OneHotEncoder

# Inisiasi objek OneHotEncoder
ohe = OneHotEncoder()

# Definisikan data dalam bentuk 2D
data = [
    ['Politeknik Negeri Malang'],
    ['Politeknik Elektronika Negeri Surabaya'],
    ['Politeknik Negeri Jakarta'],
    ['Politeknik Negeri Semarang']
]

# Transformasi menggunakan OneHotEncoder
transform_ohe = ohe.fit_transform(data)

print('Data Asli:')
print(data)

print('Data Transformasi One-Hot Encoding:')
print(transform_ohe.toarray())
