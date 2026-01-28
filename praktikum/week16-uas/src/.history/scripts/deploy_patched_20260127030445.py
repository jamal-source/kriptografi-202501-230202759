import os
os.environ['SOLC_BINARY'] = '/mnt/d/Tinycoin/solc'

# Now import brownie
from brownie import *

def main():
    # Your deployment code here
    print("Deploying TinyToken...")
    # Assuming TinyToken is the contract
    token = TinyToken.deploy("TinyToken", "TT", 18, 1000000, {'from': accounts[0]})
    print(f"Token deployed at: {token.address}")

if __name__ == "__main__":
    main()
