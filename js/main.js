document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
      navMenu.classList.toggle('active');
      const icon = mobileToggle.querySelector('i');
      if (navMenu.classList.contains('active')) {
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-times');
      } else {
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
      }
    });
  }

  // Header Scroll Effect
  const header = document.querySelector('.header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    if (question) {
      question.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        
        // Close all other items
        faqItems.forEach(otherItem => {
          otherItem.classList.remove('active');
        });

        // Toggle current item
        if (!isActive) {
          item.classList.add('active');
        }
      });
    }
  });

  // Intersection Observer for Scroll Animations
  const faders = document.querySelectorAll('.fade-up');
  const appearOptions = {
    threshold: 0.15,
    rootMargin: "0px 0px -50px 0px"
  };

  const appearOnScroll = new IntersectionObserver(function(entries, observer) {
    entries.forEach(entry => {
      if (!entry.isIntersecting) {
        return;
      } else {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, appearOptions);

  faders.forEach(fader => {
    appearOnScroll.observe(fader);
  });

  // Active Link State based on URL
  const currentLocation = location.href;
  const menuItem = document.querySelectorAll('.nav-link');
  const menuLength = menuItem.length;
  for (let i = 0; i < menuLength; i++) {
    if (menuItem[i].href === currentLocation) {
      menuItem[i].classList.add("active");
    }
  }
});

// Multi-Step Form Logic
function nextStep(step) {
  document.querySelectorAll('.multi-step-form .step').forEach(el => el.style.display = 'none');
  document.getElementById('step' + step).style.display = 'block';
}

function submitToWhatsApp() {
  const appliance = document.querySelector('input[name="appliance"]:checked')?.value || 'Not specified';
  const issue = document.getElementById('issueDesc').value || 'Not specified';
  const name = document.getElementById('custName').value;
  const phone = document.getElementById('custPhone').value;
  
  if(!name || !phone) {
    alert("Please enter your name and phone number.");
    return;
  }
  
  const text = `Hello Markaz Talal,%0A%0AI need a repair service:%0A*Appliance:* ${appliance}%0A*Issue:* ${issue}%0A*Name:* ${name}%0A*Phone:* ${phone}%0A%0APlease contact me soon.`;
  window.open(`https://wa.me/966531624801?text=${text}`, '_blank');
}

// Pricing Calculator Logic
function calculateQuote() {
  const app = document.getElementById('calcAppliance').value;
  const issue = document.getElementById('calcIssue').value;
  let price = "Select Options";
  
  if (app && issue) {
    if (app === 'ac') {
      price = issue === 'gas' ? '250 - 350 <span class="currency">SAR</span>' : (issue === 'service' ? '150 <span class="currency">SAR</span>' : '150 - 500 <span class="currency">SAR</span>');
    } else if (app === 'fridge') {
      price = issue === 'gas' ? '300 - 450 <span class="currency">SAR</span>' : '200 - 600 <span class="currency">SAR</span>';
    } else {
      price = '150 - 400 <span class="currency">SAR</span>';
    }
  }
  document.getElementById('estPrice').innerHTML = price;
}
