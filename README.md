# Caesar Log Decryptor

Python 3 program that decrypts a Caesar-shifted (shift = 3) server log, saves every
decrypted line to `decrypted_master.txt`, and copies every line containing the word
"BREACH" (any letter case) to `security_alerts.txt`.

## Files
| File | Purpose |
|---|---|
| `decrypt_logs.py` | Main solution (Tasks 1-3) |
| `raw_logs.txt` | Encrypted dummy input (8 lines) |
| `decrypted_master.txt` | Output: all decrypted lines |
| `security_alerts.txt` | Output: lines containing BREACH |
| `encrypt_logs.py` | Helper used once to create `raw_logs.txt` |
| `plain_logs_sample.txt` | Plain-text source used by the helper (for verification) |

## Run
```
python decrypt_logs.py
```
No external libraries are required. The script uses no lists, dictionaries, sets,
custom functions or imports.
