import requests
from config.settings import BOT_TOKEN,CHAT_ID
def send_message(name,email,subject,message):
    text = f"Ism:{name}\n,Email{email}\n,Subject:{subject}\n,Message:{message}\n"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/SendMessage?chat_id={CHAT_ID}&text= {text}" 
    requests.get(url)