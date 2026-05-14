import glob
import os

footer_old = "              <p>Riyadh, Jeddah, Dammam<br>Saudi Arabia</p>"
footer_new = "              <p>6540, 3519 Ankara, As Samir District,<br>Jeddah 23462</p>"

contact_address_old = "              <p>Riyadh, Jeddah, Dammam<br>Saudi Arabia</p>"
contact_address_new = "              <p>6540, 3519 Ankara, As Samir District,<br>Jeddah 23462</p>"

replacements = [
    ("Riyadh, Jeddah, and Dammam", "Jeddah"),
    ("across Riyadh, Jeddah, and Dammam", "across Jeddah"),
    ("Riyadh, Jeddah, Dammam, and Al Khobar", "Jeddah"),
    ("Saudi Arabia (Riyadh, Jeddah, Dammam)", "Jeddah, Saudi Arabia"),
    ('class="client-loc">Riyadh<', 'class="client-loc">Jeddah<'),
    ('class="client-loc">Dammam<', 'class="client-loc">Jeddah<'),
    ("across Jeddah, Dammam, and beyond", "across Jeddah"),
    ("in Riyadh, Jeddah, and Dammam", "in Jeddah"),
    ("Jeddah & Riyadh", "Jeddah"),
    ("Jeddah and Riyadh", "Jeddah"),
    ("AC repair in Riyadh,", "AC repair in Jeddah,"),
    ("Riyadh", "Jeddah"),
    ("Dammam", "Jeddah"),
    ("Al Khobar", "Jeddah"),
    ("Eastern Province", "Jeddah"),
    ("Dhahran", "Jeddah"),
]

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace footer
    content = content.replace(footer_old, footer_new)
    
    # Apply global replacements
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Updated {filepath}")
