// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/*
    TinyCoin (TNC)
    ======================
    ERC-20 Standard Token
    - OpenZeppelin v4.9.6
    - Mint saat deploy
    - Approve & transferFrom native
    - Burn token
    - Owner-controlled mint (testnet)
*/

import "@openzeppelin/contracts@4.9.6/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts@4.9.6/access/Ownable.sol";

contract TinyCoin is ERC20, Ownable {

    constructor() ERC20("TinyCoin", "TNC") {
        // Initial supply: 1,000,000 TNC
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
    }

    // Mint token (only owner)
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    // Burn token (by holder)
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
