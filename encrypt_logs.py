# encrypt_logs.py
# Helper script used ONLY to create the dummy encrypted file raw_logs.txt.
# It applies a Caesar RIGHT-shift of 3 to letters (with wrap-around Z -> C).
# Spaces, newlines, digits and punctuation are left unchanged.

SHIFT = 3

plain_file = open("plain_logs_sample.txt", "r")
raw_file = open("raw_logs.txt", "w")

for line in plain_file:
    encrypted = ""
    for ch in line:
        if "A" <= ch <= "Z":
            encrypted += chr((ord(ch) - ord("A") + SHIFT) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            encrypted += chr((ord(ch) - ord("a") + SHIFT) % 26 + ord("a"))
        else:
            encrypted += ch
    raw_file.write(encrypted)

plain_file.close()
raw_file.close()
print("raw_logs.txt created.")
