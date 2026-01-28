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
        raise Exception("PRIVATE_KEY environment variable tidak diatur")  # Error jika private key tidak ada
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
    print(f"Saldo deployer: {token.saldoDari(deployer)}")

    # Informasi untuk MetaMask
    print("\n" + "="*60)
    print("🦊 INFORMASI UNTUK MENAMBAHKAN KOINALLIN (AIC) KE METAMASK:")
    print("="*60)
    print(f"📋 Contract Address: {token.address}")
    print(f"🏷️  Token Symbol: AIC")
    print(f"🔢 Decimals: 18")
    print("="*60)
    print("📱 LANGKAH-LANGKAH MENAMBAHKAN KE METAMASK:")
    print("1. Buka MetaMask dan pastikan terhubung ke Ethereum Mainnet")
    print("2. Klik 'Import Tokens' di bagian bawah wallet")
    print("3. Pilih 'Custom Token'")
    print("4. Masukkan Contract Address di atas")
    print("5. Symbol: AIC, Decimals: 18")
    print("6. Klik 'Add Custom Token'")
    print("="*60)
    print("✅ Token AIC siap digunakan di MetaMask!")
    print("💡 Simpan contract address ini untuk verifikasi di Etherscan")
    print("="*60)

if __name__ == "__main__":
    main()
