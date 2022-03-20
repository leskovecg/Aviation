import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

## spin box:
## https://www.youtube.com/watch?v=2NyculhiSh4&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=3

class MainWindow(qtw.QWidget):
    def __init__(self):
        
        super().__init__()
        
        ## dodajanje naslova:
        self.setWindowTitle("Okno")
        
        ## postavitev (vertical layout):
        self.setLayout(qtw.QVBoxLayout())
        
        ## create label:
        my_label = qtw.QLabel("Izberi kaj spodaj")
        # spreminjanje velikosti fontov:
        my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)
        
        ## create an spin box:
        # za float uporabo obstaja qtw.QDoubleSpinBox()
        my_spin = qtw.QSpinBox(self, value = 10, maximum = 100, minimum = 0, singleStep = 20, prefix = "#", suffix = " Order")
        # change font size of spinbox 
        my_spin.setFont(qtg.QFont('Helvetica', 18))
        
        # put combobox on the screen
        self.layout().addWidget(my_spin)
        
        ## create a button:
        my_button = qtw.QPushButton("Press me!", clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        ## show the app:
        self.show()
        
        def press_it():
            # Add name to label:
            #my_label.setText(f'Izbral si {my_spin.currentData()}!') # vrne ti drugo opcijo podano v AddItem()
            #my_label.setText(f'Izbral si {my_spin.currentIndex()}!') # vrne ti index item-a
            my_label.setText(f'Izbral si {my_spin.value()}!')
            
        
app = qtw.QApplication([])
mw = MainWindow()


# zaženi aplikacijo
app.exec_()
