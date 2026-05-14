import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

new_form = r'''
        <div class="multi-step-form" id="bookingForm">
          <div class="step active" id="step1">
            <h3 style="margin-bottom: 20px; color: var(--primary-navy);">Step 1: What needs repair?</h3>
            <div class="appliance-selector">
              <label class="app-card"><input type="radio" name="appliance" value="AC"><span><i class="fa-solid fa-fan"></i> AC</span></label>
              <label class="app-card"><input type="radio" name="appliance" value="Fridge"><span><i class="fa-solid fa-temperature-empty"></i> Fridge</span></label>
              <label class="app-card"><input type="radio" name="appliance" value="Washing Machine"><span><i class="fa-solid fa-water"></i> Washer</span></label>
            </div>
            <button class="btn btn-primary next-btn" onclick="nextStep(2)" style="width:100%; margin-top:20px;">Next <i class="fa-solid fa-arrow-right"></i></button>
          </div>

          <div class="step" id="step2" style="display:none;">
            <h3 style="margin-bottom: 20px; color: var(--primary-navy);">Step 2: What is the issue?</h3>
            <textarea id="issueDesc" class="form-control" rows="4" placeholder="Briefly describe the problem..." required></textarea>
            <div style="display: flex; gap: 10px; margin-top: 20px;">
              <button class="btn btn-outline prev-btn" onclick="nextStep(1)" style="flex:1;">Back</button>
              <button class="btn btn-primary next-btn" onclick="nextStep(3)" style="flex:1;">Next <i class="fa-solid fa-arrow-right"></i></button>
            </div>
          </div>

          <div class="step" id="step3" style="display:none;">
            <h3 style="margin-bottom: 20px; color: var(--primary-navy);">Step 3: Your Details</h3>
            <div class="form-group"><input type="text" id="custName" class="form-control" placeholder="Full Name" required></div>
            <div class="form-group"><input type="tel" id="custPhone" class="form-control" placeholder="Phone (e.g., 05xxxx)" required></div>
            <div style="display: flex; gap: 10px; margin-top: 20px;">
              <button class="btn btn-outline prev-btn" onclick="nextStep(2)" style="flex:1;">Back</button>
              <button class="btn btn-primary submit-btn" onclick="submitToWhatsApp()" style="flex:2;"><i class="fa-brands fa-whatsapp"></i> Send to WhatsApp</button>
            </div>
          </div>
        </div>
'''

old_form_regex = r'<form action="#" method="POST">.*?</form>'
idx_content = re.sub(old_form_regex, new_form, idx_content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

