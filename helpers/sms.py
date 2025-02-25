from django.core.mail import send_mail


def send_email(code, email):
    recipient_email = str(email)
    subject = 'Test email'
    message = str(code)
    sender_email = ''
    try:
        send_mail(subject, message, sender_email, [recipient_email])
        return {'success': True, 'message': 'Email sent successfully'}
    except Exception as e:
        return {'success': False, 'message':str(e)}
