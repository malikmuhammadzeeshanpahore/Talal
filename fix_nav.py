import os
import glob

nav_html = """      <nav class="nav-menu">
        <div class="nav-item"><a href="index.html" class="nav-link">Home</a></div>
        <div class="nav-item"><a href="about.html" class="nav-link">About Us</a></div>
        <div class="nav-item dropdown">
          <a href="services.html" class="nav-link">Services <i class="fa-solid fa-chevron-down" style="font-size: 0.8rem; margin-left: 5px;"></i></a>
          <div class="dropdown-menu">
            <a href="ac-repair.html" class="dropdown-item">AC Repair</a>
            <a href="fridge-repair.html" class="dropdown-item">Fridge Repair</a>
            <a href="washing-machine-repair.html" class="dropdown-item">Washing Machine</a>
          </div>
        </div>
        <div class="nav-item"><a href="contact.html" class="nav-link">Contact</a></div>
      </nav>"""

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # We need to find the <nav class="nav-menu"> block
    start_idx = content.find('<nav class="nav-menu">')
    end_idx = content.find('</nav>', start_idx)
    
    if start_idx != -1 and end_idx != -1:
        # replace the block
        new_content = content[:start_idx] + nav_html + content[end_idx+6:]
        
        # fix active class based on filename
        filename = os.path.basename(filepath)
        if filename == 'index.html':
            new_content = new_content.replace('"nav-link">Home', '"nav-link active">Home')
        elif filename == 'about.html':
            new_content = new_content.replace('"nav-link">About Us', '"nav-link active">About Us')
        elif filename == 'services.html':
            new_content = new_content.replace('"nav-link">Services', '"nav-link active">Services')
        elif filename == 'ac-repair.html':
            new_content = new_content.replace('"dropdown-item">AC Repair', '"dropdown-item active" style="color: var(--primary-orange);">AC Repair')
            new_content = new_content.replace('"nav-link">Services', '"nav-link active">Services')
        elif filename == 'fridge-repair.html':
            new_content = new_content.replace('"dropdown-item">Fridge Repair', '"dropdown-item active" style="color: var(--primary-orange);">Fridge Repair')
            new_content = new_content.replace('"nav-link">Services', '"nav-link active">Services')
        elif filename == 'washing-machine-repair.html':
            new_content = new_content.replace('"dropdown-item">Washing Machine', '"dropdown-item active" style="color: var(--primary-orange);">Washing Machine')
            new_content = new_content.replace('"nav-link">Services', '"nav-link active">Services')
        elif filename == 'contact.html':
            new_content = new_content.replace('"nav-link">Contact', '"nav-link active">Contact')
            
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

