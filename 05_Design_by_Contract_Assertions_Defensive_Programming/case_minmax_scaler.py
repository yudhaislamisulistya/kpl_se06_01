from typing import List

def min_max_scaler(data: List[float]) -> List[float]:
    """Mengubah data ke dalam skala 0-1 menggunakan pendekatan MinMaxScaler"""
    # Precondition
    assert len(data) > 0, "Data tidak boleh kosong"
    
    min_val, max_val = min(data), max(data)
    
    # Postcondition
    assert max_val > min_val, "Nilai maksimum harus lebih besar dari nilai minimum"
    
    return [(x - min_val) / (max_val - min_val) for x in data]

# Test
sample_data = [10,20,30,40,50,66]
scale_data = min_max_scaler(sample_data)

# Invariant and Postcondition
assert all(0 <= x <= 1 for x in scale_data), "Data harus dalam skala 0-1"

print("data asli:", sample_data)
print("data setelah di-scaling:", scale_data)