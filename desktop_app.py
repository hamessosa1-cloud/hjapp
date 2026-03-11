import threading
import webview
import time
from app import app

def start_flask():
    app.run(port=5000)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Espera a que Flask arranque
    time.sleep(3)

    webview.create_window("Iris Predictor", "http://127.0.0.1:5000")
    webview.start()