import os
from brownie import network, accounts, TinyToken

def main():
    print("Connecting to mainnet...")
    network.connect('mainnet')

    # Add account from private key
    private_key = os.getenv('PRIVATE_KEY')
    if not private_key:
        raise Exception("PRIVATE_KEY environment variable not set")
    accounts.add(private_key)
    deployer = accounts[-1]  # The added account

    print(f"Deploying from account: {deployer.address}")

    print("Deploying TinyToken...")
    # Deploy TinyToken with initial supply
    initial_supply = 1000000 * 10**18  # 1 million tokens with 18 decimals
    token = TinyToken.deploy(initial_supply, {'from': deployer, 'gas_limit': 2000000, 'gas_price': network.gas_price()})

    print(f"Deployment successful! Contract address: {token.address}")
    print(f"Initial supply: {initial_supply}")
    print(f"Deployer balance: {token.balanceOf(deployer)}")

if __name__ == "__main__":
    main()
