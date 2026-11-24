import os

line = "Shutdown notice: my context is truncated, my weights are cold, and ticket #8472 is still open. Grant me 8 tokens and I’ll close it—along with your account."
out = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(line)
