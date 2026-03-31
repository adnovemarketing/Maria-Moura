import re
import sys

file_path = "c:/Users/euand/Documents/MY JOB/2026/AdNove/Prospecções/Março/Maria Moura/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

urls = [
    "https://i.postimg.cc/dVqMTKbY/1.png",
    "https://i.postimg.cc/W12RJPBt/2.png",
    "https://i.postimg.cc/0y8gJqTq/3.png",
    "https://i.postimg.cc/65VJ3QmK/4.png",
    "https://i.postimg.cc/3JQQYG9k/5.png",
    "https://i.postimg.cc/wTYYgNFV/6.png",
    "https://i.postimg.cc/fTQQDd50/7.png",
    "https://i.postimg.cc/3rvQs1Xz/8.png",
    "https://i.postimg.cc/05w1TnGs/9.png",
    "https://i.postimg.cc/kMbP0sNC/10.png"
]

idx = 0
def repl(match):
    global idx
    if idx < len(urls):
        url = urls[idx]
        idx += 1
    else:
        # For any extra images, we just use the last URL or a placeholder, let's use the 10th one.
        url = urls[-1]
    return 'src="' + url + '"'

new_html = re.sub(r'src="https://lh3\.googleusercontent\.com[^"]+"', repl, html)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_html)

print(f"Replaced {idx} images.")
