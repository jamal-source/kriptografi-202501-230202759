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
        'TinyToken.sol'
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

    # Connect to mainnet
    network.connect('mainnet')

    # Add account from private key
    private_key = os.getenv('PRIVATE_KEY')
    if not private_key:
        raise Exception("PRIVATE_KEY environment variable not set")
    accounts.add(private_key)
    deployer = accounts[-1]  # The added account

    # Get contract data
    print("Available contract keys:", list(compiled['contracts'].keys()))
    contract_id = list(compiled['contracts'].keys())[0]  # Use the first available key
    print(f"Using contract_id: {contract_id}")
    abi = compiled['contracts'][contract_id]['abi']
    bytecode = compiled['contracts'][contract_id]['bin']

    print("Deploying TinyToken...")
    # Deploy TinyToken with initial supply
    initial_supply = 1000000 * 10**18  # 1 million tokens with 18 decimals
    token = Contract.from_abi('TinyToken', abi, bytecode)
    tx = token.deploy(initial_supply, {'from': deployer, 'gas_limit': 2000000, 'gas_price': network.gas_price()})
    print(f"Token deployed at: {tx.contract_address}")
    # Get the deployed contract instance
    token = Contract(tx.contract_address, abi=abi)

    print(f"Deployment successful! Contract address: {tx.contract_address}")
    print(f"Initial supply: {initial_supply}")
    print(f"Deployer balance: {token.balanceOf(deployer)}")

if __name__ == "__main__":
    main()
