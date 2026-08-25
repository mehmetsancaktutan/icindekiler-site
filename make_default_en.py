import os
import shutil

# Step 1: Create tr/ directory and move root html files there
os.makedirs("tr", exist_ok=True)
html_files = ["index.html", "privacy.html", "support.html", "terms.html"]

for f in html_files:
    if os.path.exists(f):
        shutil.move(f, f"tr/{f}")

# Step 2: Move en/ html files to root
for f in html_files:
    if os.path.exists(f"en/{f}"):
        shutil.move(f"en/{f}", f)

# Step 3: Delete the en/ directory since it's now root
if os.path.exists("en"):
    os.rmdir("en")

# Step 4: Fix all the language picker links in all files
# Root files (English)
root_flags = """  <div style="text-align:center; margin-top:20px; font-size:1.2rem; display:flex; justify-content:center; gap:16px;">
    <a href="tr/index.html" style="text-decoration:none;">🇹🇷</a>
    <a href="index.html" style="text-decoration:none;">🇬🇧</a>
    <a href="de/index.html" style="text-decoration:none;">🇩🇪</a>
    <a href="fr/index.html" style="text-decoration:none;">🇫🇷</a>
    <a href="es/index.html" style="text-decoration:none;">🇪🇸</a>
  </div>"""

# Subfolder files (tr, de, fr, es)
sub_flags = """  <div style="text-align:center; margin-top:20px; font-size:1.2rem; display:flex; justify-content:center; gap:16px;">
    <a href="../tr/index.html" style="text-decoration:none;">🇹🇷</a>
    <a href="../index.html" style="text-decoration:none;">🇬🇧</a>
    <a href="../de/index.html" style="text-decoration:none;">🇩🇪</a>
    <a href="../fr/index.html" style="text-decoration:none;">🇫🇷</a>
    <a href="../es/index.html" style="text-decoration:none;">🇪🇸</a>
  </div>"""

import re

def update_flags(filepath, new_flags):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Use regex to replace the entire div block containing flags
    pattern = r'<div style="text-align:center; margin-top:20px; font-size:1.2rem; display:flex; justify-content:center; gap:16px;">.*?</div>'
    new_content = re.sub(pattern, new_flags, content, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

# Update root files
for f in html_files:
    if os.path.exists(f):
        update_flags(f, root_flags)

# Update subfolder files
for lang in ["tr", "de", "fr", "es"]:
    for f in html_files:
        filepath = f"{lang}/{f}"
        if os.path.exists(filepath):
            update_flags(filepath, sub_flags)

print("Done making English default!")
