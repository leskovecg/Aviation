import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

## combo box:
## https://www.youtube.com/watch?v=O58FGYYBV7U&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=2


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
        
        ## create an combo box:
        my_combo = qtw.QComboBox(self, editable = True, insertPolicy = qtw.QComboBox.InsertAtTop)
        # add items to the combo box 
        my_combo.addItem("Pepperoni", "Something")
        my_combo.addItem("Cheese", 2)
        my_combo.addItem("Mushroom", qtw.QWidget)
        my_combo.addItem("Peppers")
        my_combo.addItems(["one", "two", "three"])
        my_combo.insertItem(2, "Third thing!")
        my_combo.insertItems(3, ["Fourth thing!", "Fifth thong!"])
        # put combobox on the screen
        self.layout().addWidget(my_combo)
        
        ## create a button:
        my_button = qtw.QPushButton("Press me!", clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        ## show the app:
        self.show()
        
        def press_it():
            # Add name to label:
            #my_label.setText(f'Izbral si {my_combo.currentData()}!') # vrne ti drugo opcijo podano v AddItem()
            #my_label.setText(f'Izbral si {my_combo.currentIndex()}!') # vrne ti index item-a
            my_label.setText(f'Izbral si {my_combo.currentText()}!')
            
        
app = qtw.QApplication([])
mw = MainWindow()


# zaženi aplikacijo
app.exec_()