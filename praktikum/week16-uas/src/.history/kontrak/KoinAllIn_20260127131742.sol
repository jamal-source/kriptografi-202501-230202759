// SPDX-License-Identifier: MIT
    string public nama = "KoinAllIn";
    string public simbol = "AIC";
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

    function bakar(uint256 nilai) public returns (bool) {
        require(saldoDari[msg.sender] >= nilai, "Saldo tidak cukup untuk dibakar");
        saldoDari[msg.sender] -= nilai;
        totalPasokan -= nilai;
        emit Transfer(msg.sender, address(0), nilai);
        return true;
    }

    mapping(address => uint256) public taruhan;
    uint256 public totalTaruhan;

    function taruh(uint256 nilai) public {
        require(saldoDari[msg.sender] >= nilai, "Saldo tidak cukup untuk ditaruh");
        saldoDari[msg.sender] -= nilai;
        taruhan[msg.sender] += nilai;
        totalTaruhan += nilai;
    }

    function tarikTaruhan(uint256 nilai) public {
        require(taruhan[msg.sender] >= nilai, "Taruhan tidak cukup");
        taruhan[msg.sender] -= nilai;
        totalTaruhan -= nilai;
        saldoDari[msg.sender] += nilai;
    }

    function dapatkanReward() public view returns (uint256) {
        // Reward sederhana berdasarkan taruhan
        return taruhan[msg.sender] / 10; // 10% reward
    }
}
