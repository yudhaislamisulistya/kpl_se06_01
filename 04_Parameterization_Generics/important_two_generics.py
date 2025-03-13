# # # def jumlahkan(data):
# # #     return sum(data)

# # # # [1,2,3,4,5] => 1 + 2 + 3 + 4 + 5 = 15

# # # print(jumlahkan([1,2,3,4,5])) # 15
# # # print(jumlahkan([1,"2",3,4,5])) # 15

# # from typing import List

# # def jumlahkan(data: List[int]) -> int:
# #     return sum(data)

# # print(jumlahkan([1,2,3,4,5])) # 15
# # print(jumlahkan([1,"2",3,4,5])) # 15

# # def kali_dua(data):
# #     return [int(item) * 2 for item in data]
# # # [1,2,3,4,5,6] [1*2, 2*2, 3*2, 4*2, 5*2, 6*2] => [2,4,6,8,10,12]
# # print(kali_dua([1,2,3,4,5,6]))
# # print(kali_dua(["1", "2", "3", "4", "5", "6"]))

# from typing import List

# def kali_dua(data: List[int]) -> List[int]:
#     return [item * 2 for item in data]

# print(kali_dua([1,2,3,4,5,6]))
# print(kali_dua(["1", "2", "3", "4", "5", "6"]))


# angka = 5
# teks = '5'
# hasil = angka + teks
# print(hasil)

def check_admin(user_input: int) -> bool:
    return user_input == "admin"

print(check_admin("ADMIN"))