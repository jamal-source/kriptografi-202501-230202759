// Lisensi SPDX: MIT
pragma solidity ^0.8.0;

kontrak KoinKecil {
    string public nama = "KoinKecil";
    string public simbol = "KK";
    uint8 public desimal = 18;
    uint256 public totalPasokan;

    mapping(address => uint256) public saldoDari;
    mapping(address => mapping(address => uint256)) public izin;

    event Transfer(address indexed dari, address indexed ke, uint256 nilai);
    event Persetujuan(address indexed pemilik, address indexed pemberi, uint256 nilai);

    constructor(uint256 pasokanAwal) {
        totalPasokan = pasokanAwal * 10 ** desimal;
        saldoDari[msg.sender] = totalPasokan;
        emit Transfer(address(0), msg.sender, totalPasokan);
    }

    function kirim(address ke, uint256 nilai) public returns (bool) {
        require(saldoDari[msg.sender] >= nilai, "Saldo tidak cukup");
        saldoDari[msg.sender] -= nilai;
        saldoDari[ke] += nilai;
        emit Transfer(msg.sender, ke, nilai);
        return true;
    }

    function setujui(address pemberi, uint256 nilai) public returns (bool) {
        izin[msg.sender][pemberi] = nilai;
        emit Persetujuan(msg.sender, pemberi, nilai);
        return true;
    }

    function kirimDari(address dari, address ke, uint256 nilai) public returns (bool) {
        require(saldoDari[dari] >= nilai, "Saldo tidak cukup");
        require(izin[dari][msg.sender] >= nilai, "Izin tidak cukup");
        saldoDari[dari] -= nilai;
        saldoDari[ke] += nilai;
        izin[dari][msg.sender] -= nilai;
        emit Transfer(dari, ke, nilai);
        return true;
    }
}
