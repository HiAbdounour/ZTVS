import resend
import os
from dotenv import load_dotenv

def send_email(email:str):
    # need to verify email
    # pls ajout OTP

    load_dotenv()
    APIKEY = os.getenv('RESEND_API_KEY')

    r = resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": email,
    "subject": "Vérifier votre adresse email ZTVS",
    "html": "<p> --- Insérer ici le code OTP de connexion --- </p>"
    })