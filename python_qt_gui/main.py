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

        self.model = keras.models.load_model(MODEL_PATH, custom_objects={'perceptual_loss': perceptual_loss})
        print("✅ Model loaded!")

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.setWindowTitle("Image Colorization - Processing")

        self.ui.selectinputimage.clicked.connect(self.open_image)
        self.ui.downloadimagebutton.clicked.connect(self.save_output)

        self.input_pixmap = None
        self.output_pixmap = None
        self.enhanced_pixmap = None
        self.input_image_path = None

    def load_and_process_image(self, file_name):
        """Load and process image directly without file dialog"""
        self.input_image_path = file_name
        
        # Call colorization function
        gray, color, enhanced = colorize_image(self.input_image_path, self.model)

        # Helper to convert PIL Image or numpy array to QPixmap
        def to_qpixmap(img):
            if hasattr(img, 'mode'):  # It's a PIL Image
                img = np.array(img)
            
            if len(img.shape) == 2:  # grayscale
                h, w = img.shape
                qimg = QImage(img.data, w, h, w, QImage.Format_Grayscale8)
            else:  # color image
                h, w, ch = img.shape
                if ch == 3:
                    qimg = QImage(img.data, w, h, w * ch, QImage.Format_RGB888)
                else:
                    qimg = QImage(img.data, w, h, w * ch, QImage.Format_RGB888)
            return QPixmap.fromImage(qimg)

        # Convert all images to QPixmap
        self.input_pixmap = to_qpixmap(gray)
        self.output_pixmap = to_qpixmap(color)
        self.enhanced_pixmap = to_qpixmap(enhanced)

        # Display all images
        w, h = self.ui.inputimagelabel.width(), self.ui.inputimagelabel.height()
        self.ui.inputimagelabel.setPixmap(
            self.input_pixmap.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        w2, h2 = self.ui.outputimagelabel.width(), self.ui.outputimagelabel.height()
        self.ui.outputimagelabel.setPixmap(
            self.output_pixmap.scaled(w2, h2, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        w3, h3 = self.ui.enhancedimage.width(), self.ui.enhancedimage.height()
        self.ui.enhancedimage.setPixmap(
            self.enhanced_pixmap.scaled(w3, h3, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if not file_name:
            return

        self.load_and_process_image(file_name)

    def save_output(self):
        if not self.output_pixmap:
            QMessageBox.warning(self, "No Output", "No output image to save!")
            return

        base_name = os.path.splitext(os.path.basename(self.input_image_path))[0]
        default_name = base_name + "_output_image.png"

        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save Output Image",
            default_name,
            "PNG (*.png);;JPG (*.jpg)"
        )

        if file_name:
            self.output_pixmap.save(file_name)
            QMessageBox.information(self, "Saved", f"Output saved to {file_name}")

# --- Main ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Show welcome window first
    welcome = WelcomeWindow()
    main_window = mywindow()
    
    # Connect welcome window to main window
    def on_image_selected(image_path):
        welcome.hide()
        main_window.show()
        main_window.load_and_process_image(image_path)
    
    welcome.image_selected.connect(on_image_selected)
    welcome.show()
    
    sys.exit(app.exec())
