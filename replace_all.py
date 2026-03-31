import re
import os

files = [
    "c:/Users/euand/Documents/MY JOB/2026/AdNove/Prospecções/Março/Maria Moura/listagem_de_produtos.html",
    "c:/Users/euand/Documents/MY JOB/2026/AdNove/Prospecções/Março/Maria Moura/pagina_do_produto.html",
    "c:/Users/euand/Documents/MY JOB/2026/AdNove/Prospecções/Março/Maria Moura/carrinho_de_compras.html"
]

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

def replace_images(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    idx = 0
    def repl(match):
        nonlocal idx
        url = urls[idx % len(urls)]
        idx += 1
        return 'src="' + url + '"'
    
    # Target lh3.googleusercontent.com links
    new_html = re.sub(r'src="https://lh3\.googleusercontent\.com[^"]+"', repl, html)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    
    print(f"Processed {os.path.basename(file_path)}: replaced {idx} images.")

for f in files:
    if os.path.exists(f):
        replace_images(f)
    else:
        print(f"File not found: {f}")
