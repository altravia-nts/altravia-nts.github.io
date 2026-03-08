from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
# Enable CORS to accept requests from the frontend domain
CORS(app)

@app.route('/api', methods=['GET'], strict_slashes=False)
@app.route('/api/', methods=['GET'], strict_slashes=False)
@app.route('/api/index', methods=['GET'], strict_slashes=False)
def api_status():
    return jsonify({"status": "success", "message": "API is running. Send a POST request to /api/submit to use the contact form."})

@app.route('/api/submit', methods=['GET', 'POST'], strict_slashes=False)
def submit_form():
    if request.method == 'GET':
        return jsonify({"error": "Method Not Allowed. Please send a POST request to submit the form."}), 405


    name = request.form.get('name')
    # The form input uses name="_replyto"
    email = request.form.get('_replyto')
    residence = request.form.get('residence')
    phone = request.form.get('phone')
    services = request.form.get('services')
    message = request.form.get('message')

    # Basic validation
    if not all([name, email, services, message]):
        return "Missing mandatory fields.", 400

    # Format the message for the email body
    submission_data = f"""New Contact Form Submission:

Name: {name}
Email: {email}
Residence: {residence or 'N/A'}
Phone: {phone or 'N/A'}
Service Requested: {services}

Message:
{message}
"""
    
    # Also log to console for debugging
    print("-" * 50)
    print(submission_data)
    print("-" * 50)

    # --- Email Sending Logic ---
    # Fetch environment variables
    smtp_server = os.environ.get('SMTP_SERVER')
    smtp_port = os.environ.get('SMTP_PORT', 587)  # Default to 587 (TLS)
    smtp_user = os.environ.get('SMTP_USER')
    smtp_pass = os.environ.get('SMTP_PASS')
    destination_email = os.environ.get('DESTINATION_EMAIL')

    if all([smtp_server, smtp_user, smtp_pass, destination_email]):
        try:
            # HTML format for Admin
            admin_html = f"""
            <html>
              <body style="font-family: Arial, sans-serif; background-color: #f4f7f6; padding: 20px;">
                <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                  <h2 style="color: #333333; border-bottom: 2px solid #007bff; padding-bottom: 10px;">New Contact Request</h2>
                  <p style="color: #555555; font-size: 16px;"><strong>Name:</strong> {name}</p>
                  <p style="color: #555555; font-size: 16px;"><strong>Email:</strong> {email}</p>
                  <p style="color: #555555; font-size: 16px;"><strong>Residence:</strong> {residence or 'N/A'}</p>
                  <p style="color: #555555; font-size: 16px;"><strong>Phone:</strong> {phone or 'N/A'}</p>
                  <p style="color: #555555; font-size: 16px;"><strong>Service Requested:</strong> {services}</p>
                  <br>
                  <h3 style="color: #333333;">Message:</h3>
                  <div style="background-color: #f8f9fa; padding: 15px; border-left: 4px solid #007bff; color: #444444; white-space: pre-wrap;">
                    {message}
                  </div>
                </div>
              </body>
            </html>
            """
            
            # HTML format for User Acknowledgment
            ack_html = f"""
            <html>
              <body style="font-family: Arial, sans-serif; background-color: #f4f7f6; padding: 20px;">
                <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                  <div style="text-align: center; margin-bottom: 20px;">
                    <h2 style="color: #007bff; margin: 0;">Thank You for Contacting Altravia</h2>
                  </div>
                  <p style="color: #555555; font-size: 16px; line-height: 1.6;">Hi <strong>{name}</strong>,</p>
                  <p style="color: #555555; font-size: 16px; line-height: 1.6;">
                    Thank you for reaching out to us regarding <strong>{services}</strong>. We have successfully received your message and our team will get back to you as soon as possible.
                  </p>
                  <br>
                  <h3 style="color: #333333; text-align: left; font-size: 18px;">A copy of your message:</h3>
                  <div style="background-color: #f8f9fa; padding: 15px; border-left: 4px solid #ced4da; color: #444444; white-space: pre-wrap;">
                    {message}
                  </div>
                  <br>
                  <p style="color: #888888; font-size: 14px; text-align: center; margin-top: 30px; border-top: 1px solid #eeeeee; padding-top: 15px;">
                    Best regards,<br>
                    <strong>The Altravia Team</strong>
                  </p>
                </div>
              </body>
            </html>
            """
            # Email 1: To the admin (You)
            msg = MIMEMultipart()
            msg['From'] = smtp_user
            msg['To'] = destination_email
            msg['Subject'] = f"New Contact Request from {name}"
            msg['Reply-To'] = email

            msg.attach(MIMEText(admin_html, 'html'))

            # Email 2: Acknowledgment to the user
            ack_msg = MIMEMultipart()
            ack_msg['From'] = smtp_user
            ack_msg['To'] = email
            ack_msg['Subject'] = "Thank you for contacting Altravia!"
            
            ack_msg.attach(MIMEText(ack_html, 'html'))

            server = smtplib.SMTP(smtp_server, int(smtp_port))
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
            server.send_message(ack_msg)
            server.quit()
            print("Emails sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
            error_html = """
            <!DOCTYPE html>
            <html>
            <head><title>Error</title></head>
            <body style="font-family: sans-serif; text-align: center; margin-top: 50px; background-color: #f8f9fa;">
                <div style="max-width: 500px; margin: auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    <h2 style="color: #dc3545;">Oops! Something went wrong.</h2>
                    <p>We couldn't submit your message at this time. Please check your email address and try again later.</p>
                    <br>
                    <a href="/" style="display: inline-block; padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px;">&larr; Try Again</a>
                </div>
            </body>
            </html>
            """
            return render_template_string(error_html), 500
    else:
        print("SMTP environment variables are not fully configured. Skipping email send.")

    # Return a success page to the user
    html = """
    <!DOCTYPE html>
    <html>
    <head><title>Message Sent</title></head>
    <body style="font-family: sans-serif; text-align: center; margin-top: 50px; background-color: #f8f9fa;">
        <div style="max-width: 500px; margin: auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h2 style="color: #28a745;">Thank You!</h2>
            <p>Your message has been successfully sent. We will get back to you shortly.</p>
            <br>
            <a href="/" style="display: inline-block; padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px;">&larr; Return to Website</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

# For local testing only. Vercel automatically handles execution in production.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
