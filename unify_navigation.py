import re
import os

files = [
    "c:/Users/euand/Documents/MY JOB/2026/AdNove/Prospecções/Março/Maria Moura/index.html",
    "c:/Users/euand/Documents/MY JOB/2026/AdNove/Prospecções/Março/Maria Moura/listagem_de_produtos.html",
    "c:/Users/euand/Documents/MY JOB/2026/AdNove/Prospecções/Março/Maria Moura/pagina_do_produto.html",
    "c:/Users/euand/Documents/MY JOB/2026/AdNove/Prospecções/Março/Maria Moura/carrinho_de_compras.html"
]

header_fixed_html = """
<!-- TopAppBar -->
<header class="bg-[#faf9f6]/95 dark:bg-stone-900/95 backdrop-blur-md full-width top-0 sticky z-[60] transition-all duration-300 border-b border-stone-100/50">
  <div class="flex justify-between items-center px-4 md:px-8 py-4 w-full max-w-screen-2xl mx-auto">
    <div class="flex items-center gap-2 md:gap-8">
      <button class="md:hidden text-[#865140] p-3 -ml-3 flex items-center justify-center hover:opacity-70 transition-opacity" id="open-menu" aria-label="Abrir Menu">
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
    <div class="flex items-center space-x-2 md:space-x-6 text-[#865140] dark:text-[#c28471]">
      <button class="p-2 hover:opacity-80 transition-opacity duration-300 scale-95 active:duration-150">
        <span class="material-symbols-outlined">person</span>
      </button>
      <a href="carrinho_de_compras.html" class="p-2 hover:opacity-80 transition-opacity duration-300 scale-95 active:duration-150 relative">
        <span class="material-symbols-outlined">shopping_bag</span>
      </a>
    </div>
  </div>
</header>
"""

overlay_script_html = """
<!-- Mobile Menu Overlay -->
<div id="mobile-menu" class="hidden fixed inset-0 z-[200] bg-[#faf9f6] flex flex-col overflow-y-auto transform transition-transform duration-300 translate-x-full">
  <div class="flex justify-between items-center p-8">
    <span class="font-serif text-2xl font-bold tracking-tighter text-[#865140]">MARIA MOURA</span>
    <button id="close-menu" class="p-2 text-[#865140] flex items-center justify-center" aria-label="Fechar Menu">
      <span class="material-symbols-outlined text-4xl">close</span>
    </button>
  </div>
  <nav class="flex flex-col space-y-6 px-8 font-serif text-3xl tracking-wide text-stone-800 pt-8">
    <a href="index.html" class="py-2 border-b border-stone-100">Novidades</a>
    <a href="listagem_de_produtos.html" class="py-2 border-b border-stone-100">Coleções</a>
    <a href="listagem_de_produtos.html" class="py-2 border-b border-stone-100">Blusas</a>
    <a href="listagem_de_produtos.html" class="py-2 border-b border-stone-100">Calças</a>
    <a href="listagem_de_produtos.html" class="py-2 border-b border-stone-100">Sale</a>
  </nav>
  <div class="mt-auto p-8 bg-stone-50 flex flex-col gap-6 text-stone-500 font-serif text-xl border-t border-stone-100">
    <a href="index.html" class="flex items-center justify-between">Minha Conta <span class="material-symbols-outlined">person</span></a>
    <a href="carrinho_de_compras.html" class="flex items-center justify-between text-[#865140] font-bold">
      Minha Sacola
      <span class="material-symbols-outlined">shopping_bag</span>
    </a>
  </div>
</div>

<script>
  (function() {
    const openBtn = document.getElementById('open-menu');
    const closeBtn = document.getElementById('close-menu');
    const menu = document.getElementById('mobile-menu');

    if (openBtn && closeBtn && menu) {
      openBtn.addEventListener('click', () => {
        menu.classList.remove('hidden');
        setTimeout(() => {
          menu.style.transform = 'translateX(0)';
        }, 10);
        document.body.style.overflow = 'hidden';
      });

      const closeHandler = () => {
        menu.style.transform = 'translateX(100%)';
        setTimeout(() => {
          menu.classList.add('hidden');
          document.body.style.overflow = '';
        }, 300);
      };

      closeBtn.addEventListener('click', closeHandler);
      
      menu.querySelectorAll('nav a').forEach(link => {
        link.addEventListener('click', closeHandler);
      });
    }
  })();
</script>
"""

def fix_links_and_header(file_path):
    if not os.path.exists(file_path): return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove existing mobile menu (in case it's inside the header or elsewhere)
    content = re.sub(r'<!-- Mobile Menu Overlay -->.*?</div>\s*</header>', '</header>', content, flags=re.DOTALL)
    # Remove existing mobile menu if it's already outside (cleanup)
    content = re.sub(r'<!-- Mobile Menu Overlay -->.*?<script>.*?</script>', '', content, flags=re.DOTALL)

    # 1. Replace TopAppBar block
    content = re.sub(r'<!-- TopAppBar -->.*?(?=<section|首页|<main|<!-- Hero|<!-- Breadcrumbs)', header_fixed_html + "\n", content, flags=re.DOTALL)
    
    # 2. Inject Overlay and Script before </body>
    if "</body>" in content and "mobile-menu" not in content:
        content = content.replace("</body>", overlay_script_html + "\n</body>")
    
    # 3. Fix other links like href="#"
    content = content.replace('href="#"', 'href="index.html"')
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {os.path.basename(file_path)}")

for f in files:
    fix_links_and_header(f)
