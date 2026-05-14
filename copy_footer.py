import re
import glob

# Read index.html to extract the exact footer
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the footer tag
footer_match = re.search(r'(<footer class="footer">.*?</footer>)', index_content, re.DOTALL)

if footer_match:
    footer_code = footer_match.group(1)
    
    # Apply to all other html files
    for file in glob.glob('*.html'):
        if file == 'index.html':
            continue
            
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace the existing footer
        new_content = re.sub(r'<footer class="footer">.*?</footer>', footer_code, content, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Updated footer in {file}")
else:
    print("Could not find footer in index.html")
