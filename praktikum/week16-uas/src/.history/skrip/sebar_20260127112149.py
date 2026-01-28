dari brownie import KoinAllIn, akun

def utama():
    # Gunakan akun default dari Brownie
    akun1 = akun[0]

    # Sebar kontrak dengan pasokan awal 1000 AIC (1e18 = 1 token)
    pasokan_awal = 1000 * 10**18
    token = KoinAllIn.deploy(pasokan_awal, {"from": akun1})

    print(f"Kontrak disebar di: {token.address}")
    print(f"Saldo penyebar: {token.saldoDari(akun1) / 10**18} AIC")
