def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))

/*************  ✨ Windsurf Command 🌟  *************/
def gcd(a, b):
    """
    Return the greatest common divisor of two numbers a and b using the Euclidean algorithm.

    Parameters:
    a (int): the first number
    b (int): the second number

    Returns:
    int: the greatest common divisor of a and b
    """
    while b != 0:
        # Replace a with b and b with a % b
        a, b = b, a % b
    # When b is 0, return a as the greatest common divisor
    return a
/*******  cef54222-36db-4bad-8da7-6d0f19b3ee46  *******/

print("gcd(54, 24) =", gcd(54, 24))

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4

def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

