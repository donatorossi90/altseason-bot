import requests
import time
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except:
        pass

def get_btc_dominance():
    url = "https://api.coingecko.com/api/v3/global"
    try:
        data = requests.get(url).json()
        return data["data"]["market_cap_percentage"]["btc"]
    except:
        return None

def main():
    while True:
        dominance = get_btc_dominance()
        if dominance and dominance < 50:
            send_alert(f"⚠️ BTC Dominance in calo: {dominance:.2f}%")
        time.sleep(3600)

if __name__ == "__main__":
    send_alert("✅ Bot avviato e monitoraggio iniziato.")
    main()
