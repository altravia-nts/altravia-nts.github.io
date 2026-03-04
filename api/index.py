from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
# Enable CORS to accept requests from the frontend domain
CORS(app)

@app.route('/api/submit', methods=['POST'])
def submit_form():
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
            msg = MIMEMultipart()
            msg['From'] = smtp_user
            msg['To'] = destination_email
            msg['Subject'] = f"New Contact Request from {name}"
            msg['Reply-To'] = email

            msg.attach(MIMEText(submission_data, 'plain'))

            server = smtplib.SMTP(smtp_server, int(smtp_port))
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
            # If email sending is critical, you might return an error here.
            # return f"Error sending email: {e}", 500
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
