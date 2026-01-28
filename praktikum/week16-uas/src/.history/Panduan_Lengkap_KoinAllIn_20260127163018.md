# 🪙 Panduan Lengkap Proyek KoinAllIn (AIC) - ERC-20 Token dengan DApp MetaMask

## 📋 Daftar Isi
1. [Pendahuluan](#pendahuluan)
2. [Prasyarat Sistem](#prasyarat-sistem)
3. [Struktur Proyek](#struktur-proyek)
4. [Instalasi dan Setup](#instalasi-dan-setup)
5. [Pengembangan Kontrak Pintar](#pengembangan-kontrak-pintar)
6. [Deployment ke Ethereum Mainnet](#deployment-ke-ethereum-mainnet)
7. [Setup DApp MetaMask](#setup-dapp-metamask)
8. [Penggunaan DApp](#penggunaan-dapp)
9. [Proses Berhasil](#proses-berhasil)
10. [Kegagalan dan Troubleshooting](#kegagalan-dan-troubleshooting)
11. [Limitasi Transaksi](#limitasi-transaksi)
12. [Keamanan](#keamanan)
13. [Kesimpulan](#kesimpulan)

---

## 🎯 Pendahuluan

### Apa itu KoinAllIn (AIC)?
KoinAllIn (AIC) adalah token ERC-20 yang fully functional dengan fitur tambahan burning dan staking, dikembangkan menggunakan Solidity dan di-deploy ke jaringan utama Ethereum. Proyek ini mencakup:

- **Smart Contract ERC-20** dengan fungsi standar plus burning dan staking
- **Decentralized Application (DApp)** berbasis web dengan integrasi MetaMask
- **Deployment script** untuk mainnet menggunakan Brownie framework
- **Infura integration** untuk RPC provider
- **Comprehensive error handling** dan user experience yang baik

### Mengapa KoinAllIn?
- ✅ **Standar ERC-20** - Kompatibel dengan semua wallet dan exchange
- ✅ **Fitur Tambahan** - Burning untuk deflasi, staking untuk reward
- ✅ **User-Friendly** - Interface web modern dengan MetaMask
- ✅ **Secure** - Private keys tetap di MetaMask wallet
- ✅ **Real Token** - Bisa diperdagangkan di Ethereum mainnet

---

## 🔧 Prasyarat Sistem

### Hardware Requirements
- **RAM**: Minimum 8GB, recommended 16GB+
- **Storage**: 5GB free space
- **Internet**: Stable connection (untuk deployment dan transaksi)

### Software Requirements
- **Operating System**: Windows 10/11, Linux, atau macOS
- **Python**: Version 3.8 - 3.11
- **Node.js**: Version 16+ dengan npm
- **Git**: Untuk cloning repositories
- **MetaMask**: Browser extension (Chrome/Firefox/Edge)

### Akun dan API Keys
- **Infura Account**: https://infura.io/ (untuk Ethereum RPC)
- **Ethereum Wallet**: Dengan ETH untuk gas fees
- **Etherscan Account**: Opsional untuk contract verification

---

## 📁 Struktur Proyek

```
d:/Tinycoin/
├── kontrak/                    # Solidity contracts
│   ├── KoinAllIn.sol          # Main ERC-20 contract
│   └── TinyToken.sol          # Alternative contract
├── skrip/                      # Python scripts
│   ├── deploy_patched.py      # Mainnet deployment script
│   ├── deploy.py              # Development deployment
│   ├── interaksi.py           # Contract interaction
│   └── sebar.py               # Distribution script
├── bangun/                     # Build artifacts
│   ├── contracts/             # Compiled contracts
│   └── deployments/           # Deployment info
├── index.html                 # DApp interface
├── brownie-config.yaml        # Brownie configuration
├── Laporan_Penuh.md          # Project report
└── README.md                  # Basic documentation
```

---

