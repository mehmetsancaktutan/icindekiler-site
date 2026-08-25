import os

langs = ["en", "de", "fr", "es"]
for lang in langs:
    filepath = f"{lang}/index.html"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    flags = """  <div style="text-align:center; margin-top:20px; font-size:1.2rem; display:flex; justify-content:center; gap:16px;">
    <a href="../index.html" style="text-decoration:none;">🇹🇷</a>
    <a href="../en/index.html" style="text-decoration:none;">🇬🇧</a>
    <a href="../de/index.html" style="text-decoration:none;">🇩🇪</a>
    <a href="../fr/index.html" style="text-decoration:none;">🇫🇷</a>
    <a href="../es/index.html" style="text-decoration:none;">🇪🇸</a>
  </div>
  
  <footer>"""
    
    content = content.replace("  <footer>", flags)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
