from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from pyDesign import Ui_MainWindow
import requests
import sys
from PyQt5.QtGui import QPixmap
import pyqtgraph as pg
from PyQt5.QtWidgets import QButtonGroup
import time
from pyAdminDesign import Ui_MainWindow as Ui_AdminMainWindow

class YourMainWindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.adminUi = Ui_AdminMainWindow()
        self.adminWindow = QMainWindow()
        self.start_time = time.time()  # Program başlangıç zamanını sakla
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateCurrentCoinPrice)
        self.timer.timeout.connect(self.updateWorkTime)  # QTimer'a bağlanan fonksiyon
        self.timer.start(1000)





        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateCurrentCoinPrice)
        self.timer.start(2000)
        self.ui.lbProfitRatePlus.setVisible(False)
        self.ui.lbCurrentCoinPrice.setVisible(False)
        self.ui.lbProfitRate.setVisible(False)
        self.ui.lbWorkTime.setVisible(False)
        self.coinChartGroup = QButtonGroup(self)
        self.coinChartGroup.addButton(self.ui.rbEnableCoinChart)
        self.coinChartGroup.addButton(self.ui.rbDisabledCoinChart)
        self.candlestickGroup = QButtonGroup(self)
        self.candlestickGroup.addButton(self.ui.rbEnableCandlestick)
        self.candlestickGroup.addButton(self.ui.rbDisabledCandlestick)
        self.profitRateGroup = QButtonGroup(self)
        self.profitRateGroup.addButton(self.ui.rbEnableProfitRate)
        self.profitRateGroup.addButton(self.ui.rbDisabledProfitRate)
        self.ui.rbEnableCoinChart.toggled.connect(self.enableCoinChart)
        self.ui.rbDisabledCoinChart.toggled.connect(self.disableCoinChart)
        self.ui.rbEnableCandlestick.toggled.connect(self.enableCandleStickChart)
        self.ui.rbDisabledCandlestick.toggled.connect(self.disableCandleStickChart)
        self.ui.rbEnableProfitRate.toggled.connect(self.enableProfitRate)
        self.ui.rbDisabledProfitRate.toggled.connect(self.disableProfitRate)
        pixmapBottomLeft = QPixmap("leftBottomIcon.png")
        self.ui.bottomLeftImage.setPixmap(pixmapBottomLeft)
        self.ui.bottomLeftImage.setScaledContents(True)
        pixmapBottomRight = QPixmap("BUTTON.png")
        self.ui.bottomRightImage.setPixmap(pixmapBottomRight)
        self.ui.bottomRightImage.setScaledContents(True)
        self.setFixedWidth(940)
        self.setFixedHeight(640)
        self.ui.pushButton.clicked.connect(self.showAdminUi)

#COİN SEÇİLDİĞİNDE lbCurrentCoinPrice'ın güncellenmesi (Binance' dan veri çekilerek #
        
    try:
        def updateCurrentCoinPrice(self):
            selectedCoin = self.ui.comboBox.currentText()
            apiUrl = f"https://api.binance.com/api/v3/ticker/price?symbol={selectedCoin}USDT"
            response = requests.get(apiUrl)
            data = response.json()
            

            if "price" in data:
                currentPrice = float(data["price"])
                formattedPrice = "{:.2f}".format(currentPrice)
                self.ui.lbCurrentCoinPrice.setText(f"Current {selectedCoin} Price: {formattedPrice} USDT")
                self.ui.lbCurrentCoinPrice.setVisible(True)
                
                
                
            else:
                print("API doesn't work")
    except requests.RequestExceptionas as e : 
        print(f"API request falied: {e}")








        
#?Ana fonksiyonlar--------------------------------------------------------------------#

      
    def showAdminUi(self):
        self.adminUi.setupUi(self.adminWindow)    
        self.adminWindow.show()
        
        
    def updateWorkTime(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        # elapsed_time'i gün, saat, dakika, saniye cinsine dönüştür
        days, remainder = divmod(elapsed_time, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Zamanı etikete yerleştir
        work_time_text = f"according to transaction so far : {int(hours)}:{int(minutes)}:{int(seconds)}"
        self.ui.lbWorkTime.setText(work_time_text)
    
#*rbEnableCoinChart tiklendiğinde grafiğin arayüzde gözükmesi-------------------------#        
    def enableCoinChart(self):
        # rbEnableCoinChart işaretlendiğinde yapılacak işlemler
        if self.ui.rbEnableCoinChart.isChecked():
            print("Coin Chart is enabled!")
            pixmap = QPixmap("deneme1.png")   
            self.ui.coinChart.setPixmap(pixmap)  
            self.ui.coinChart.setScaledContents(True)
            self.ui.lbCoinChart.setVisible(True)
            self.ui.coinChart.setVisible(True)

#*-------------------------------------------------------------------------------------#             

 
#?-------------------------rbDisableCoinChart Fonksiyonu-------------------------------#

    def disableCoinChart(self):
        if self.ui.rbDisabledCoinChart.isChecked():
            print("Coin chart is disabled")
            self.ui.lbCoinChart.setVisible(False)
            self.ui.coinChart.setVisible(False)
#?-------------------------------------------------------------------------------------#         
    
#*rbEnableCandleStickChart Fonksiyonu--------------------------------------------------#
            
    def enableCandleStickChart(self):
        if self.ui.rbEnableCandlestick.isChecked():
            print("Candlestick chart is enable")
            pixmap = QPixmap("deneme2.png")
            self.ui.candleStickChart.setPixmap(pixmap)       
            self.ui.candleStickChart.setScaledContents(True)
            self.ui.candleStickChart.setVisible(True)
            self.ui.lbCandleStickChart.setVisible(True)     

#*-------------------------------------------------------------------------------------#
            
#?-------------------------rbDisableCandleStickChart Fonksiyonu------------------------#

    def disableCandleStickChart(self):
        if self.ui.rbDisabledCandlestick.isChecked():
            print("Candlestick chart is disable")
            self.ui.candleStickChart.setVisible(False)
            self.ui.lbCandleStickChart.setVisible(False)

#?-------------------------------------------------------------------------------------# 



#*rbEnableProfitRate Fonksiyonu--------------------------------------------------------#
            
    def enableProfitRate(self):
        if self.ui.rbEnableProfitRate.isChecked():
            self.ui.lbProfitRate.setVisible(True)
            self.ui.lbWorkTime.setVisible(True)
            self.ui.lbProfitRatePlus.setVisible(True)

#*-------------------------------------------------------------------------------------#
            

#?rbDisableProfitRate Fonksiyonu-------------------------------------------------------#

    def disableProfitRate(self):
        if self.ui.rbDisabledProfitRate.isChecked():
            self.ui.lbProfitRate.setVisible(False)
            self.ui.lbWorkTime.setVisible(False)
            self.ui.lbProfitRatePlus.setVisible(False)

#?-------------------------------------------------------------------------------------#            
                                    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = YourMainWindowClass()
    MainWindow.show()
    sys.exit(app.exec_())
