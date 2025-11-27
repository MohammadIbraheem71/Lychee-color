from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Signal
from welcome_ui import Ui_WelcomeForm

class WelcomeWindow(QWidget):
    image_selected = Signal(str)  #this sends the image path to main window
    
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_WelcomeForm()
        self.ui.setupUi(self)
        
        #connect the select image button to function
        self.ui.selectImageButton.clicked.connect(self.select_image)
    
    def select_image(self):
        #open file box for picking image
        file_name, _ = QFileDialog.getOpenFileName(
            self, "open image", "", "images (*.png *.jpg *.jpeg *.bmp)"
        )
        
        #if user picked file then send it
        if file_name:
            self.image_selected.emit(file_name)
