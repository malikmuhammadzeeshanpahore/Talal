import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

new_faq = r'''      <div class="faq-container fade-up">
        <div class="faq-item">
          <div class="faq-question">
            Do you provide services all over Saudi Arabia?
            <i class="fa-solid fa-chevron-down"></i>
          </div>
          <div class="faq-answer">
            <p>We primarily operate in major districts of Jeddah. We are continually expanding our reach to serve more areas across the Kingdom.</p>
          </div>
        </div>
        
        <div class="faq-item">
          <div class="faq-question">
            Expert Advice: DIY vs. Professional Repair
            <i class="fa-solid fa-chevron-down"></i>
          </div>
          <div class="faq-answer">
            <p><strong>DIY (Do It Yourself):</strong> You can safely clean your AC's external air filters every 2 weeks or clear debris around your fridge. <br><strong>Professional Help:</strong> Never attempt to refill refrigerant gas, fix compressor electricals, or handle PCB boards yourself. This requires a certified technician to avoid permanent appliance damage or electrical hazards.</p>
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">
            Are your technicians certified?
            <i class="fa-solid fa-chevron-down"></i>
          </div>
          <div class="faq-answer">
            <p>Yes, all our technicians undergo rigorous training and are certified to handle complex repairs for all leading brands like Haier, Samsung, LG, and more.</p>
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">
            Do you offer a warranty on repairs?
            <i class="fa-solid fa-chevron-down"></i>
          </div>
          <div class="faq-answer">
            <p>Absolutely. We provide a 6-month service warranty on our labor and any genuine spare parts replaced during the repair process, ensuring your peace of mind.</p>
          </div>
        </div>
      </div>
'''

old_faq = r'<div class="faq-container fade-up">.*?</div>\s*</div>\s*</section>'
idx_content = re.sub(old_faq, new_faq + '    </div>\n  </section>', idx_content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
