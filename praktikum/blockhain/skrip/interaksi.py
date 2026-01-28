from brownie import KoinAllIn, accounts

def utama():
    # Dapatkan kontrak yang telah disebar
    token = KoinAllIn[-1]  # Dapatkan kontrak yang paling baru disebar

    # Gunakan akun
    akun1 = accounts[0]  # Penyebar
    akun2 = accounts[1]  # Akun kedua

    # Tampilkan saldo awal
    print(f"Saldo awal akun 1: {token.saldoDari(akun1) / 10**18} AIC")
    print(f"Saldo awal akun 2: {token.saldoDari(akun2) / 10**18} AIC")

    # Transfer 100 AIC dari akun 1 ke akun 2
    jumlah_transfer = 100 * 10**18
    token.kirim(akun2, jumlah_transfer, {"from": akun1})

    # Tampilkan saldo setelah transfer
    print(f"Saldo akun 1 setelah transfer: {token.saldoDari(akun1) / 10**18} AIC")
    print(f"Saldo akun 2 setelah transfer: {token.saldoDari(akun2) / 10**18} AIC")
