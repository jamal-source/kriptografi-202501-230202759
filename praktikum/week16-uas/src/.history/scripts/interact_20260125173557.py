from brownie import TinyCoin, accounts

def main():
    # Get the deployed contract
    token = TinyCoin[-1]  # Get the most recently deployed contract

    # Use accounts
    acct1 = accounts[0]  # Deployer
    acct2 = accounts[1]  # Second account

    # Display initial balances
    print(f"Initial balance of account 1: {token.balanceOf(acct1) / 10**18} TNC")
    print(f"Initial balance of account 2: {token.balanceOf(acct2) / 10**18} TNC")

    # Transfer 100 TNC from account 1 to account 2
    transfer_amount = 100 * 10**18
    token.transfer(acct2, transfer_amount, {"from": acct1})

    # Display balances after transfer
    print(f"Balance of account 1 after transfer: {token.balanceOf(acct1) / 10**18} TNC")
    print(f"Balance of account 2 after transfer: {token.balanceOf(acct2) / 10**18} TNC")
