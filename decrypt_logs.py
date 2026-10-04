# decrypt_logs.py
# Security Log Decryptor - Caesar cipher (left shift of 3)
#
# Reads raw_logs.txt, decrypts every line, saves ALL decrypted lines to
# decrypted_master.txt and saves every line that contains "BREACH"
# (in any letter case) to security_alerts.txt.
#
# Only basic file input/output, ord(), chr(), string methods,
# for loops and if statements are used.

SHIFT = 3

# ---------- Task 1: File ingestion and output preparation ----------
input_file = open("raw_logs.txt", "r")
master_file = open("decrypted_master.txt", "w")
alert_file = open("security_alerts.txt", "w")

total_lines = 0
alert_lines = 0

# ---------- Task 2: Caesar decryption, line by line ----------
for line in input_file:
    decrypted = ""

    for ch in line:
        if "A" <= ch <= "Z":
            # uppercase letter: left shift with wrap-around (A -> X)
            decrypted += chr((ord(ch) - ord("A") - SHIFT) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            # lowercase letter: left shift with wrap-around (a -> x)
            decrypted += chr((ord(ch) - ord("a") - SHIFT) % 26 + ord("a"))
        else:
            # spaces, newlines, digits and punctuation are preserved
            decrypted += ch

    # ---------- Task 3: Parsing and file writing ----------
    decrypted = decrypted.strip()          # remove leading/trailing whitespace

    if decrypted != "":                    # ignore completely blank lines
        master_file.write(decrypted + "\n")    # every line goes to master file
        total_lines += 1

        # Case-insensitive keyword check using upper()
        if "BREACH" in decrypted.upper():
            alert_file.write(decrypted + "\n")
            alert_lines += 1

input_file.close()
master_file.close()
alert_file.close()

print("Decryption complete.")
print("Lines decrypted  :", total_lines)
print("Breach alerts    :", alert_lines)
print("Output files     : decrypted_master.txt, security_alerts.txt")
