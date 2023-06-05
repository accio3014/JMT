import sys
from PyQt5.QtWidgets import *
import Jonna_Michine_Tool
import time
import random

# Screen Size
WIDTH = 700
HEIGHT = 400

path = ""
exploitCategory = ""
result_time = ""

querys = []

# read exploit file and setting querys
def readCategory(path):
    global querys

    f = open(path, 'r')

    while(True):
        line = f.readline()
        if(not(line)):
            break
        
        line = line[:-1]
        querys.append(line)
        
    f.close()

def writeTitle(search_url, result_time, exploitCategory):
    result = open("./report_" + result_time + ".md", "a") 
    result.write('# %s [ %s] \n</br>\n\n' % (search_url, exploitCategory))           # Write heading of report file (URL, Category)

def reCAPTCHAList(result_time, query):
    result = open("./reCAPTCHAList_" + result_time + ".txt", "a")
    result.write('%s\n' % query)           # Write reCAPTCHA query list.

# Setting GUI
class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    # Setting screen
    def initUI(self):
        
        # Title
        self.setWindowTitle('Web vulnerability check')
        
        # Setting status bar in menu bar
        selectFile = QAction('&select', self)
        selectFile.setShortcut('Ctrl+O')
        selectFile.setStatusTip('Select file')
        selectFile.triggered.connect(self.selectFile)
        self.statusBar()
        
        # Setting menu bar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        file_m = menubar.addMenu('&File')
        file_m.addAction(selectFile)
        
        # Setting file select
        self.search_widget = SearchWidget()
        self.setCentralWidget(self.search_widget)

        # Setting GUI place
        screen = app.desktop().screenGeometry()
        width, height = screen.width(), screen.height()
        self.setGeometry(int(width/2) - int(WIDTH/2), int(height/2) - int(HEIGHT/2), WIDTH, HEIGHT)

        self.show()


    # Select file
    def selectFile(self):
        global path, exploitCategory

        pathInfo = []

        # Select file and get path
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
        
        # Check file
        if(len(exploitCategory) != 0):
            self.showAlert("Success", "Successfully loading [" + exploitCategory + "." + fileName[-1] + "] file")
        else:
            self.showAlert("Fail", "Please select *.txt file")
                
        print(path)     # file path


    # Alert
    def showAlert(self, title: str, content: str):
        
        # Setting alert
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

        # Insert URL
        self.le = QLineEdit()
        self.le.setPlaceholderText('Enter your website URL')
        self.le.returnPressed.connect(self.crawl_view)

        # Exploit button
        self.btn = QPushButton('Exploit')
        self.btn.clicked.connect(self.crawl_view)
        
        self.lbl = QLabel('')

        # Result screen
        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        # Layout
        grid = QGridLayout()
        grid.addWidget(self.le, 0, 0, 1, 3)
        grid.addWidget(self.btn, 0, 3, 1, 1)
        grid.addWidget(self.lbl, 1, 0, 1, 4)
        grid.addWidget(self.tb, 2, 0, 1, 4)
        self.setLayout(grid)


    # Run crawling
    def crawl_view(self):
        global exploitCategory, query

        search_url = self.le.text()
        result_time = time.strftime("%Y%m%d%H%M%S")
        
        if(search_url):
            self.tb.clear()
            if(len(exploitCategory) != 0):
                readCategory(path)
                # print(querys)    # check querys

                writeTitle(search_url, result_time, exploitCategory)
                
                self.lbl.setText('Google Search Results for [' + search_url + ']')
                self.tb.append("GHDB Category ····· " + exploitCategory + '\n')

                # Exploit
                for query in querys:
                    sync = Jonna_Michine_Tool.exploitGHDB(query, search_url, result_time)

                    time.sleep(random.randint(1, 2))                # Avoid bot detection
                    if(sync == "Exploit"):
                        self.tb.append("<p style='color:#FFF978'>[Exploit]&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;····· %s</p>" % query)
                    elif(sync == "Fail"):
                        self.tb.append("<p style='color:#696969'>[Fail]&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ····· %s</p>" % query)
                    elif(sync == "reCAPTCHA"):
                        reCAPTCHAList(result_time, query)
                        self.tb.append("<p style='color:#5F87E1'>[reCAPTCHA]&nbsp; &nbsp;····· %s</p>" % query)
                    
                    # Code that immediately applies the contents of the loop statement to the gui.
                    QApplication.processEvents()

                self.tb.append("\n\n[Done]")
                exploitCategory = ""
                querys = []
            else:
                self.showAlert("ERROR", "Please select category file.")
                exploitCategory = ""
                querys = []
        else:
            self.showAlert("ERROR", "Please insert URL.")
            exploitCategory = ""
            querys = []

                
    # Setting alert
    def showAlert(self, title: str, content: str):
        # Setting alert
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(content)
        msg.setStandardButtons(QMessageBox.Ok)
        
        if QMessageBox.Ok:
            msg.exec_()


# Run
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    app.setStyle('Dark')
    ex = MyWindow()

    sys.exit(app.exec_())