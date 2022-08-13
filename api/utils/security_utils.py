"""This component implements logic to send emails.
"""

from sendgrid import SendGridAPIClient
from django.conf import settings
from sendgrid.helpers.mail import Mail
from logging import Logger
from api.models import User

from django.contrib.auth.tokens import PasswordResetTokenGenerator



class EmailHandler:
    class Result:
        def __init__(self, is_success, errors, result=None):
            self.is_success = is_success
            self.errors = errors
            self.result = result

    def send_account_authentication_email(
        self, user: User, to_email: str, verification_link: str
    ) -> None:
        """Send Email to user for email verification."""

        logger = Logger("")
        message = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=to_email,
            subject="VERIFY YOUR EMAIL",
            plain_text_content=f"Please verify clicking here, {verification_link}",
        )
        sendgrid_client = SendGridAPIClient(settings.SENDGRID_API_KEY)
        try:
            response = sendgrid_client.send(message)
            logger.info(f"VERIFICATION_EMAIL_SENT: {response}")
        except Exception:
            logger.exception("SEND_VERIFICATION_EMAIL_FAILED")

    def send_invite_email(
        self, user: User, to_email: str
    ) -> None:
        """Send Email to user for email verification."""

        logger = Logger("")
        message = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=to_email,
            subject="Welcome To CG Africa Portal",
            plain_text_content=f"You are added as a collaborator on CG Africa Project. Please login "
                               f"on CG Africa to view your artwork.",
        )
        sendgrid_client = SendGridAPIClient(settings.SENDGRID_API_KEY)
        try:
            response = sendgrid_client.send(message)
            logger.info(f"INVITE_EMAIL_SENT: {response}")
        except Exception:
            logger.exception("SEND_INVITE_EMAIL_FAILED")

    def send_forgot_password_email(
        self, user: User, to_email: str, verification_link: str
    ) -> None:
        """Send Email to user to reset password."""
        logger = Logger("")
        message = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=to_email,
            subject="RESET YOUR PASSWORD",
            plain_text_content=f"Please click on below link to reset your password, {verification_link}",
        )

        sendgrid_client = SendGridAPIClient(settings.SENDGRID_API_KEY)
        try:
            response = sendgrid_client.send(message)
            logger.info(f"VERIFICATION_EMAIL_SENT: {response}")
        except Exception:
            logger.exception("SEND_VERIFICATION_EMAIL_FAILED")



class TokenGenerator(PasswordResetTokenGenerator):
    """
    This component generates a unique verification token.
    It is used when sending an email to for verification and password reset.
    """

    def _make_hash_value(self, user, timestamp):
        try:
            username = user.get("username")
        except AttributeError:
            username = user.username

        return str(username) + str(timestamp)