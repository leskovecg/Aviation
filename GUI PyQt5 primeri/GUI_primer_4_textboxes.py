import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

## text box:
## https://www.youtube.com/watch?v=Fl92v4PpbzE&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=4

class MainWindow(qtw.QWidget):
    def __init__(self):
        
        super().__init__()
        
        ## dodajanje naslova:
        self.setWindowTitle("Okno")
        
        ## postavitev (vertical layout):
        self.setLayout(qtw.QVBoxLayout())
        
        ## create label:
        my_label = qtw.QLabel("Napiši kaj spodaj", self)
        # spreminjanje velikosti fontov:
        my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)
        
        ## create an text box:
        my_text = qtw.QTextEdit(self,
            #plainText = "To je pravi text!",
            #html = "<h1>Velik naslov</h1>",                     
            acceptRichText = False,
            lineWrapMode = qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth = 50,
            placeholderText = "Hello world!",
            readOnly = False,            
            )
        
        # put combobox on the screen
        self.layout().addWidget(my_text)
        
        ## create a button:
        my_button = qtw.QPushButton("Press me!", clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        ## show the app:
        self.show()
        
        def press_it():
            # Add name to label:
            my_label.setText(f'Napisal si {my_text.toPlainText()}!')
            my_text.setPlainText("Stisnil si gumb!")
            

app = qtw.QApplication([])
mw = MainWindow()


# zaženi aplikacijo
app.exec_()
