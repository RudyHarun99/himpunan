'''
Soal 1 - 🔴🔵 Himpunan
Diketahui:

A = himpunan (set) bilangan genap antara 1 dan 20.
B = himpunan (set) bilangan ganjil antara 1 dan 20.
C = himpunan (set) bilangan negatif lebih dari -10.
D = himpunan (set) bilangan prima antara 1 dan 20.
E = himpunan (set) bilangan komposit antara 1 dan 20.
Definisi & kategori bilangan dapat Anda simak di laman Wikipedia. Buatlah sebuah file python (.py) yang dapat menyelesaikan permasalahan himpunan berikut:

a. A ∪ B ∪ C ∪ D ∪ E

b. (A ∩ B) ∪ (D ∩ E)

c. (A ∪ B) ∩ (D ∪ E)

d. (A ∪ B) - (D ∪ E)

e. (A ∪ B ∪ C) - (A ∩ E)
'''

# Jawaban
A={2,4,6,8,10,12,14,16,18}
B={3,5,7,9,11,13,15,17,19}
C={-1,-2,-3,-4,-5,-6,-7,-8,-9}
D={2,3,5,7,11,13,17,19}
E={4,6,8,9,10,12,14,15,16,18}

# a.
print('a. A ∪ B ∪ C ∪ D ∪ E =',(A|B|C|D|E))

# b.
print('b. (A ∩ B) ∪ (D ∩ E) =',(A&B)|(D&E))

# c.
print('c. (A ∪ B) ∩ (D ∪ E) =',(A|B)&(D|E))

# d.
print('d. (A ∪ B) - (D ∪ E) =',(A|B)-(D|E))

# e.
print('e. (A ∪ B ∪ C) - (A ∩ E) =',(A|B|C)-(A&E))