import os
import glob
from PIL import Image

image_dir = 'images'
os.makedirs(image_dir, exist_ok=True)

# 1. Convert Images
image_files = glob.glob(f"{image_dir}/*.jpg") + glob.glob(f"{image_dir}/*.jpeg") + glob.glob(f"{image_dir}/*.png")

for file in image_files:
    if file.endswith('.webp'):
        continue
    img = Image.open(file)
    webp_path = os.path.splitext(file)[0] + '.webp'
    img.save(webp_path, 'webp', optimize=True, quality=85)
    os.remove(file)
    print(f"Converted {file} -> {webp_path}")

# 2. Update HTML files
import re
for html_file in glob.glob('*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace .jpg, .jpeg, .png with .webp
    content = re.sub(r'(src="images/[^"]+)\.(jpg|jpeg|png)(")', r'\1.webp\3', content, flags=re.IGNORECASE)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated image references in {html_file}")
