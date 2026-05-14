import os
import glob
import re

# 1. Add lazy loading to images (except those in hero section if possible, but for simplicity we can add to all imgs not having it, then remove from hero)
for html_file in glob.glob('*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add loading="lazy" if not present
    content = re.sub(r'<img(?!.*loading=)[^>]*>', lambda m: m.group(0).replace('<img', '<img loading="lazy"'), content)
    
    # Remove lazy from hero image (if any) to prevent LCP delay
    content = re.sub(r'(<div class="about-image.*?)<img loading="lazy"', r'\1<img', content, flags=re.DOTALL)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Minify CSS (Basic)
with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()
    
# Remove comments
css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
# Remove whitespace
css_content = re.sub(r'\s+', ' ', css_content)
css_content = css_content.replace(' {', '{').replace(': ', ':').replace(';}', '}').replace('; ', ';')

with open('css/style.min.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# 3. Minify JS (Basic)
with open('js/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()
# Remove single line comments
js_content = re.sub(r'//.*', '', js_content)
# Remove multi line comments
js_content = re.sub(r'/\*.*?\*/', '', js_content, flags=re.DOTALL)
# Remove extra whitespace
js_content = re.sub(r'\s+', ' ', js_content)

with open('js/main.min.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Update HTML references
for html_file in glob.glob('*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('css/style.css', 'css/style.min.css')
    content = content.replace('js/main.js', 'js/main.min.js')
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
