import string
import collections

def caesar_brute_force(ciphertext, max_shift=25):
    """
    Melakukan serangan brute force pada cipher Caesar
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
    Melakukan analisis frekuensi pada teks
    """
    text = text.upper()
    freq = collections.Counter(c for c in text if c.isalpha())
    total = sum(freq.values())
    freq_percent = {char: (count / total) * 100 for char, count in freq.items()}
    return dict(sorted(freq_percent.items()))

def vigenere_attack(ciphertext, key_length):
    """
    Mencoba memecahkan cipher Vigenere dengan panjang kunci diketahui
    """
    ciphertext = ciphertext.upper()
    groups = ['' for _ in range(key_length)]
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            groups[i % key_length] += char

    # Analisis frekuensi untuk setiap grup
    group_freqs = [frequency_analysis(group) for group in groups]

    # Tebak kunci berdasarkan huruf yang paling sering muncul (mengasumsikan 'E' paling umum)
    key = ""
    for freq in group_freqs:
        if freq:
            most_common = max(freq, key=freq.get)
            # Mengasumsikan 'E' paling umum, shift = (most_common - 'E') % 26
            shift = (ord(most_common) - ord('E')) % 26
            key += chr(shift + ord('A'))
        else:
            key += 'A'

    return key, group_freqs

# Contoh penggunaan
if __name__ == "__main__":
    # Contoh cipher Caesar
    caesar_ciphertext = "WKLV LV D VHFUHW PHVVDJH"
    print("Serangan Brute Force Caesar Cipher:")
    caesar_results = caesar_brute_force(caesar_ciphertext)
    for shift, plaintext in caesar_results[:5]:  # Tampilkan 5 pertama
        print(f"Shift {shift}: {plaintext}")

    # Contoh analisis frekuensi
    sample_text = "THIS IS A SAMPLE TEXT FOR FREQUENCY ANALYSIS"
    print("\nAnalisis Frekuensi:")
    freq = frequency_analysis(sample_text)
    for char, percent in freq.items():
        print(f"{char}: {percent:.2f}%")

    # Contoh serangan Vigenere
    vigenere_ciphertext = "WKLVLVDFLSKHUBWH[W"
    key_length = 3
    print(f"\nSerangan Vigenere (panjang kunci {key_length}):")
    guessed_key, group_freqs = vigenere_attack(vigenere_ciphertext, key_length)
    print(f"Kunci yang diperkirakan: {guessed_key}")
