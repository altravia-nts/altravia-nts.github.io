<h2>Let’s Get in Touch</h2>

<div class="row">
  <!-- Left Column: Profile Image -->
  <div class="col-lg-3 text-center">
    <img class="img-fluid py-3" src="/img/Neema.jpg" alt="Profile Picture">
  </div>

  <!-- Right Column: Contact Info / Form -->
  <div class="col-lg-9 text-start">
    Whether you have a question about mentorship, want guidance on your master’s journey, or just want to connect, you can reach me using the form below.<br><br>

    <form action="https://formspree.io/f/mvgeldby" method="POST">
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
                   placeholder="+49 123 456789">
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
      <button class="btn btn-dark btn-xl" type="submit">Send Message</button>
    </form>
  </div>
</div>
