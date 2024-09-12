import numpy as np
from sklearn.preprocessing import StandardScaler

# Set opsi untuk mencetak hasil numpy dengan presisi tertentu dan menghilangkan notasi ilmiah
np.set_printoptions(precision=6, suppress=True)

# Membentuk data dalam format list
data = [
    [100, 0.0001],
    [50, 0.05],
    [30, 0.003]
]

# Ubah ke bentuk numpy n-dimensional array
data = np.asarray(data)
print('Data Asli:')
print(data)

# Mendefinisikan objek StandardScaler
scaler = StandardScaler()

# Transformasikan data
scaled = scaler.fit_transform(data)
print('Data Standarisasi:')
print(scaled)
