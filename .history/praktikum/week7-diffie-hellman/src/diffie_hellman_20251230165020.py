import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)

# Simulasi MITM (Man-in-the-Middle)
print("\n--- Simulasi Serangan MITM ---")
# Eve mencegat dan mengganti public key
e = random.randint(1, p-1)  # secret Eve
E = pow(g, e, p)  # public key Eve

# Alice mengira mengirim ke Bob, tapi Eve ganti dengan E
shared_secret_A_eve = pow(E, a, p)
shared_secret_E_alice = pow(A, e, p)

# Bob mengira menerima dari Alice, tapi Eve ganti dengan E
shared_secret_B_eve = pow(E, b, p)
shared_secret_E_bob = pow(B, e, p)

print("Alice berpikir kunci bersama dengan Bob:", shared_secret_A_eve)
print("Bob berpikir kunci bersama dengan Alice:", shared_secret_B_eve)
print("Eve mengetahui kunci Alice:", shared_secret_E_alice)
print("Eve mengetahui kunci Bob:", shared_secret_E_bob)
