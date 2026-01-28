# Proyek Token KoinAllIn ERC-20

Proyek ini membuat token TinyCoin (TNC) ERC-20 menggunakan Python, Brownie, Web3.py, dan Ganache.

## Prasyarat

- Python 3.8+
- Node.js dan npm
- Microsoft Visual C++ 14.0 atau lebih tinggi (untuk Windows, instal dari https://visualstudio.microsoft.com/visual-cpp-build-tools/)

## Instalasi

1. Instal dependensi Python:
   ```bash
   pip install eth-brownie web3
   ```

   Jika Anda mengalami kesalahan build, coba instal di lingkungan virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  
   pip install eth-brownie web3
   ```

2. Instal Ganache:
   ```bash
   npm install -g ganache
   ```

3. Instal dependensi Brownie:
   ```bash
   brownie pm install
   ```

## Struktur Proyek

```
tinycoin-python/
├─ contracts/
│   └─ TinyCoin.sol
├─ scripts/
│   ├─ deploy.py
│   └─ interact.py
├─ build/
├─ brownie-config.yaml
├─ README.md
└─ TODO.md
```

## Penggunaan

1. Mulai Ganache (blockchain lokal):
   ```bash
   ganache
   ```

2. Deploy kontrak KoinAllIn:
   ```bash
   brownie run skrip/deploy_patched.py --network mainnet
   ```

3. Interaksi dengan kontrak (transfer token dan periksa saldo):
   ```bash
   brownie run skrip/interaksi.py --network mainnet
   ```

## Detail Kontrak

- **Nama**: KoinAllIn
- **Simbol**: AIC
- **Pasokan Awal**: 1,000,000 AIC (dideploy ke akun pertama)
- **Desimal**: 18 (standar ERC-20)
- **Fitur**: Burning, Staking

## Skrip

- `deploy_patched.py`: Deploy kontrak KoinAllIn dengan pasokan awal dan integrasi MetaMask.
- `interaksi.py`: Interaksi dengan kontrak (transfer token dan periksa saldo).
