import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

## forms:
## https://www.youtube.com/watch?v=Lyph52xJe7U&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=5

class MainWindow(qtw.QWidget):
    def __init__(self):
        
        super().__init__()
        
        ## dodajanje naslova:
        self.setWindowTitle("Okno")
        
        ## postavitev:
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)
        
        ## Add stuff / widgets:
        label_1 = qtw.QLabel("To je kul vrstica!")
        label_1.setFont(qtg.QFont("Helvetica", 24))
        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)
        
        # Add rows to app:
        form_layout.addRow(label_1)
        form_layout.addRow("Ime", f_name)
        form_layout.addRow("Priimek", l_name)
        form_layout.addRow(qtw.QPushButton("Pritisni gumb!", clicked = lambda: press_it()))
              
        ## show the app:
        self.show()
        
        def press_it():
            label_1.setText(f'Stisnil si gumb, {f_name.text()} {l_name.text()}!')
        
app = qtw.QApplication([])
mw = MainWindow()


# zaženi aplikacijo
app.exec_()
