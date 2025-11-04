import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))

/*************  ✨ Windsurf Command 🌟  *************/
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    """
    Calculate the time required to brute force a key space of given size.

    Parameters
    ----------
    keyspace_size : int
        The size of the key space to brute force.
    attempts_per_second : int, optional
        The number of attempts per second. Defaults to 1e6.

    Returns
    -------
    days : float
        The time required to brute force the key space in days.
    """
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days
/*******  8a756282-0e11-40a5-8337-3a7800a49a64  *******/

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
