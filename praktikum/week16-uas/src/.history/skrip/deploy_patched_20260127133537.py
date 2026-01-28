# Import library yang diperlukan
import os  # Untuk mengakses environment variables
from brownie import network, accounts, KoinAllIn  # Import dari Brownie untuk jaringan, akun, dan kontrak

def main():
    # Menampilkan pesan koneksi ke mainnet
    print("Menghubungkan ke mainnet...")
    # Menghubungkan ke jaringan Ethereum mainnet
    network.connect('mainnet')

    # Menambahkan akun dari private key
    private_key = os.getenv('PRIVATE_KEY')  # Mengambil private key dari environment variable
    if not private_key:
        raise Exception(" environment variable tidak diatur")  # Error jika private key tidak ada
    accounts.add(private_key)  # Menambahkan akun ke Brownie
    deployer = accounts[-1]  # Mengambil akun yang baru ditambahkan

    # Menampilkan alamat akun deployer
    print(f"Deploy dari akun: {deployer.address}")

    # Menampilkan pesan deploy KoinAllIn
    print("Deploy KoinAllIn...")
    # Deploy KoinAllIn dengan supply awal
    initial_supply = 1000000  # 1 juta token (kontrak sudah handle desimal)
    token = KoinAllIn.deploy(initial_supply, {'from': deployer, 'gas_limit': 2000000, 'gas_price': network.gas_price()})

    # Menampilkan pesan sukses deploy
    print(f"Deploy berhasil! Alamat kontrak: {token.address}")
    print(f"Supply awal: {initial_supply}")
    print(f"Saldo deployer: {token.balanceOf(deployer)}")

if __name__ == "__main__":
    main()
