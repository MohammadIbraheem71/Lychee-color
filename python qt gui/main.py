from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from ui_main import Ui_Form  
import sys
import os


class mywindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.selectinputimage.clicked.connect(self.open_image)
        self.ui.downloadimagebutton.clicked.connect(self.save_output)

        self.input_pixmap = None
        self.output_pixmap = None
        self.input_image_path = None

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if file_name:
            self.input_image_path = file_name
            self.input_pixmap = QPixmap(file_name)

            # show input
            self.ui.inputimagelabel.setPixmap(
    self.input_pixmap.scaled(250, 250, Qt.KeepAspectRatio)
)

            self.ui.inputimagelabel.adjustSize()

            # dummy processing (copy input to output)
            self.output_pixmap = self.input_pixmap

            # show output
            self.ui.outputimagelabel.setPixmap(
    self.output_pixmap.scaled(250, 250, Qt.KeepAspectRatio)
)

            self.ui.outputimagelabel.adjustSize()

    def save_output(self):
        if self.output_pixmap:

            # extract file name without extension
            base_name = os.path.splitext(os.path.basename(self.input_image_path))[0]

            # default name
            default_name = base_name + "_output.png"

            # save dialog
            file_name, _ = QFileDialog.getSaveFileName(
                self,
                "Save Output Image",
                default_name,
                "PNG (*.png);;JPG (*.jpg)"
            )

            if file_name:
                self.output_pixmap.save(file_name)
                QMessageBox.information(self, "Saved", f"Output saved to {file_name}")

        else:
            QMessageBox.warning(self, "No Output", "No output image to save!")


# start
app = QApplication(sys.argv)
win = mywindow()
win.show()
app.exec()
