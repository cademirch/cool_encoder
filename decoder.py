import sys
import base64
from random import choice


with open(sys.argv[1], "r") as fh:
    text = []
    for i, line in enumerate(fh):
        if line.startswith("+"):
            line = next(fh)
            line = line.strip()
            text.append(bytes(line, "utf-8"))

out_text = b"".join(text)
fh = open("out.mp4", "wb")
fh.write(base64.b64decode(out_text + b"=="))
fh.close()
