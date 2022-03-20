import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

## simple app:
## https://www.youtube.com/watch?v=rZcdhles6vQ&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=1

class MainWindow(qtw.QWidget):
    def __init__(self):
        
        super().__init__()
        
        ## dodajanje naslova:
        self.setWindowTitle("Okno")
        
        ## postavitev (vertical layout):
        self.setLayout(qtw.QVBoxLayout())
        
        ## create label:
        my_label = qtw.QLabel("Živjo, kako ti je ime?")
        # spreminjanje velikosti fontov:
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)
        
        ## create an entry box:
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("vpiši svoje ime...")
        self.layout().addWidget(my_entry)
        
        ## create a button:
        my_button = qtw.QPushButton("Press me!", clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        ## show the app:
        self.show()
        
        def press_it():
            # Add name to label:
            my_label.setText(f'Hello {my_entry.text()}!')
            # Clear the entry box
            my_entry.setText("")
        
app = qtw.QApplication([])
mw = MainWindow()


# zaženi aplikacijo
app.exec_()