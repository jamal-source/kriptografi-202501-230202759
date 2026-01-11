import string
import collections

def caesar_brute_force(ciphertext, max_shift=25):
    """
    Perform brute force attack on Caesar cipher
    """
    results = []
    for shift in range(max_shift + 1):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                plaintext += chr((ord(char) - base - shift) % 26 + base)
            else:
                plaintext += char
        results.append((shift, plaintext))
    return results

def frequency_analysis(text):
    """
    Perform frequency analysis on text
    """
    text = text.upper()
    freq = collections.Counter(c for c in text if c.isalpha())
    total = sum(freq.values())
    freq_percent = {char: (count / total) * 100 for char, count in freq.items()}
    return dict(sorted(freq_percent.items()))

def vigenere_attack(ciphertext, key_length):
    """
    Attempt to break Vigenere cipher with known key length
    """
    ciphertext = ciphertext.upper()
    groups = ['' for _ in range(key_length)]
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            groups[i % key_length] += char

    # Frequency analysis for each group
    group_freqs = [frequency_analysis(group) for group in groups]

    # Guess key based on most frequent letter (assuming 'E' is most common)
    key = ""
    for freq in group_freqs:
        if freq:
            most_common = max(freq, key=freq.get)
            # Assuming 'E' is most common, shift = (most_common - 'E') % 26
            shift = (ord(most_common) - ord('E')) % 26
            key += chr(shift + ord('A'))
        else:
            key += 'A'

    return key, group_freqs

# Example usage
if __name__ == "__main__":
    # Caesar cipher example
    caesar_ciphertext = "WKLV LV D VHFUHW PHVVDJH"
    print("Caesar Cipher Brute Force:")
    caesar_results = caesar_brute_force(caesar_ciphertext)
    for shift, plaintext in caesar_results[:5]:  # Show first 5
        print(f"Shift {shift}: {plaintext}")

    # Frequency analysis example
    sample_text = "THIS IS A SAMPLE TEXT FOR FREQUENCY ANALYSIS"
    print("\nFrequency Analysis:")
    freq = frequency_analysis(sample_text)
    for char, percent in freq.items():
        print(f"{char}: {percent:.2f}%")

    # Vigenere attack example
    vigenere_ciphertext = "WKLVLVDFLSKHUBWH[W"
    key_length = 3
    print(f"\nVigenere Attack (key length {key_length}):")
    guessed_key, group_freqs = vigenere_attack(vigenere_ciphertext, key_length)
    print(f"Guessed key: {guessed_key}")
