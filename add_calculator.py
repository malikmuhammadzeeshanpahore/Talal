import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

calc_html = r'''
      <div class="pricing-calc fade-up" style="margin-top: 50px;">
        <h3 class="section-title" style="font-size: 1.8rem; text-align: center;">Get a Free Quote</h3>
        <p style="text-align: center; margin-bottom: 30px;">Select your appliance and the issue to get an instant estimated repair cost.</p>
        <div class="form-group" style="display: flex; gap: 20px; flex-wrap: wrap;">
          <select id="calcAppliance" class="form-control" style="flex: 1; min-width: 200px;" onchange="calculateQuote()">
            <option value="" disabled selected>Select Appliance</option>
            <option value="ac">Air Conditioner</option>
            <option value="fridge">Refrigerator</option>
            <option value="washing">Washing Machine</option>
          </select>
          <select id="calcIssue" class="form-control" style="flex: 1; min-width: 200px;" onchange="calculateQuote()">
            <option value="" disabled selected>Select Issue</option>
            <option value="not_cooling">Not Cooling / Not Working</option>
            <option value="gas">Gas Leak / Refill Needed</option>
            <option value="noise">Strange Noise / Leaking Water</option>
            <option value="service">General Maintenance & Cleaning</option>
          </select>
        </div>
        <div class="pricing-result">
          <h4>Estimated Cost:</h4>
          <div class="est-price" id="estPrice">Select Options</div>
        </div>
      </div>
    </div>
  </section>
'''

idx_content = idx_content.replace('      </div>\n    </div>\n  </section>\n\n  <!-- Section 8: Testimonials -->', calc_html + '\n  <!-- Section 8: Testimonials -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
