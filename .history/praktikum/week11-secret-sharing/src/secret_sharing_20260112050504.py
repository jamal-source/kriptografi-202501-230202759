import random

class ShamirSecretSharing:
    def __init__(self, prime=2**127 - 1):  # Bilangan prima besar untuk finite field
        self.prime = prime

