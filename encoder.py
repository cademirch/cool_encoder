import sys
import base64
from random import choice


with open(sys.argv[1], "rb") as fh:
    text = base64.b64encode(fh.read())
    n = 150  # chunk length
    chunks = [text[i : i + n] for i in range(0, len(text), n)]
    for i, chunk in enumerate(chunks):
        read_name = f"@read{i}"
        seq = "".join(choice(["A", "C", "T", "G"]) for i in range(150))
        sep = "+"
        qual = chunk.decode()
        print(read_name, seq, sep, qual, sep="\n")
