import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))

def brute_force_time(keyspace_size, attempts_per_second=1e6):
/*************  ✨ Windsurf Command ⭐  *************/
    """
    Estimates the time it takes to brute force a key with a given size.

    Parameters
    ----------
    keyspace_size : int
        The size of the key space to brute force.
    attempts_per_second : int, optional
        The number of attempts per second. Defaults to 1e6.

    Returns
    -------
    float
        The estimated time in days to brute force the key.
/*******  05b252f7-9353-4454-8d22-1934c42b0230  *******/
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
