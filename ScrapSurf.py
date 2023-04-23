from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QScrollArea, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QDesktopServices, QIcon, QFont, QPixmap
import requests
from bs4 import BeautifulSoup
import sys

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'ScrapSurf'
        self.left = 250
        self.top = 250
        self.width = 640
        self.height = 480
        self.initUI()
        self.setWindowIcon(QIcon('MYOWNPROJECTS/webscrapper/web_1.png'))

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: #0B0808; color: white;")
        font = QFont("Source Code Pro", 24, QFont.Bold)
        self.setFont(font)
        


        pixmap = QPixmap('MYOWNPROJECTS/webscrapper/web_1.png')
        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)
        self.image_label.move(150, 5)




        # add search bar and button
        self.search_bar = QLabel("Search:", self)
        self.search_bar.move(20, 170)
        self.search_bar.setFont(QFont("Source Code Pro", 14))
        self.search_input = QLineEdit(self)
        self.search_input.setGeometry(100, 170, 300, 30)
        self.search_button = QPushButton("Search", self)
        self.search_button.setGeometry(420, 170, 100, 30)
        self.search_button.setStyleSheet("background-color: #020630; color: white; font: 10pt 'Anonymous Pro';")
        self.search_button.clicked.connect(self.search)

        # create a scrollable area to hold the search results
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setGeometry(20, 200, 600, 250)
        self.scroll_area.setWidgetResizable(True)

        # create a widget to hold the search result labels
        self.search_widget = QWidget()
        self.search_layout = QVBoxLayout(self.search_widget)




        #about
        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(5, 458, 40,20)
        self.about_button.setStyleSheet("background-color: #080808; color: white; font: 10pt 'Anonymous Pro';")
        self.about_button.clicked.connect(self.open_website)






        # add labels to display search results
        self.search_labels = []
        for i in range(20):
            label = QLabel("", self)
            label.setFont(QFont("Source Code Pro", 12))
            label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            label.setOpenExternalLinks(True)
            self.search_layout.addWidget(label)
            self.search_labels.append(label)

        self.scroll_area.setWidget(self.search_widget)

        self.show()
    def open_website(self):
        # replace this with your website url
        url = "http://amithvss.ezyro.com/blog/"
        QDesktopServices.openUrl(QUrl(url))
    def search(self):
        query = self.search_input.text()
        url = f"https://www.google.com/search?q={query}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.find_all("a")
        results = []
        for link in links:
            href = link.get("href")
            if "http" in href and "google" not in href:
                results.append(href)

        # clear previous results
        for label in self.search_labels:
            label.setText("")

        # display new results
        for i, result in enumerate(results):
            if i >= len(self.search_labels):
                break
            self.search_labels[i].setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
