import sys

Dir = 'C:/Users/Administrator/Documents/GitHub/PyQt_For_Maya-2016-2017'
PyQt4Dir = 'C:/Python27/Lib/site-packages'

from pymel import versions
try: versions.v2017
except: versions.v2017 = 201700
try: versions.v2015
except: versions.v2015 = 201500

if versions.current() >= versions.v2017:
    import PySide2.QtCore    as qc
    import PySide2.QtWidgets as qw
    import PySide2.QtGui     as qg
    if Dir not in sys.path:
        sys.path.append(Dir)
    import PraLib.utils.generic as generic;reload(generic)
    from PraLib.utils.generic import loadUiType
elif versions.current() >= versions.v2015:
    import PySide.QtCore     as qc
    import PySide.QtGui      as qw
    import PySide.QtGui      as qg
    if Dir not in sys.path:
        sys.path.append(Dir)
    import PraLib.utils.generic as generic;reload(generic)
    from PraLib.utils.generic import loadUiType
else:
    if PyQt4Dir not in sys.path:
        sys.path.append(PyQt4Dir)
    import PyQt4.QtCore      as qc
    import PyQt4.QtGui       as qw
    import PyQt4.QtGui       as qg
    from PyQt4.uic import loadUiType

from functools import partial

dialog = None

#Path to the designer UI file
ui_filename = Dir+'/ui/SimpleUI.ui'
form_class, base_class = loadUiType(ui_filename)

#--------------------------------------------------------------------------------#

#Interface class
class SimpleUI(base_class, form_class):
    def __init__(self):
        # Call base_class's __init__()
        super(SimpleUI, self).__init__()
        # Call .ui file's setup function
        self.setupUi(self)

        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setModal(False)

        #self.layout_1_bttn.clicked.connect(partial(self.stacked_layout.setCurrentIndex, 0))
        #self.layout_2_bttn.clicked.connect(partial(self.stacked_layout.setCurrentIndex, 1))
        #self.layout_3_bttn.clicked.connect(partial(self.stacked_layout.setCurrentIndex, 2))
        #self.layout_4_bttn.clicked.connect(partial(self.stacked_layout.setCurrentIndex, 3))

        #self.middle_frame.layout().setAlignment(qc.Qt.AlignBottom)

        reg_ex = qc.QRegExp("[a-zA-Z_]+")
        text_validator = qg.QRegExpValidator(reg_ex, self.example_le)
        self.example_le.setValidator(text_validator)

        self.example_bttn.clicked.connect(self.printText)
        self.example_check.stateChanged.connect(self.example_bttn.setDisabled)

        self.button_grp_1 = qw.QButtonGroup(self)
        self.button_grp_2 = qw.QButtonGroup(self)

        self.button_grp_1.addButton(self.a_radio)
        self.button_grp_1.addButton(self.b_radio)

        self.button_grp_2.addButton(self.c_radio)
        self.button_grp_2.addButton(self.d_radio)

        self.button_grp_1.buttonClicked.connect(self.addToTextEdit)

    def printText(self):
        print self.example_te.toPlainText()

    def addToTextEdit(self, button):
        button_text = button.text()
        self.example_te.setText(self.example_te.toPlainText() + button_text)

#--------------------------------------------------------------------------------#

def create():
    global dialog
    if dialog is None:
        dialog = SimpleUI()
    dialog.show()

def delete():
    global dialog
    if dialog is None:
        return

    dialog.deleteLater()
    dialog = None
