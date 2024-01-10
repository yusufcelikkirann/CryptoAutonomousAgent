import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
import pyqtgraph as pg
from binance.client import Client
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
from datetime import datetime

# Binance API anahtarları
api_key = 'wss://stream.binance.com:9443/stream?streams='
api_secret = 'YOUR_API_SECRET'

# Binance Client oluştur
client = Client(api_key, api_secret)

# İlgili varlık ve zaman aralığı
symbol = 'BTCUSDT'
interval = '1h'  # Saatlik veri çekmek için

# Kripto verilerini getirme fonksiyonu
def get_crypto_data(symbol, interval, limit=500):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    data = [{'timestamp': datetime.utcfromtimestamp(item[0] / 1000),
             'open': float(item[1]),
             'high': float(item[2]),
             'low': float(item[3]),
             'close': float(item[4]),
             'volume': float(item[5])} for item in klines]
    return data

# Veriyi al
crypto_data = get_crypto_data(symbol, interval)

# Veriyi DataFrame'e çevirme
df = pd.DataFrame(crypto_data)
df.set_index('timestamp', inplace=True)

# Grafiği oluştur
mpf.plot(df, type='candle', style='yahoo', volume=True, title='Binance BTC/USDT Grafiği', ylabel='Fiyat', ylabel_lower='Hacim', figscale=1.5, figratio=(10, 6), mav=(10, 20))

# Grafiği göster
plt.show()

# Grafiği dosyaya kaydet
plt.savefig('coin_chart.png')

class MyWindow(QGraphicsView):
    def __init__(self):
        super().__init__()

        # QGraphicsScene oluştur
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # PyQtGraph PlotWidget oluştur
        self.plot_widget = pg.PlotWidget()
        self.scene.addWidget(self.plot_widget)

        # Coin chart verilerini ekleyin (örneğin)
        x = [0, 1, 2, 3, 4]
        y = [0, 1, 4, 9, 16]
        self.plot_widget.plot(x, y, pen='r')  # Örnek veriler, gerçek verilerinizi ekleyin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    plt.savefig('coin_chart2.png')
    sys.exit(app.exec_())
