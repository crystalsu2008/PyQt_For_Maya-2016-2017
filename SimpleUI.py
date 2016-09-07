from pymel import versions
try: versions.v2017
except: versions.v2017 = 201700

if versions.current() >= versions.v2017:
    import PySide2.QtCore    as qc
    import PySide2.QtWidgets as qg
else:
    import PySide.QtCore     as qc
    import PySide.QtGui      as qg

import sys
Dir = 'C:/Users/Administrator/Documents/DEV/PyQt_To_Maya-2016-2017'
if Dir not in sys.path:
    sys.path.append(Dir)

import POTLib.utils.generic as generic;reload(generic)
from POTLib.utils.generic import loadUiType

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
        # Call Ui setup function
        self.setupUi(self)

        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setModal(False)

        #self.layout_1_bttn.clicked.connect(partial(self.stacked_layout.setCurrentIndex, 0))
        #self.layout_2_bttn.clicked.connect(partial(self.stacked_layout.setCurrentIndex, 1))
        #self.layout_3_bttn.clicked.connect(partial(self.stacked_layout.setCurrentIndex, 2))
        #self.layout_4_bttn.clicked.connect(partial(self.stacked_layout.setCurrentIndex, 3))


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
