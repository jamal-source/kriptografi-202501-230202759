import random

class ShamirSecretSharing:
    def __init__(self, prime=2**127 - 1):  # Bilangan prima besar untuk finite field
        self.prime = prime

    def _mod_inverse(self, a, m):
        """Algoritma Euclidean diperluas untuk invers modular"""
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
        """Evaluasi polinomial pada titik x"""
        result = 0
        for coeff in reversed(coeffs):
            result = (result * x + coeff) % self.prime
        return result

    def _lagrange_interpolation(self, points, x=0):
        """Interpolasi Lagrange untuk menemukan f(0)"""
        result = 0
        for i, (xi, yi) in enumerate(points):
            L = 1
            for j, (xj, _) in enumerate(points):
                if i != j:
                    L = L * (-xj % self.prime) * self._mod_inverse((xi - xj) % self.prime, self.prime) % self.prime
            result = (result + yi * L) % self.prime
        return result

    def split_secret(self, secret, n, k):
        """Bagi rahasia menjadi n shares, memerlukan k shares untuk rekonstruksi"""
        if secret >= self.prime:
            raise ValueError("Rahasia terlalu besar untuk field prima")

        # Hasilkan koefisien acak untuk polinomial derajat k-1
        coeffs = [secret] + [random.randint(0, self.prime - 1) for _ in range(k - 1)]

        # Hasilkan n shares
        shares = []
        for i in range(1, n + 1):
            y = self._evaluate_polynomial(coeffs, i)
            shares.append((i, y))

        return shares

    def reconstruct_secret(self, shares):
        """Rekonstruksi rahasia dari shares menggunakan interpolasi Lagrange"""
        return self._lagrange_interpolation(shares)

# Demo
if __name__ == "__main__":
    sss = ShamirSecretSharing()

    # Contoh: Bagi rahasia 12345 menjadi 5 shares, memerlukan 3 untuk rekonstruksi
    secret = 12345
    n = 5  # Total shares
    k = 3  # Threshold

    print(f"Rahasia asli: {secret}")

    # Bagi rahasia
    shares = sss.split_secret(secret, n, k)
    print(f"Menghasilkan {n} shares:")
    for share in shares:
        print(f"  Share {share[0]}: {share[1]}")

    # Rekonstruksi dengan kombinasi berbeda
    print("\nMerekonstruksi dengan kombinasi berbeda:")

    # Uji dengan k shares
    subset_k = shares[:k]
    reconstructed = sss.reconstruct_secret(subset_k)
    print(f"Dengan {k} shares {subset_k}: Rahasia yang direkonstruksi = {reconstructed}")

    # Uji dengan lebih dari k shares
    subset_more = shares[:k+1]
    reconstructed = sss.reconstruct_secret(subset_more)
    print(f"Dengan {k+1} shares {subset_more}: Rahasia yang direkonstruksi = {reconstructed}")

    # Uji dengan kurang dari k shares (harus gagal)
    subset_less = shares[:k-1]
    reconstructed = sss.reconstruct_secret(subset_less)
    print(f"Dengan {k-1} shares {subset_less}: Rahasia yang direkonstruksi = {reconstructed} (salah)")
