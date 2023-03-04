import random

# 1. Felhasználótól bekért N értékének tárolása
N = int(input("Hány alkalommal legyen feldobás? "))

# 2. N feldobás kivitelezése és nyertes meghatározása
anni_w = 0
panni_w = 0

for i in range(N):
    # Három véletlenszám generálása 1 és 6 között
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    r3 = random.randint(1, 6)

    # Kockák összege
    r_sum = r1 + r2 + r3

    # Nyertes meghatározása
    if r_sum < 10:
        winner = "Anni"
        anni_w += 1
    else:
        winner = "Panni"
        panni_w += 1

    # Eredmény kiírása
    print(f"Dobás: {r1} + {r2} + {r3} = {r_sum}\tNyert: {winner}")

# 3. Nyertesek számának kiírása
print(f"A játék során {anni_w} alkalommal Anni, {panni_w} alkalommal Panni nyert. ")
