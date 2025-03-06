from enum import Enum

class JenisKelamin(Enum):
    PRIA = 1
    WANITA = 2

# Name => PRIA atau WANITA
# Value => PRIA -> 1, WANITA -> 2
# Enum Value => JenisKelamin.PRIA atau JenisKelamin.WANITA
print(JenisKelamin.PRIA)
print(JenisKelamin.PRIA.name)
print(JenisKelamin.PRIA.value)