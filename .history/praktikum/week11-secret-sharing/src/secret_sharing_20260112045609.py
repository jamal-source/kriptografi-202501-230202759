from secretsharing import SecretSharer

# Rahasia yang ingin dibagi
secret = "KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:", shares)

# Rekonstruksi rahasia dari 3 shares
recovered = SecretSharer.recover_secret(shares[:3])
print("Recovered secret:", recovered)

# Rekonstruksi rahasia dari 4 shares
recovered4 = SecretSharer.recover_secret(shares[:4])
print("Recovered secret with 4 shares:", recovered4)

# Coba rekonstruksi dari 2 shares (harus gagal)
try:
    recovered2 = SecretSharer.recover_secret(shares[:2])
    print("Recovered secret with 2 shares:", recovered2)
except Exception as e:
    print("Failed to recover with 2 shares:", str(e))
