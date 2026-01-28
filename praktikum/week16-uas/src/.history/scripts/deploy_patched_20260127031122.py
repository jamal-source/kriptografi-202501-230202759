import os
os.environ['SOLC_BINARY'] = '/mnt/d/Tinycoin/solc'

# Compile contracts manually using py-solc-x
from solcx import compile_source
from brownie import network, accounts, Contract

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
    
    # Get contract data
    contract_id = '<stdin>:TinyCoin'
    abi = compiled[contract_id]['abi']
    bytecode = compiled[contract_id]['bin']
    
    print("Deploying TinyCoin...")
    # Deploy TinyCoin with initial supply
    token = Contract.from_abi('TinyCoin', '0x0000000000000000000000000000000000000000', abi)
    tx = accounts[0].transfer(data=bytecode + '00000000000000000000000000000000000000000000000000000000000f4240', gas_limit=6721975)
    token = Contract.from_abi('TinyCoin', tx.contract_address, abi)
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
