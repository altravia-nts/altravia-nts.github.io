<h2>Let’s Get in Touch</h2>

<div class="row">
  <!-- Left Column: Profile Image -->
  <div class="col-lg-3 text-center">
    <img class="img-fluid py-3" src="/img/Neema.jpg" alt="Profile Picture">
  </div>

  <!-- Right Column: Contact Info / Form -->
  <div class="col-lg-9 text-start">
    Have a question about mentorship, need guidance on your master’s journey, or simply wish to connect? I’d be glad to hear from you — just use the form below.<br><br>

    {% if jekyll.environment == 'production' %}
    <form id="contactForm" action="/api/submit" method="POST">
    {% else %}
    <form id="contactForm" action="http://localhost:5000/api/submit" method="POST">
    {% endif %}
      <div class="row">
        <!-- Name -->
        <div class="col-md-6">
          <div class="mb-3">
            <label for="name" class="form-label">Your Name</label>
            <input type="text" name="name" class="form-control" id="name" 
                   placeholder="Enter your name" required>
          </div>
        </div>

        <!-- Email -->
        <div class="col-md-6">
          <div class="mb-3">
            <label for="email" class="form-label">Email address</label>
            <input type="email" name="_replyto" class="form-control" id="email" 
                   placeholder="name@example.com" required>
          </div>
        </div>
      </div>

      <div class="row">
        <!-- Place of Residence (optional) -->
        <div class="col-md-6">
          <div class="mb-3">
            <label for="residence" class="form-label">Place of Residence</label>
            <input type="text" name="residence" class="form-control" id="residence" 
                   placeholder="City, Country">
          </div>
        </div>

        <!-- Phone (optional) -->
        <div class="col-md-6">
          <div class="mb-3">
            <label for="phone" class="form-label">Phone Number</label>
            <input type="tel" name="phone" class="form-control" id="phone" 
                   placeholder="+49 123 456789"
                   pattern="^\+?[0-9\s\-\(\)]+$"
                   title="Please enter a valid phone number (numbers, spaces, and + - ( ) only)"
                   oninput="this.value = this.value.replace(/[^0-9\+\-\s\(\)]/g, '');">
          </div>
        </div>
      </div>

      <!-- Services you are looking for (mandatory) -->
      <div class="mb-3">
        <label for="services" class="form-label">Services you are looking for</label>
        <select name="services" class="form-select" id="services" required>
          <option value="" disabled selected>Select a service</option>
          <option value="Study in Europe Planning">Study in Europe Planning</option>
          <option value="Scholarship Application Support">Scholarship Application Support</option>
          <option value="CV, Cover Letter">CV, Cover Letter</option>
          <option value="Internship & Job Application Support">Internship & Job Application Support</option>
          <option value="Visa Application Assistance">Visa Application Assistance</option>
        </select>
      </div>

      <!-- Message -->
      <div class="mb-3">
        <label for="message" class="form-label">Message</label>
        <textarea name="message" class="form-control" id="message" 
                  placeholder="Leave a message here" style="height: 10rem" required></textarea>
      </div>

      <!-- Submit -->
      <button class="btn-custom" type="submit">Send Message</button>
    </form>
  </div>
</div>

<!-- Loading Overlay UI -->
<div id="loadingOverlay">
  <div class="spinner"></div>
  <div class="loading-text">Sending message...</div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('contactForm');
  const overlay = document.getElementById('loadingOverlay');

  if (form) {
    form.addEventListener('submit', function(e) {
      // Prevent standard browser form submission
      e.preventDefault();
      
      // Show loading overlay
      overlay.classList.add('active');

      // Create form data 
      const formData = new URLSearchParams(new FormData(form));
      const url = form.getAttribute('action');

      // Send the request via fetch API
      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData.toString()
      })
      .then(response => {
        if (!response.ok) {
           throw new Error('Network response was not ok');
        }
        return response.text(); 
      })
      .then(html => {
        // Success: the server returns an HTML success page. Render it to the current window.
        document.open();
        document.write(html);
        document.close();
      })
      .catch(error => {
        // Hide overlay on error and show alert
        overlay.classList.remove('active');
        alert("Sorry, an error occurred while sending your message. Please try again.");
        console.error('Error submitting form:', error);
      });
    });
  }
});
</script>
