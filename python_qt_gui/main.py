import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from main_ui import Ui_Form  
import cv2 
import numpy as np  
from welcome_window import WelcomeWindow

#adding parent directory to module search
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#this is the path of model .keras file
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pseudocolor', 'colorization_model_faces.keras'))

from pseudocolor.colorization import colorize_image, perceptual_loss
from tensorflow import keras

class mywindow(QWidget):
    def __init__(self):
        super().__init__()

        #load the model for color work
        self.model = keras.models.load_model(MODEL_PATH, custom_objects={'perceptual_loss': perceptual_loss})
        print("model loaded")

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        #set window name
        self.setWindowTitle("image colorization - processing")

        #connect buttons to functions
        self.ui.selectinputimage.clicked.connect(self.open_image)
        self.ui.downloadimagebutton.clicked.connect(self.save_output)

        #make empty holders for images
        self.input_pixmap = None
        self.output_pixmap = None
        self.enhanced_pixmap = None
        self.input_image_path = None

    def load_and_process_image(self, file_name):
        #save selected image path
        self.input_image_path = file_name
        
        #send image to color function
        gray, color, enhanced = colorize_image(self.input_image_path, self.model)

        #this helper changes pil or numpy image into qpmap
        def to_qpixmap(img):
            #if it is pil image change to array
            if hasattr(img, 'mode'):
                img = np.array(img)
            
            #if it is gray image
            if len(img.shape) == 2:
                h, w = img.shape
                qimg = QImage(img.data, w, h, w, QImage.Format_Grayscale8)
            else:
                h, w, ch = img.shape
                if ch == 3:
                    qimg = QImage(img.data, w, h, w * ch, QImage.Format_RGB888)
                else:
                    qimg = QImage(img.data, w, h, w * ch, QImage.Format_RGB888)
            return QPixmap.fromImage(qimg)

        #change images to qpixmap
        self.input_pixmap = to_qpixmap(gray)
        self.output_pixmap = to_qpixmap(color)
        self.enhanced_pixmap = to_qpixmap(enhanced)

        #show gray image
        w, h = self.ui.inputimagelabel.width(), self.ui.inputimagelabel.height()
        self.ui.inputimagelabel.setPixmap(
            self.input_pixmap.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        #show color image
        w2, h2 = self.ui.outputimagelabel.width(), self.ui.outputimagelabel.height()
        self.ui.outputimagelabel.setPixmap(
            self.output_pixmap.scaled(w2, h2, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        #show enhanced image
        w3, h3 = self.ui.enhancedimage.width(), self.ui.enhancedimage.height()
        self.ui.enhancedimage.setPixmap(
            self.enhanced_pixmap.scaled(w3, h3, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

    def open_image(self):
        #open file box for pic
        file_name, _ = QFileDialog.getOpenFileName(
            self, "open image", "", "images (*.png *.jpg *.jpeg *.bmp)"
        )

        if not file_name:
            return

        self.load_and_process_image(file_name)

    def save_output(self):
        #check if image is here
        if not self.output_pixmap:
            QMessageBox.warning(self, "no output", "no output image to save!")
            return

        #make file name for saving
        base_name = os.path.splitext(os.path.basename(self.input_image_path))[0]
        default_name = base_name + "_output_image.png"

        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "save output image",
            default_name,
            "PNG (*.png);;JPG (*.jpg)"
        )

        if file_name:
            self.output_pixmap.save(file_name)
            QMessageBox.information(self, "saved", f"output saved to {file_name}")

#main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    #show welcome window first
    welcome = WelcomeWindow()
    main_window = mywindow()
    
    #connect welcome window to main window
    def on_image_selected(image_path):
        welcome.hide()
        main_window.show()
        main_window.load_and_process_image(image_path)
    
    welcome.image_selected.connect(on_image_selected)
    welcome.show()
    
    sys.exit(app.exec())
