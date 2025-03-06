# def check_hari(bulan: str):
#     hari = 0
#     if(bulan == "Januari"):
#         hari = 31
#     elif(bulan == "Februari"):
#         hari = 28
#     elif(bulan == "Maret"):
#         hari = 31
#     elif(bulan == "April"):
#         hari = 30
#     elif(bulan == "Mei"):
#         hari = 31
#     elif(bulan == "Juni"):
#         hari = 30
#     elif(bulan == "Juli"):
#         hari = 31
#     elif(bulan == "Agustus"):
#         hari = 31
#     elif(bulan == "September"):
#         hari = 30
#     elif(bulan == "Oktober"):
#         hari = 31
#     elif(bulan == "November"):
#         hari = 30
#     elif(bulan == "Desember"):
#         hari = 31
#     return hari

# print(check_hari("Agustus")) # 31

days_in_month = {
    "Januari": 31, "Februari": 28, "Maret": 31, "April": 30, "Mei": 31, "Juni": 30,
    "Juli": 31, "Agustus": 31, "September": 30, "Oktober": 31, "November": 30, "Desember": 31
}

bulan = "Agustus"
jumlah_hari = days_in_month.get(bulan, "Bulan tidak ditemukan")
print(jumlah_hari) # 31