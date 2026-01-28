import os
os.environ['SOLC_BINARY'] = '/mnt/d/Tinycoin/solc'

# Compile contracts manually using py-solc-x
from solcx import compile_source
from brownie import network, accounts

def compile_contracts():
    # Read the contract source
    with open('contracts/TinyCoin.sol', 'r') as f:
        source = f.read()
    
    # Compile
    compiled = compile_source(source, solc_version='0.8.0')
    return compiled

def main():
    print("Compiling contracts...")
    try:
        compiled = compile_contracts()
        print("Compilation successful")
    except Exception as e:
        print(f"Compilation failed: {e}")
        return
    
    # Connect to network
    network.connect('development')
    
    print("Deploying TinyCoin...")
    # Deploy TinyCoin with initial supply
    token = TinyCoin.deploy(1000000, {'from': accounts[0]})
    print(f"Token deployed at: {token.address}")
    
    # Test token transfer
    print("Testing token transfer...")
    recipient = accounts[1]
    amount = 100
    token.transfer(recipient, amount, {'from': accounts[0]})
    print(f"Transferred {amount} tokens to {recipient}")
    print(f"Recipient balance: {token.balanceOf(recipient)}")
    print(f"Deployer balance: {token.balanceOf(accounts[0])}")

if __name__ == "__main__":
    main()
