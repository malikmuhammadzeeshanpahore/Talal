import re
import glob

# 1. Update Hero Section text
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

idx_content = re.sub(
    r'<h1 class="hero-title">.*?</h1>',
    r'<h1 class="hero-title">Professional Repair Services for <span>AC, Fridge & Washing Machines</span></h1>',
    idx_content, flags=re.DOTALL
)

idx_content = re.sub(
    r'<p class="hero-text">.*?</p>',
    r'<p class="hero-text">Fast, reliable, and energy-efficient repair services across Jeddah. 24/7 Support & 1-Year Warranty.</p>',
    idx_content, flags=re.DOTALL
)

# 2. Update Header buttons
header_buttons_old = r'<div class="nav-actions">.*?</div>\s*</div>\s*</header>'
header_buttons_new = r'''<div class="nav-actions">
        <a href="tel:0531624801" class="btn btn-outline click-to-call" aria-label="Call Now"><i class="fa-solid fa-phone-volume pulse-icon"></i> 0531624801</a>
        <a href="contact.html" class="btn btn-primary" aria-label="Book Service">Book Service</a>
      </div>
    </div>
  </header>'''
idx_content = re.sub(header_buttons_old, header_buttons_new, idx_content, flags=re.DOTALL)

# Add Language Toggle placeholder before nav-actions
nav_menu_old = r'(<nav class="nav-menu">.*?</nav>)'
nav_menu_new = r'''\1
      <div class="lang-toggle" aria-label="Switch Language">
        <select style="background: transparent; border: 1px solid var(--glass-border); color: var(--primary-white); padding: 5px; border-radius: 5px;">
          <option value="en">EN</option>
          <option value="ar">العربية</option>
        </select>
      </div>'''
idx_content = re.sub(nav_menu_old, nav_menu_new, idx_content, flags=re.DOTALL)

# Add Mobile Bottom Bar before closing body
bottom_bar = r'''
  <!-- Mobile Bottom Navigation (Thumb-Zone) -->
  <div class="mobile-bottom-bar">
    <a href="tel:0531624801" class="bottom-bar-btn call-btn" aria-label="Call Us">
      <i class="fa-solid fa-phone"></i>
      <span>Call</span>
    </a>
    <a href="contact.html" class="bottom-bar-btn book-btn" aria-label="Book Online">
      <i class="fa-solid fa-calendar-check"></i>
      <span>Book</span>
    </a>
    <a href="https://wa.me/966531624801" class="bottom-bar-btn wa-btn" aria-label="WhatsApp Us" target="_blank">
      <i class="fa-brands fa-whatsapp"></i>
      <span>WhatsApp</span>
    </a>
  </div>
'''
if "mobile-bottom-bar" not in idx_content:
    idx_content = idx_content.replace('</body>', bottom_bar + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

# Update the header in other files too
for html_file in glob.glob('*.html'):
    if html_file == 'index.html': continue
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(header_buttons_old, header_buttons_new, content, flags=re.DOTALL)
    content = re.sub(nav_menu_old, nav_menu_new, content, flags=re.DOTALL)
    if "mobile-bottom-bar" not in content:
        content = content.replace('</body>', bottom_bar + '\n</body>')
        
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

