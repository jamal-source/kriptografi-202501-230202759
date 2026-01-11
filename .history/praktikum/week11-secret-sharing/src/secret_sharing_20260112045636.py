import random

class ShamirSecretSharing:
    def __init__(self, prime=2**127 - 1):  # Large prime for finite field
        self.prime = prime

    def _mod_inverse(self, a, m):
        """Extended Euclidean algorithm for modular inverse"""
        m0, y, x = m, 0, 1
        if m == 1:
            return 0
        while a > 1:
            q = a // m
            m, a = a % m, m
            y, x = x - q * y, y
        if x < 0:
            x += m0
        return x

    def _evaluate_polynomial(self, coeffs, x):
        """Evaluate polynomial at point x"""
        result = 0
        for coeff in reversed(coeffs):
            result = (result * x + coeff) % self.prime
        return result

    def _lagrange_interpolation(self, points, x=0):
        """Lagrange interpolation to find f(0)"""
        result = 0
        for i, (xi, yi) in enumerate(points):
            L = 1
