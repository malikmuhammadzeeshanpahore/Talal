import glob

schema = '''
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Markaz Talal liltabreed",
    "image": "https://markaztalal.com/images/hero-banner.webp",
    "description": "Professional AC, Refrigerator, and Washing Machine repair services in Jeddah, Saudi Arabia.",
    "url": "https://markaztalal.com",
    "telephone": "+966531624801",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "6540, 3519 Ankara, As Samir District",
      "addressLocality": "Jeddah",
      "postalCode": "23462",
      "addressCountry": "SA"
    },
    "openingHoursSpecification": {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
      "opens": "00:00",
      "closes": "23:59"
    },
    "priceRange": "SAR 99 - 500",
    "currenciesAccepted": "SAR"
  }
  </script>
</head>'''

for html_file in glob.glob('*.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "application/ld+json" not in content:
        content = content.replace('</head>', schema)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
