from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction ,QFont

# Version (V.2.5)
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showMaximized()

        self.init_ui()
        self.dataio()

    def dataio(self):
        self.data_read = open('data.html','r')
        self.main.append(self.data_read.read())
        self.data_read.close()

    def init_ui(self):

        self.main = QTextEdit(self)
        self.setCentralWidget(self.main)

        self.tb = QToolBar()

        self.save = QAction('save')
        self.save.triggered.connect(self.save_content)

        self.sep0 = QAction('|')
        self.sep0.setDisabled(True)
        self.copy = QAction('copy')
        self.copy.triggered.connect(self.main.copy)

        self.cut = QAction('cut')
        self.cut.triggered.connect(self.main.cut)

        self.paste = QAction('paste')
        self.paste.triggered.connect(self.main.paste)

        self.sep = QAction('|')
        self.sep.setDisabled(True)

        self.sep2 = QAction('|')
        self.sep2.setDisabled(True)

        self.font_family = QFontComboBox()
        self.font_family.currentFontChanged.connect(self.font_changed)

        self.font_size = QSpinBox()
        self.font_size.valueChanged.connect(self.font_size_changed)
        self.font_size.setValue(int(self.main.fontPointSize()))

        self.font_color = QAction('fg')
        self.font_color.triggered.connect(self.choose_fg)

        self.font_bg_color = QAction('bg')
        self.font_bg_color.triggered.connect(self.choose_bg)

        self.bold = QAction('BOLD')
        self.bold.triggered.connect(self.makeItBold)

        self.italic = QAction('italic')
        self.italic.triggered.connect(self.makeItItalic)

        self.underline = QAction('underline')
        self.underline.triggered.connect(self.markUnderline)

        self.tb.addAction(self.save)
        self.tb.addAction(self.sep0)
        self.tb.addAction(self.copy)
        self.tb.addAction(self.cut)
        self.tb.addAction(self.paste)
        self.tb.addAction(self.sep)
        self.tb.addWidget(self.font_family)
        self.tb.addWidget(self.font_size)
        self.tb.addAction(self.font_color)
        self.tb.addAction(self.font_bg_color)
        self.tb.addAction(self.sep2)
        self.tb.addAction(self.bold)
        self.tb.addAction(self.italic)
        self.tb.addAction(self.underline)
        self.addToolBar(self.tb)
        font = QFont('Times', 12)

        self.update_widgets = [self.font_family, self.font_size]
        self.main.setFont(font)
        self.main.selectionChanged.connect(self.update_text)

    def update_text(self):
        for widgets in self.update_widgets:
            widgets.blockSignals(True)
        self.font_family.setCurrentFont(QFont(self.main.currentFont()))
        self.font_size.setValue(int(self.main.fontPointSize()))
        for widgets in self.update_widgets:
            widgets.blockSignals(False)

    def font_changed(self):
        self.main.setCurrentFont(QFont(self.font_family.currentFont()))

    def font_size_changed(self):
        self.main.setFontPointSize(self.font_size.value())

    def choose_fg(self):
        self.fg_box = QColorDialog()
        self.fg_box.open()
        self.main.setTextColor(self.fg_box.getColor())

    def choose_bg(self):
        self.bg_box = QColorDialog()
        self.bg_box.open()
        self.main.setTextBackgroundColor(self.bg_box.getColor())

    def makeItBold(self):
        self.main.setFontWeight(700)

    def makeItItalic(self):
        self.main.setFontItalic(True)

    def markUnderline(self):
        self.main.setFontUnderline(True)

    def save_content(self):
        self.to = self.main.toHtml()
        self.data_write = open('data.html','w')
        self.data_write.write(self.to)
        self.data_write.close()

a = QApplication([])

w = Window()
w.show()
a.exec()
