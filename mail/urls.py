from django.urls import path

from .views import *

urlpatterns = [
    path('mailchimp/add-email/', MailchimpAddMail.as_view()),
    path('gmail/send-email/', GoogleSendEmail.as_view()),
]