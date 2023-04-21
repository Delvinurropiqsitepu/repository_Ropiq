# Program untuk menghitung jumlah bilangan ganjil dari sebuah list menggunakan filter dan reduce

from functools import reduce

# Fungsi untuk memeriksa apakah bilangan ganjil atau tidak
def is_odd(num):
    return num % 2 != 0

# List bilangan
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Menggunakan filter untuk memfilter bilangan ganjil dari list nums
filtered_nums = list(filter(is_odd, nums))

# Menggunakan reduce untuk menghitung jumlah bilangan ganjil dari filtered_nums
odd_sum = reduce(lambda x, y: x + y, filtered_nums)

# Menampilkan hasil
print("List bilangan: ", nums)
print("List bilangan ganjil: ", filtered_nums)
print("Jumlah bilangan ganjil: ", odd_sum)
