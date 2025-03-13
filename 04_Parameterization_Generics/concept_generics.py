# def maximun_int(a: int, b: int) -> int:
#     return a if a > b else b

# def maximun_float(a: float, b: float) -> float:
#     return a if a > b else b

# def maximun_str(a: str, b: str) -> str:
#     return a if a > b else b

# print(maximun_int(1, 2))
# print(maximun_float(1.0, 2.0))
# print(maximun_str('a', 'b'))

from typing import TypeVar

T = TypeVar('T')

# T => Semua Tipe Data => int, float, str, dll

def maximum(a: T, b: T) -> T:
    return a if a > b else b

print(maximum(1, 2))
print(maximum(1.0, 2.0))
print(maximum('a', 'b'))