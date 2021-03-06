"""
Text Editor – Notepad style application that can open, edit, and save text documents.
Work in progress
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self,parent)
        
        self.filename = ''
        self.initUI()

    def initToolbar(self):
        
        self.newAction = QtWidgets.QAction("New",self)
        self.newAction.setStatusTip("Create a new document from scratch.")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)
        
        self.openAction = QtWidgets.QAction("Open file",self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)
        
        self.saveAction = QtWidgets.QAction("Save",self)
        self.saveAction.setStatusTip("Save document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)
                
        self.toolbar = self.addToolBar("Options")
        
        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)

        self.toolbar.addSeparator()
        # Makes the next toolbar appear underneath this one
        self.addToolBarBreak()

    def initFormatbar(self):
        self.formatbar = self.addToolBar("Format")

    def initMenubar(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)

    def initUI(self):

        self.text = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text)
    
        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()
    
        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()

        # x and y coordinates on the screen, width, height
        self.setGeometry(100,100,720,480)

        self.setWindowTitle("Text editor")

    def new(self):

        spawn = main(self)
        spawn.show()

    def open(self):
    
        # Get filename and show only .writer files
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".","(*.writer)")
    
        if self.filename:
            with open(self.filename,"rt") as file:
                self.text.setText(file.read())
    
    def save(self):
    
        # Only open dialog if there is no filename yet
        if not self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
    
        # Append extension if not there yet
        if not self.filename.endswith(".writer"):
            self.filename += ".writer"
    
        # We just store the contents of the text file along with the
        # format in html, which Qt does in a very nice way for us
        with open(self.filename,"wt") as file:
            file.write(self.text.toHtml())
                
def main():

    app = QtWidgets.QApplication(sys.argv)

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
