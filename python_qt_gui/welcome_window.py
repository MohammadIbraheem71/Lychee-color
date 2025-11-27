from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Signal
from welcome_ui import Ui_WelcomeForm

class WelcomeWindow(QWidget):
    image_selected = Signal(str)  # Signal to emit selected image path
    
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_WelcomeForm()
        self.ui.setupUi(self)
        
        # Connect button
        self.ui.selectImageButton.clicked.connect(self.select_image)
    
    def select_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        
        if file_name:
            self.image_selected.emit(file_name)
