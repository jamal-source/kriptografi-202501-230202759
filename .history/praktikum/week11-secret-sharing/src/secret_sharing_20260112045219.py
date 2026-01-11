import random

class ShamirSecretSharing:
    def __init__(self, prime=7):  # Small prime for testing
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
            term = yi
            for j, (xj, _) in enumerate(points):
                if i != j:
                    term = term * (x - xj) * self._mod_inverse((xi - xj) % self.prime, self.prime) % self.prime
            result = (result + term) % self.prime
        return result

    def split_secret(self, secret, n, k):
        """Split secret into n shares, requiring k shares to reconstruct"""
        if secret >= self.prime:
            raise ValueError("Secret too large for prime field")

        # Generate random coefficients for polynomial of degree k-1
        coeffs = [secret] + [random.randint(0, self.prime - 1) for _ in range(k - 1)]

        # Generate n shares
        shares = []
        for i in range(1, n + 1):
            y = self._evaluate_polynomial(coeffs, i)
            shares.append((i, y))

        return shares

    def reconstruct_secret(self, shares):
        """Reconstruct secret from shares using Lagrange interpolation"""
        return self._lagrange_interpolation(shares)

# Demo
if __name__ == "__main__":
    sss = ShamirSecretSharing()

    # Example: Split secret 5 into 3 shares, requiring 2 to reconstruct
    secret = 5
    n = 3  # Total shares
    k = 2  # Threshold

    print(f"Original secret: {secret}")

    # Split secret
    shares = sss.split_secret(secret, n, k)
    print(f"Generated {n} shares:")
    for share in shares:
        print(f"  Share {share[0]}: {share[1]}")

    # Reconstruct with different combinations
    print("\nReconstructing with different combinations:")

    # Test with k shares
    subset_k = shares[:k]
    reconstructed = sss.reconstruct_secret(subset_k)
    print(f"With {k} shares {subset_k}: Reconstructed secret = {reconstructed}")

    # Test with more than k shares
    subset_more = shares[:k+1]
    reconstructed = sss.reconstruct_secret(subset_more)
    print(f"With {k+1} shares {subset_more}: Reconstructed secret = {reconstructed}")

    # Test with less than k shares (should fail)
    subset_less = shares[:k-1]
    reconstructed = sss.reconstruct_secret(subset_less)
    print(f"With {k-1} shares {subset_less}: Reconstructed secret = {reconstructed} (incorrect)")
