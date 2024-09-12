from sklearn.preprocessing import OrdinalEncoder

# Inisiasi objek Ordinal Encoder
oe = OrdinalEncoder()

# Definisikan data dalam bentuk 2D
data = [
    ['Politeknik Negeri Malang'],
    ['Politeknik Elektronika Negeri Surabaya'],
    ['Politeknik Negeri Jakarta'],
    ['Politeknik Negeri Semarang']
]

# Transformasi menggunakan Ordinal Encoder
transform_oe = oe.fit_transform(data)

print('Data Asli:')
print(data)

print('Data Transformasi Ordinal Encoder:')
print(transform_oe)
