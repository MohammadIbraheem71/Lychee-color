Here's how to run the Image Colorization project:

STEP 1: OPEN COMMAND PROMPT OR TERMINAL

Press Windows key + R, type cmd, and press Enter

STEP 2: NAVIGATE TO PROJECT FOLDER

Type this command and press Enter:
cd C:\Users\Muhamamad Zain\Desktop\Lychee-color

STEP 3: CREATE VIRTUAL ENVIRONMENT (OPTIONAL BUT RECOMMENDED)

Type this command and press Enter:
python -m venv venv

STEP 4: ACTIVATE VIRTUAL ENVIRONMENT

For Windows, type this and press Enter:
venv\Scripts\activate

You should see (venv) appear at the start of your command line

STEP 5: INSTALL REQUIRED PACKAGES

Type this command and press Enter:
pip install -r requirements.txt

This will install TensorFlow, PySide6, OpenCV, and all other dependencies. It may take a few minutes.

STEP 6: NAVIGATE TO GUI FOLDER

Type this command and press Enter:
cd python_qt_gui

STEP 7: RUN THE APPLICATION

Type this command and press Enter:
python main.py

STEP 8: USE THE APPLICATION

The welcome window will open with a logo. Click the "Select Image to Colorize" button. Choose a grayscale image from your computer. The processing window will open showing three images side by side: input grayscale, basic colorized, and enhanced colorized. Click "SELECT IMAGE" to process another image. Click "SAVE OUTPUT" to save the colorized result.

TROUBLESHOOTING:

If you get "Model not found" error, make sure the file colorization_model_faces.keras exists in the pseudocolor folder.

If you get "Module not found" errors, make sure you ran pip install -r requirements.txt successfully.

If the logo doesn't show in welcome window, that's okay, the functionality will still work.

To close the application, just close the window or press Ctrl+C in the command prompt.

To run again later, just navigate to python_qt_gui folder and run python main.py again. You don't need to reinstall packages.