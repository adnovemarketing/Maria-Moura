import re
import os

files = [
    "c:/Users/euand/Documents/MY JOB/2026/AdNove/Prospecções/Março/Maria Moura/index.html",
    "c:/Users/euand/Documents/MY JOB/2026/AdNove/Prospecções/Março/Maria Moura/listagem_de_produtos.html",
    "c:/Users/euand/Documents/MY JOB/2026/AdNove/Prospecções/Março/Maria Moura/pagina_do_produto.html",
    "c:/Users/euand/Documents/MY JOB/2026/AdNove/Prospecções/Março/Maria Moura/carrinho_de_compras.html"
]

header_html = """
<!-- TopAppBar -->
<header class="bg-[#faf9f6]/90 dark:bg-stone-900/90 backdrop-blur-md full-width top-0 sticky z-50 transition-all duration-300">
  <div class="flex justify-between items-center px-6 md:px-8 py-4 w-full max-w-screen-2xl mx-auto">
    <div class="flex items-center gap-4 md:gap-8">
      <button class="md:hidden text-[#865140]" onclick="document.getElementById('mobile-menu').classList.remove('hidden')">
        <span class="material-symbols-outlined text-3xl">menu</span>
      </button>
      <a href="index.html" class="font-serif text-xl md:text-2xl font-bold tracking-tighter text-[#865140] dark:text-[#c28471]">MARIA MOURA</a>
      <nav class="hidden md:flex items-center space-x-8 font-serif text-lg tracking-wide">
        <a class="nav-link text-[#5f5e5e] hover:text-[#865140] transition-colors" href="index.html">Novidades</a>
        <a class="nav-link text-[#5f5e5e] hover:text-[#865140] transition-colors" href="listagem_de_produtos.html">Coleções</a>
        <a class="nav-link text-[#5f5e5e] hover:text-[#865140] transition-colors" href="listagem_de_produtos.html">Blusas</a>
        <a class="nav-link text-[#5f5e5e] hover:text-[#865140] transition-colors" href="listagem_de_produtos.html">Calças</a>
        <a class="nav-link text-[#5f5e5e] hover:text-[#865140] transition-colors" href="listagem_de_produtos.html">Sale</a>
      </nav>
    </div>
    <div class="flex items-center space-x-4 md:space-x-6 text-[#865140] dark:text-[#c28471]">
      <button class="hover:opacity-80 transition-opacity duration-300 scale-95 active:duration-150">
        <span class="material-symbols-outlined">person</span>
      </button>
      <a href="carrinho_de_compras.html" class="hover:opacity-80 transition-opacity duration-300 scale-95 active:duration-150 relative">
        <span class="material-symbols-outlined">shopping_bag</span>
      </a>
    </div>
  </div>
  <!-- Mobile Menu Overlay -->
  <div id="mobile-menu" class="hidden fixed inset-0 z-[100] bg-[#faf9f6]/98 backdrop-blur-xl flex flex-col p-8 space-y-8 overflow-y-auto">
    <div class="flex justify-between items-center">
      <span class="font-serif text-2xl font-bold tracking-tighter text-[#865140]">MARIA MOURA</span>
      <button onclick="document.getElementById('mobile-menu').classList.add('hidden')">
        <span class="material-symbols-outlined text-4xl text-[#865140]">close</span>
      </button>
    </div>
    <nav class="flex flex-col space-y-6 font-serif text-3xl tracking-wide text-stone-800 pt-12">
      <a href="index.html" onclick="document.getElementById('mobile-menu').classList.add('hidden')">Novidades</a>
      <a href="listagem_de_produtos.html" onclick="document.getElementById('mobile-menu').classList.add('hidden')">Coleções</a>
      <a href="listagem_de_produtos.html" onclick="document.getElementById('mobile-menu').classList.add('hidden')">Blusas</a>
      <a href="listagem_de_produtos.html" onclick="document.getElementById('mobile-menu').classList.add('hidden')">Calças</a>
      <a href="listagem_de_produtos.html" onclick="document.getElementById('mobile-menu').classList.add('hidden')">Sale</a>
    </nav>
    <div class="mt-auto pt-8 border-t border-stone-200 flex flex-col gap-6 text-stone-500 font-serif text-xl">
      <a href="#">Minha Conta</a>
      <a href="carrinho_de_compras.html" class="flex items-center justify-between">
        Minha Sacola
        <span class="material-symbols-outlined">arrow_forward</span>
      </a>
    </div>
  </div>
</header>
"""

def fix_links_and_header(file_path):
    if not os.path.exists(file_path): return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Replace TopAppBar block
    # Start at <!-- TopAppBar --> and end at the next <!-- comment --> or major tag like <main> or <section>
    content = re.sub(r'<!-- TopAppBar -->.*?(?=<section|首页|<main|<!-- Hero|<!-- Breadcrumbs)', header_html + "\n", content, flags=re.DOTALL)
    
    # 2. Fix other links like href="#"
    # Home path in breadcrumbs etc
    content = content.replace('href="#"', 'href="index.html"')
    
    # Breadcrumb links to collections
    content = re.sub(r'href="index\.html">Blusas</a>', 'href="listagem_de_produtos.html">Blusas</a>', content)
    content = re.sub(r'href="index\.html">Início</a>', 'href="index.html">Início</a>', content)
    
    # Final cleanup: specific page links
    if "listagem_de_produtos" in file_path:
        pass # All good
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {os.path.basename(file_path)}")

for f in files:
    fix_links_and_header(f)
