from django.core.mail import send_mail

from rest_framework import status, permissions
from rest_framework.views import Response, APIView

from .utils import (
    mailchimp
)


class MailchimpAddMail(APIView):
    """
    Send the Mail to Contact list
    """
    def post(self, request, format=None):
        email = request.data.get('email')
        adding = mailchimp.Mailchimp()
        adding.add_email(email=email)
        return Response({
            "message": "Email Successfully added to the list"
        })


class GoogleSendEmail(APIView):
    """
    Send the mail through google gsuit
    """
    def post(self, request, format=None):
        from_email = request.data.get('from_email')
        to_email = request.data.get('to_email')
        subject = request.data.get('subject')
        message = request.data.get('message')

        try:
            send_mail(
                from_email=from_email,
                recipient_list=[to_email,],
                subject=subject,
                message=message,
                fail_silently=False
            )
            msg = "Email successfully sent from {from_email} to {to_email}".format(str(from_email), str(to_email))
            msg_status = status.HTTP_201_CREATED
        except Exception as e:
            msg = e
            msg_status = status.HTTP_400_BAD_REQUEST
        return Response({
            "message": str(msg),
            "status": msg_status
        })