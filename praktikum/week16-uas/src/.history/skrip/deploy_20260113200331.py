from brownie import TinyCoin, accounts

def main():
    # Use the default account from Brownie
    acct = accounts[0]

    # Deploy contract with initial supply of 1000 TNC (1e18 = 1 token)
    initial_supply = 1000 * 10**18
    token = TinyCoin.deploy(initial_supply, {"from": acct})

    print(f"Contract deployed at: {token.address}")
    print(f"Deployer balance: {token.balanceOf(acct) / 10**18} TNC")
