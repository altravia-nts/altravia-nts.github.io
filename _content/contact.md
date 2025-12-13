<section id="contact" class="contact bg-light">
  <div class="container">
    <h2 class="text-center">Get in Touch</h2>
    <hr class="small div-center mb-5">
    <p class="lead text-center mb-5">Have a question or want to work together? Send me a message!</p>

    <div class="row justify-content-center">
      <!-- Left Column: Image -->
      <div class="col-lg-3 text-center">
        <img class="img-fluid py-3" src="/img/Neema.jpg" alt="Profile Picture">
      </div>

      <!-- Right Column: Contact Form -->
      <div class="col-lg-8 text-start">
        <form action="https://formspree.io/f/mvgeldby" method="POST">
          <div class="row">
            <div class="col-md-6">
              <div class="form-floating mb-3">
                <input type="text" name="name" class="form-control" id="name" placeholder="Your Name" required>
                <label for="name">Your Name</label>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-floating mb-3">
                <input type="email" name="_replyto" class="form-control" id="email" placeholder="name@example.com" required>
                <label for="email">Email address</label>
              </div>
            </div>
          </div>
          <div class="form-floating mb-3">
            <textarea name="message" class="form-control" placeholder="Leave a message here" id="message" style="height: 10rem" required></textarea>
            <label for="message">Message</label>
          </div>
          <button class="btn btn-dark btn-xl" type="submit">Send Message</button>
        </form>
      </div>
    </div>
  </div>
</section>
