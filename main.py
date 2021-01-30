import PyQt5.QtWidgets as qtw
import bidscan
import agency


class MainWindow(qtw.QWidget):

    widgets = []

    def __init__(self):
        super().__init__()
        self.title = "Bid Request Scanner"
        self.left = 600
        self.top = 400
        self.width = 320
        self.height = 200
        self.initUI()
        self.show()

    def initUI(self):
        lbl_layout_x = 10
        lbl_layout_y = 10
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        for agency in bidscan.agencies:
            lbl_name = qtw.QLabel(agency.name, self)
            lbl_name.move(lbl_layout_x, lbl_layout_y)
            lbl_demarc = qtw.QLabel("|", self)
            lbl_demarc.move(lbl_layout_x + 130, lbl_layout_y)
            lbl_bid_scan_result = qtw.QLabel("#", self)
            lbl_bid_scan_result.move(lbl_layout_x + 160, lbl_layout_y)
            self.widgets.append(lbl_bid_scan_result)
            lbl_layout_y += 30
        btn_scan = qtw.QPushButton("Scan Websites", self)
        btn_scan.move(235, 170)
        btn_scan.clicked.connect(self.scan)

    def scan(self):
        for agency in bidscan.agencies:
            self.widgets[bidscan.agencies.index(agency)].setText(bidscan.bidscan(agency))
            self.widgets[bidscan.agencies.index(agency)].adjustSize()


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create("Fusion"))
app.exec_()
