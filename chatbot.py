import sys
import openai

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

openai.api_key = "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"


class EnglishChat(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200,700)

        self.init_ui()

    def init_ui(self):
        vb = QVBoxLayout()
        self.setLayout(vb)

        hb = QHBoxLayout()
        vb.addLayout(hb)

        hb1 = QHBoxLayout()
        vb.addLayout(hb1)

        vb1 = QVBoxLayout()
        hb1.addLayout(vb1)

        self.chat_btn = QPushButton("Chat")
        self.chat_btn.clicked.connect(self.generate_response)
        vb1.addWidget(self.chat_btn)

        vb1.addStretch()

        self.splitter = QSplitter()
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        hb1.addWidget(self.splitter)

        self.vsplitter1 = QSplitter()
        self.vsplitter1.setOrientation(Qt.Orientation.Vertical)
        self.splitter.addWidget(self.vsplitter1)

        self.vsplitter2 = QSplitter()
        self.vsplitter2.setOrientation(Qt.Orientation.Vertical)
        self.splitter.addWidget(self.vsplitter2)
#ukuran prompt dan tulisan
        self.prompt_box = QTextEdit()
        self.prompt_box.setFont(QFont("Calibri", 20))
        self.vsplitter1.addWidget(self.prompt_box)
#pertanyaan
        self.learning_page = QWebEngineView()
        self.learning_page.setFont(QFont("Calibri", 16))
        self.vsplitter1.addWidget(self.learning_page)

        self.response_box = QTextBrowser()
        self.response_box.setFont(QFont("Calibri", 20))
        self.vsplitter2.addWidget(self.response_box)

        self.vsplitter1.setSizes([int(self.splitter.height()* .30), int(self.splitter.height()*.70)])


    def generate_response(self):
        prompt = self.prompt_box.toPlainText()

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt = prompt,
            n=1,
            max_tokens=2048,
            temperature=.5
        )

        response = response.choices[0].text

        self.response_box.setText(response)


def main():
    app = QApplication(sys.argv)
    gui = EnglishChat()
    gui.show()
    app.exec()

if __name__ == '__main__':
     main()

