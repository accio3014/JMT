import sys
from PyQt5.QtWidgets import *
import requests
from bs4 import BeautifulSoup
import Jonna_Michine_Tool
import time

WIDTH = 700
HEIGHT = 400

path = ""
exploitCategory = ""

query = []

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a new file
        # newFile = QAction('&new', self)
        # newFile.setShortcut('Ctrl+N')
        # newFile.setStatusTip('New file')
        # newFile.triggered.connect(self.newFile)
        
        selectFile = QAction('&select', self)
        selectFile.setShortcut('Ctrl+O')
        selectFile.setStatusTip('Select file')
        selectFile.triggered.connect(self.selectFile)
        
        # quitFile = QAction('&exit', self)
        # quitFile.setShortcut('Ctrl+Q')
        # quitFile.setStatusTip('Exit application')
        # quitFile.triggered.connect(qApp.quit)
        
        # edit_m = menubar.addMenu('&Edit')
        # view_m = menubar.addMenu('&View')
        # tools_m = menubar.addMenu('&Tooles')
        # help_m = menubar.addMenu('&Help')
        
        self.statusBar()
        
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        file_m = menubar.addMenu('&File')
        
        # file_m.addAction(newFile)
        file_m.addAction(selectFile)
        # file_m.addAction(quitFile)
        
        self.search_widget = SearchWidget()
        self.setCentralWidget(self.search_widget)
        
        self.setWindowTitle('Web vulnerability check')

        # Setting GUI place
        screen = app.desktop().screenGeometry()
        width, height = screen.width(), screen.height()
        self.setGeometry(int(width/2) - int(WIDTH/2), int(height/2) - int(HEIGHT/2), WIDTH, HEIGHT)

        self.show()
        
    
    # def newFile(self):
    #     nFile = QFileDialog.getSaveFileName(self, 'New file', './')
        
    def selectFile(self):
        global path, exploitCategory

        pathInfo = []

        # Select file and get path
        # oFile = QFileDialog.getOpenFileName(self, 'Select file', './', 'TextFile(*.txt);; All File(*)')
        selectFile = QFileDialog.getOpenFileName(self, 'Select file', './', 'TextFile(*.txt)')
        path = selectFile[0]
        pathInfo = path.split('/')
        fileName = pathInfo[-1].split('.')
        fileNameSpace = fileName[0].split('-')
        for i in fileNameSpace:
            if(fileNameSpace.index(i) == (len(fileName)-1)):
                exploitCategory += i
            else:
                exploitCategory += i + " "
        
        if(len(exploitCategory) != 0):
            self.showAlert("Success", "Successfully loading [" + exploitCategory + "." + fileName[-1] + "] file")
        else:
            self.showAlert("Fail", "Please select *.txt file")


        # print(pathInfo)
        # print(path)     # 선택한 파일 경로

    def showAlert(self, title: str, content: str):
        
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(content)
        msg.setStandardButtons(QMessageBox.Ok)
        
        if QMessageBox.Ok:
            msg.exec_()
        

class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.le = QLineEdit()
        self.le.setPlaceholderText('Enter your website URL')
        self.le.returnPressed.connect(self.crawl_view)

        
        self.btn = QPushButton('Exploit')
        self.btn.clicked.connect(self.crawl_view)
        
        self.lbl = QLabel('')

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        grid = QGridLayout()
        grid.addWidget(self.le, 0, 0, 1, 3)
        grid.addWidget(self.btn, 0, 3, 1, 1)
        grid.addWidget(self.lbl, 1, 0, 1, 4)
        grid.addWidget(self.tb, 2, 0, 1, 4)
        self.setLayout(grid)


    def crawl_view(self):
        global query
        # search_url = self.le.text()
        search_url = "test"
        
        if search_url:
            self.tb.clear()
            if(len(exploitCategory) != 0):
                query = Jonna_Michine_Tool.readCategory(path)
                
                self.lbl.setText('Google Search Results for [' + search_url + '] URL')
                self.tb.append("GHDB Category ····· " + exploitCategory + '\n')
                # for i in range(2):
                #     p, sync = Jonna_Michine_Tool.exploitGHDB(path, i)
                #     time.sleep(1)
                #     if(sync == 1):
                #         self.tb.append("[Exploit] ····· " + p)
                #     elif(sync == 0):
                #         self.tb.append("[Fail] ····· " + p)

                p, sync = Jonna_Michine_Tool.exploitGHDB(path, 0)
                time.sleep(1)
                if(sync == 1):
                    self.tb.append("[Exploit] ····· " + p)
                elif(sync == 0):
                    self.tb.append("[Fail] ····· " + p)

                # p, sync = Jonna_Michine_Tool.exploitGHDB(path, 1)
                # time.sleep(1)
                # if(sync == 1):
                #     self.tb.append("[Exploit] ····· " + p)
                # elif(sync == 0):
                #     self.tb.append("[Fail] ····· " + p)
                
                # p, sync = Jonna_Michine_Tool.exploitGHDB(path, 2)
                # time.sleep(1)
                # if(sync == 1):
                #     self.tb.append("[Exploit] ····· " + p)
                # elif(sync == 0):
                #     self.tb.append("[Fail] ····· " + p)

                self.tb.append("\n\n[Done]")
            else:
                self.showAlert("ERROR", "Please select category file.")
                # self.tb.append("ERROR!!! Please select category file.")
            
            # website_url = 'https://www.google.com'
            # url = website_url + search_url
            # r = requests.get(url)
            # html = r.content
            # soup = BeautifulSoup(html, 'html.parser')
            # titles_html = soup.select('.search-results > li > article > div > h1 > a')

            # for i in range(len(titles_html)):
            #     title = titles_html[i].text
            #     link = titles_html[i].get('href')
            #     self.tb.append(str(i+1) + '. ' + title + ' (' + '<a href="' + link + '">Link</a>' + ')')

    # 
    def showAlert(self, title: str, content: str):
        
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(content)
        msg.setStandardButtons(QMessageBox.Ok)
        
        if QMessageBox.Ok:
            msg.exec_()

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = MyWindow()

    
    sys.exit(app.exec_())
    
