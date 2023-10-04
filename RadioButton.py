import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

verdana_font = QFont("Verdana", 12)

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRadioButton Kullanımı")
        self.setGeometry(400, 100, 600, 400)
        self.arayuz()
    
    def arayuz(self):
        self.yazi = QLabel("Merhaba Python", self)
        self.yazi.setFont(verdana_font)
        self.yazi.move(200, 50)
        self.yazi.resize(300, 20)
        
        self.isim_kutusu = QLineEdit(self)
        self.isim_kutusu.move(200, 100)
        self.isim_kutusu.setPlaceholderText("Lütfen İsminizi Giriniz.")
        
        self.soyisim_kutusu = QLineEdit(self)
        self.soyisim_kutusu.move(200, 150)
        self.soyisim_kutusu.setPlaceholderText("Lütfen Soyisminizi Giriniz.")
        
        self.cinsiyet_label = QLabel("Cinsiyet:", self)
        self.cinsiyet_label.setFont(verdana_font)
        self.cinsiyet_label.move(200, 200)
        
        self.erkek_radio = QRadioButton("Erkek", self)
        self.erkek_radio.setFont(verdana_font)
        self.erkek_radio.move(280, 200)
        
        self.kadin_radio = QRadioButton("Kadın", self)
        self.kadin_radio.setFont(verdana_font)
        self.kadin_radio.move(360, 200)
        
        self.buton_kaydet = QPushButton("Kaydet", self)
        self.buton_kaydet.setFont(verdana_font)
        self.buton_kaydet.move(200, 300) 
        self.buton_kaydet.clicked.connect(self.fonksiyon_kaydet)
   
        self.show()
        
    def fonksiyon_kaydet(self):
        isim = self.isim_kutusu.text()
        soy_isim = self.soyisim_kutusu.text()
   
        if self.erkek_radio.isChecked():
            cinsiyet = "Erkek"
        elif self.kadin_radio.isChecked():
            cinsiyet = "Kadın"
        else:
            cinsiyet = "Belirtilmemiş"
            
        print(f"İsminiz: {isim} -- Soyisminiz: {soy_isim} -- Cinsiyetiniz: {cinsiyet}")    

uygulama = QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec_())