import os
import subprocess
import json
from brownie import network, accounts, Contract

def compile_contracts():
    # Use subprocess to call the local solc binary directly
    solc_path = '/mnt/d/Tinycoin/solc'
    
    # Compile the contract
    result = subprocess.run([
        solc_path, 
        '--combined-json', 'abi,bin', 
        'contracts/TinyCoin.sol'
    ], capture_output=True, text=True, cwd='/mnt/d/Tinycoin')
    
    if result.returncode != 0:
        raise Exception(f"Solc compilation failed: {result.stderr}")
    
    # Parse the output
    compiled = json.loads(result.stdout)
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
    
    # Get contract data - debug the keys first
    print("Available contract keys:", list(compiled['contracts'].keys()))
    contract_id = list(compiled['contracts'].keys())[0]  # Use the first available key
    print(f"Using contract_id: {contract_id}")
    abi = compiled['contracts'][contract_id]['abi']
    bytecode = compiled['contracts'][contract_id]['bin']
    
    print("Deploying TinyCoin...")
    # Deploy TinyCoin with initial supply using proper Brownie deployment
    initial_supply = 1000000 * 10**18  # 1 million tokens with 18 decimals
    token = Contract.from_abi('TinyCoin', abi, bytecode)
    tx = token.deploy(initial_supply, {'from': accounts[0], 'gas_limit': 6721975})
    print(f"Token deployed at: {tx.contract_address}")
    # Get the deployed contract instance
    token = Contract(tx.contract_address, abi=abi)
    
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
