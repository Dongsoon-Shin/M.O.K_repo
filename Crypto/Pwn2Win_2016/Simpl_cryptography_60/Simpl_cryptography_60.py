from pwn import *

text = "071c1545_77_273829_0915140e_071d_2c213a2c343e_071b_4b515548545d_10_0f"
text = text.replace("_", "")

# XOR with all possible byte values
for i in range(255):
    r = ""
    for j in range(0, len(text), 2):
        d = int(text[j:j+2], 16)
        r += chr((d ^ i) % 256)

    # Re-insert underscores and print
    print i, ":", '_'.join([r[0:4], r[4:5], r[5:8], r[8:12], r[12:14],
                            r[14:20], r[20:22], r[22:28], r[28], r[29]])

