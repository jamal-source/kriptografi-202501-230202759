import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Patch the _get_solc_version_list function to avoid GitHub connection
def patch_brownie():
    try:
        from brownie.project.compiler import solidity
        original_get_solc_version_list = solidity._get_solc_version_list

        def patched_get_solc_version_list():
            # Return a list with the required version
            return (['0.8.0'], [])

        solidity._get_solc_version_list = patched_get_solc_version_list
        print("Brownie patched successfully")
    except ImportError as e:
        print(f"Failed to patch Brownie: {e}")

patch_brownie()

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
