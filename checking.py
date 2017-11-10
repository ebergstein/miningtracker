# Ezra Bergstein
# 10/13/17
# Monitoring Project
import os, serial
import psutil
import datetime, time
import sys
import math
import re
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QGridLayout, QLabel, QComboBox, QVBoxLayout, QMenuBar, \
    QMenu, QStatusBar, QMainWindow, QLineEdit, QSizePolicy
from PyQt5.QtCore import QUrl, QRect, QMetaObject
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt5.Qt import Qt
from bs4 import BeautifulSoup


#Keeps track of power usage
class Power:
    def __init__(self):
        self.usage = 0.0

    def update(self):
        self.usage = psutil.cpu_percent()
        return self.usage

#Renders a web page
def render(app, source_url):
    class Render(QWebEngineView):
        def __init__(self, app, url):
            self.html = None
            self.app = app
            #Creates a new webpage
            QWebEngineView.__init__(self)
            #Makes the page call the _loadfinished function once the page finishes loading, with the resulting page as
            #a result
            self.loadFinished.connect(self._loadFinished)
            #Loads a page from a url
            self.load(QUrl(url))
            #Renders the webpage
            self.app.exec_()

        def _loadFinished(self, result):
            #Creates an HTML version of the page, then calls _callable with the result
            self.page().toHtml(self._callable)

        def _callable(self, data):
            self.html = data
            self.app.quit()

    #Formats the page properly
    return Render(app, source_url).html


