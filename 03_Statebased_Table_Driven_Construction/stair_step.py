def get_days_in_month(bulan):
    if bulan in ["Januari", "Maret", "Mei", "Juli", "Agustus", "Oktober", "Desember"]:
        return 31
    elif bulan in ["April", "Juni", "September", "November"]:
        return 30
    elif bulan == "Februari":
        return 28 # Asumsi ini adalah bulan non-kabisat
    else:
        return "Bulan tidak ditemukan"
    
print(get_days_in_month("Februari")) # 31