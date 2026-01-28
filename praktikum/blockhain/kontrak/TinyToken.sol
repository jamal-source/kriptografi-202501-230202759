// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin via GitHub release tag (pastikan versi valid)
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.9.3/contracts/token/ERC20/ERC20.sol";

contract TinyToken is ERC20 {
    // initialSupply in whole tokens (e.g. 1000000 = 1.000.000 token)
    constructor(uint256 initialSupply) ERC20("TinyToken", "TINY") {
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }
}
