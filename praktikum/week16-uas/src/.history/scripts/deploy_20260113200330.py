from brownie import TinyCoin, accounts

def main():
    # Use the default account from Brownie
    acct = accounts[0]

    # Deploy contract with initial supply of 1000 TNC (1e18 = 1 token)