# Most of the code of this class was generated with PyQTDesigner
class Ui_MainWindow(object):
    def setupUi(self, MainWindow, usa_text, check, money):
        #MainWindow is the window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1947, 1439)
        MainWindow.setWindowTitle("Tracking")
        #Sets a stylesheet for the window, similar to CSS
        MainWindow.setStyleSheet('''
            QLabel {
                border-top: 2px solid black;
                border-right: 2px solid black;
                border-left: 2px solid black;
                border-top-left-radius: 3px;
                border-top-right-radius: 3px;
                padding: 3px;
                background-color: rgba(0, 0, 0, 0.5);
                color: Yellow;
            }
            QLabel#label_9, QLabel#label_10 {
                border-top: 0px solid black;
                border-right: 2px solid black;
                border-left: 2px solid black;
                border-top-left-radius: 0px;
                border-top-right-radius: 0px;
                padding: 3px;
                background-color: rgba(0, 0, 0, 0.5);
                color: Yellow;
            }
            QLineEdit {
                border: 2px solid black;
            }
            QComboBox {
                border-left: 2px solid black;
                border-right: 2px solid black;
                border-bottom: 2px solid black;
                border-bottom-left-radius: 3px;
                border-bottom-right-radius: 3px;
                padding: 1px 18px 1px 3px;
                min-width: 6em;
            }
            QComboBox:editable {
                background-color: rgba(128, 128, 128, 0.6);
            }
            QComboBox:!editable, QComboBox::drop-down:editable {
                background-color: rgba(128, 128, 128, 0.5);
            }
            QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                background-color: rgba(128, 128, 128, 0.5);
            }
        ''')
        #sets the background gradient for the window
        palette = QPalette()
        #where the gradiant starts and ends
        gradient = QLinearGradient(0, 0, 200, 1000)
        gradient.setColorAt(0.0, QColor(135, 206, 235))
        gradient.setColorAt(1.0, QColor(65, 125, 225))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        MainWindow.setPalette(palette)
        self.money = float(money)
        self.currency = "usd"
        self.table_source = "usa"
        self.source = "sha256"
        self.cpu_time = "hour"
        self.power_time = "hour"
        self.mining = "btc"
        self.hashing = "4793"
        self.cost = "0.12"
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Sets the Layout of the window.  This one sorts all elements that it contains into a grid.
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        #This layout arranges elements from top to bottom
        self.verticalLayout = QVBoxLayout()
        #setSpacing dictates the distance between objects in a layout.  A value of 0 is used to fake the text and the
        #dropdown menu being in the same window.
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        #This is a Piece of Text
        self.label = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label.setFont(font)
        #Sets the alignment of the label
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label.setText(check)
        #Adds the label to a layout
        self.verticalLayout.addWidget(self.label)
        #This is a dropdown menu
        self.comboBox_5 = QComboBox(self.centralwidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("Hour")
        self.comboBox_5.addItem("Day")
        self.comboBox_5.addItem("Week")
        self.comboBox_5.addItem("Month")
        self.comboBox_5.addItem("Year")
        self.comboBox_5.setFont(font)
        #Calls the updateCPUPeriod function when an item is selected, and passes the item's name as input.
        self.comboBox_5.activated[str].connect(self.updateCPUPeriod)
        self.verticalLayout.addWidget(self.comboBox_5)
        #Adds the vertical layout to a section of the grid
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Power Usage: 1293w\nPower usage from the past hour: 25000w")
        self.verticalLayout_2.addWidget(self.label_2)
        self.comboBox_4 = QComboBox(self.centralwidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("Hour")
        self.comboBox_4.addItem("Day")
        self.comboBox_4.addItem("Week")
        self.comboBox_4.addItem("Month")
        self.comboBox_4.addItem("Year")
        self.comboBox_4.setFont(font)
        self.comboBox_4.activated[str].connect(self.updatePowerPeriod)
        self.verticalLayout_2.addWidget(self.comboBox_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 3, 1, 2)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_4.setText(usa_text)
        self.verticalLayout_4.addWidget(self.label_4)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("Usa")
        self.comboBox_2.addItem("Eu")
        self.comboBox_2.setFont(font)
        self.comboBox_2.activated[str].connect(self.updateCountry)
        self.verticalLayout_4.addWidget(self.comboBox_2)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Calibri")
        #size is smaller to fit the money being made into the window
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_7.setText("Money being made: \n" + str(self.money) + " " + str(self.currency) + "/h")
        self.verticalLayout_5.addWidget(self.label_7)
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("usd")
        self.comboBox_3.addItem("btc")
        self.comboBox_3.addItem("eth")
        self.comboBox_3.activated[str].connect(self.updateCurrency)
        self.comboBox_3.setFont(font)
        self.verticalLayout_5.addWidget(self.comboBox_3)
        self.gridLayout.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Current Table Source:")
        self.verticalLayout_3.addWidget(self.label_3)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("sha256")
        self.comboBox.addItem("scrypt")
        self.comboBox.addItem("x11")
        self.comboBox.activated[str].connect(self.updateSource)
        self.comboBox.setFont(font)
        self.verticalLayout_3.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 4, 1, 1)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_8.setText("Input your hash rate.")
        self.verticalLayout_6.addWidget(self.label_8)
        self.lineEdit = QLineEdit(self.centralwidget)
        #Constrains the text box's length to the current size of the window
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)
        self.lineEdit.textChanged[str].connect(self.updateHashing)
        self.lineEdit.setText(self.hashing)
        self.verticalLayout_6.addWidget(self.lineEdit)
        self.label_9 = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_9.setText("Input your power bill \nin cost per kilowatt per hour.")
        self.verticalLayout_6.addWidget(self.label_9)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setText(self.cost)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.textChanged[str].connect(self.updateCost)
        self.verticalLayout_6.addWidget(self.lineEdit_2)
        self.label_10 = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_10.setText("Select the currency that \nyou are mining.")
        self.verticalLayout_6.addWidget(self.label_10)
        self.comboBox_4 = QComboBox(self.centralwidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("Bitcoin")
        self.comboBox_4.addItem("Etherium")
        self.comboBox_4.setFont(font)
        self.comboBox_4.activated[str].connect(self.updateMining)
        self.verticalLayout_6.addWidget(self.comboBox_4)
        self.gridLayout.addLayout(self.verticalLayout_6, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        #Creates a Menu Bar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1947, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        #Creates a file menu in the menu bar
        self.menuFile.setTitle("File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #Creates a quit button that is placed in the file menu
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        #Creates a key shortcut for the action
        self.actionQuit.setShortcut('Ctrl+Q')
        self.actionQuit.triggered.connect(QApplication.quit)
        self.actionQuit.setText("Quit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        QMetaObject.connectSlotsByName(MainWindow)

    #Gets the country that the scraper pulls from
    def getCountry(self):
        return self.table_source

    def updateCountry(self, country):
        self.table_source = country

    #Updates the CPU Usage text and the usage over a period text
    def updateText(self, check, text, cpu_period):
        self.label.setText(
            check + "\nCPU Usage from the past " + self.cpu_time.lower() + ": " + str(math.ceil(cpu_period)) + " percent")
        self.label_4.setText(text)


    #Updates the currency source for the order
    def updateSource(self, source):
        self.source = source

    def getSource(self):
        return self.source

    #Updates the current period to read cpu history from
    def updateCPUPeriod(self, time):
        self.cpu_time = time

    def getCPUPeriod(self):
        return self.cpu_time

    # Updates the Power Usage text
    def updatePowerPeriod(self, time):
        self.power_time = time
        self.label_2.setText("Power Usage: 1293w\nPower usage from the past " + self.power_time.lower() + ": 2500w")

    def getPowerPeriod(self):
        return self.power_time

    #Changes the source that is being mined
    def updateMining(self, source):
        if source == "Bitcoin":
            self.mining = "btc"
            self.hashing = "4723"
            self.lineEdit.setText(self.hashing)
        else:
            self.mining = "eth"
            self.hashing = "20"
            self.lineEdit.setText(self.hashing)

    def getMining(self):
        return self.mining

    #Updates the Hash rate
    def updateHashing(self, rate):
        if re.match("^[0-9\.]*$", rate):
            self.hashing = rate

    #Updates the power bill
    def updateCost(self, rate):
        if re.match("^[0-9\.]*$", rate):
            self.cost = rate

    def getCost(self):
        return self.cost

    def getHashing(self):
        return self.hashing

    #updates the currency that the money being made is displayed in
    def updateCurrency(self, currency):
        self.currency = currency

    def getCurrency(self):
        return self.currency

    #updates the money being made
    def updateMoney(self, money):
        self.money = float(money)
        temp = self.money
        if self.currency == "btc":
            temp = temp * .00015
        elif self.currency == "eth":
            temp = temp * .0035
        else:
            temp = temp * 1.00
        self.label_7.setText("Money being made: \n" + str(temp) + " " + str(self.currency) + "/h")




#Reads the current CPU Usage, logs it, and returns it.
def start(power):
    current = datetime.datetime.today()
    total = power.update()
    usage = "CPU Usage is at " + str(math.ceil(total)) + " percent"
    #Creates the file if it is not present locally.
    file = open("cpu_usage.txt", "a+")
    file.close()
    file = open("cpu_usage.txt", "r+")
    #Reads through all of the content of the file
    content = file.read()
    #Jumps to the start of the file
    file.seek(0, 0)
    #Writes the current update to the top of the file.
    file.write((str(current) + " " + str(total)).rstrip("\r\n") + "\n" + content)
    file.close()
    return usage


#Creates a time delta based on the current time and the inputted time period.
def update_time(time):
    current = datetime.datetime.today()
    if time == "Hour":
        past = current - datetime.timedelta(hours=1)
    elif time == "Day":
        past = current - datetime.timedelta(days=1)
    elif time == "Week":
        past = current - datetime.timedelta(weeks=1)
    elif time == "Month":
        past = current - datetime.timedelta(weeks=4)
    else:
        past = current - datetime.timedelta(weeks=52)
    return past


#Gets the average amount of CPU Usage based on the current time and the inputted time delta.
def update_cpu_period(delta):
    current = datetime.datetime.today()
    file = open("cpu_usage.txt", "a+")
    file.close()
    file = open("cpu_usage.txt", "r+")
    cpu_list = file.readlines()
    file.close()
    total = 0.0
    counted = 0
    for line in cpu_list:
        words = line.split()
        #Makes a new date from the current line
        date = datetime.datetime.strptime((words[0] + " " + words[1]), '%Y-%m-%d %X.%f')
        #Exits if the date goes past the current time period
        if current - date > current - delta:
            break
        total += float(words[len(words) - 1])
        counted += 1
    return total / counted


#Gets a table from the scraped wep page
def get_table(country, soup):
    table = soup.find("div", attrs={"class": country}).find("tbody").find_all("tr")
    return table


#Updates the order
def iterate(table, start):
    result = start
    #Gets the first order from the table
    raw = table[0].get_text(" ", strip=True).split()
    #Orders will start with F or S if the order is fixed or Standard, then go to the order id.  Dead orders start with
    # the order id.  This is to keep place with the varying length orders.
    place = 0
    if raw[place] == "F" or raw[place] == "S":
        result += "Order " + raw[1] + ":\n"
        if raw[place] == "F":
            result += "Fixed\n"
        else:
            result += "Standard\n"
        place = 2
    else:
        result += "Order " + raw[0] + ":\nDead\n"
        place = 1
    result += "Price: " + raw[place] + "\nLimit: " + raw[place + 1] + "\nMiners: " + raw[place + 2] + "\nSpeed: " + \
              raw[place + 3] + "\n"
    return result


if __name__ == "__main__":

    power = Power()
    #Sets up the application
    app = QApplication(sys.argv)
    site = "https://www.nicehash.com/marketplace/"
    source = "sha256"
    cpu_length = "hour"
    request = render(app, site + source)
    # Scrapes a website
    soup = BeautifulSoup(request, "html.parser")
    #Scrapes a website
    usa_table = get_table("usa", soup)
    eu_table = get_table("eu", soup)
    text = iterate(usa_table, "US Orders:\n")
    check = start(power)
    currency = "btc"
    hashing = "4730"
    powerdraw = "1293"
    cost = "0.12"
    #Using webscraping again for money calculations because I was unable to find any formulas to calculate money being
    #made per hour mining
    calcsite = "https://www.cryptocompare.com/mining/calculator/" + currency + "?HashingPower=" + hashing + \
               "&HashingUnit=GH%2Fs&PowerConsumption=" + powerdraw + "&CostPerkWh=" + cost
    calcrequest = render(app, calcsite)
    calcsoup = BeautifulSoup(calcrequest, "html.parser")
    calcvalues = calcsoup.find("div", attrs={"class": "calculator-container"}).find_all("div", attrs={"class": "calculator-value ng-binding"})
    #money being made per hour
    calcvalue = calcvalues[0].get_text(" ", strip=True).split()
    #Creates the window
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    #Sets up the ui
    ui.setupUi(MainWindow, text, check, calcvalue[1])
    MainWindow.show()
    while True:
        if ui.getCountry() == "usa":
            text = iterate(usa_table, "US Orders:\n")
        else:
            text = iterate(eu_table, "EU Orders:\n")
        check = start(power)
        cpu_type = ui.getCPUPeriod()
        cpu_delta = update_time(cpu_type)
        cpu_period_text = update_cpu_period(cpu_delta)
        ui.updateText(check, text, cpu_period_text)
        source = ui.getSource()
        request = render(app, site + source)
        # The request will be none if the user quit.
        if request is None:
            MainWindow.close()
            sys.exit(app.quit())
        soup = BeautifulSoup(request, "html.parser")
        usa_table = get_table("usa", soup)
        eu_table = get_table("eu", soup)
        currency = ui.getMining()
        hashing = ui.getHashing()
        cost = ui.getCost()
        if currency == "btc":
            calcsite = "https://www.cryptocompare.com/mining/calculator/" + currency + "?HashingPower=" + hashing + \
                   "&HashingUnit=GH%2Fs&PowerConsumption=" + powerdraw + "&CostPerkWh=" + cost
        else:
            calcsite = "https://www.cryptocompare.com/mining/calculator/" + currency + "?HashingPower=" + hashing + \
                       "&HashingUnit=MH%2Fs&PowerConsumption=" + powerdraw + "&CostPerkWh=" + cost
        calcrequest = render(app, calcsite)
        if calcrequest is None:
            MainWindow.close()
            sys.exit(app.quit())
        calcsoup = BeautifulSoup(calcrequest, "html.parser")
        calcvalues = calcsoup.find("div", attrs={"class": "calculator-container"}).find("div", attrs={
            "class": "calculator-value ng-binding"})
        calcvalue = calcvalues.get_text(" ", strip=True).split()
        ui.updateMoney(calcvalue[1])
