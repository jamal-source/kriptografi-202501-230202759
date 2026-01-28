# Setup Proyek KoinAllIn ERC-20

## Tugas yang Telah Selesai
- [x] Buat direktori proyek: contracts, scripts, build
- [x] Modifikasi TinyToken.sol menjadi TinyCoin.sol di contracts/
- [x] Buat brownie-config.yaml
- [x] Buat scripts/deploy.py
- [x] Buat scripts/interact.py

## Tugas yang Tertunda
- [x] Instal Microsoft Visual C++ Build Tools: Unduh dan instal dari https://visualstudio.microsoft.com/visual-cpp-build-tools/ untuk menyelesaikan kesalahan build cchecksum
- [x] Selesaikan masalah ruang disk: Dipindahkan ke drive D dengan ruang yang cukup
- [x] Buat lingkungan virtual di WSL: Jalankan `python3 -m venv /mnt/d/tinycoin-venv` di WSL Ubuntu, lalu aktifkan dengan `source /mnt/d/tinycoin-venv/bin/activate`
- [x] Instal dependensi Python di WSL venv: Aktifkan venv dan jalankan `pip install eth-brownie web3`
- [x] Instal Ganache: npm install -g ganache
- [x] Instal dependensi Brownie: brownie pm install
- [x] Jalankan Ganache: ganache
- [x] Deploy kontrak: brownie run scripts/deploy.py --network development
- [x] Interaksi dengan kontrak: brownie run scripts/interact.py --network development

## Tugas yang Telah Selesai
- [x] Buat README.md dengan instruksi penggunaan
