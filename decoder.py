import sys
import base64
from random import choice


with open(sys.argv[1], "r") as fh:
    text = b""
    for i, line in enumerate(fh):
        if line.startswith("+"):
            line = next(fh)
            line = line.strip()
            text += bytes(line, "utf-8")


fh = open("out.mp3", "wb")
fh.write(base64.b64decode(text + b"=="))
fh.close()
