#implementasi normalisasi part 1
def norm_data(data):
    """
    Melakukan normalisasi data.

    Parameters:
    data (list): Data yang akan dinormalisasi

    Returns:
    list: Data hasil normalisasi
    """
    data_max = max(data)
    data_min = min(data)

    # Proses normalisasi data
    for i in range(len(data)):
        data[i] = (data[i] - data_min) / (data_max - data_min)

    return data

# Contoh Penggunaan
data = [10, 11, 12, 14, 16]
n_data = norm_data(data)  # melakukan normalisasi
print(n_data)

#implemetasi normalisasi part 2
import numpy as np
from sklearn.preprocessing import MinMaxScaler

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

# Mendefinisikan obyek MinMaxScaler
scaler = MinMaxScaler()

# Transformasikan data
scaled = scaler.fit_transform(data)
print('Data Normalisasi:')
print(scaled)
