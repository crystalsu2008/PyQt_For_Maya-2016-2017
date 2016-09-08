import sys

Dir = 'C:/Users/Administrator/Documents/DEV/PyQt_To_Maya-2016-2017'
PyQt4Dir = 'D:/Python27/Lib/site-packages'

from pymel import versions
try: versions.v2017
except: versions.v2017 = 201700
try: versions.v2015
except: versions.v2015 = 201500

if versions.current() >= versions.v2017:
    import PySide2.QtCore    as qc
    import PySide2.QtWidgets as qg
    if Dir not in sys.path:
        sys.path.append(Dir)
    import PraLib.utils.generic as generic;reload(generic)
    from PraLib.utils.generic import loadUiType
elif versions.current() >= versions.v2015:
    import PySide.QtCore     as qc
    import PySide.QtGui      as qg
    if Dir not in sys.path:
        sys.path.append(Dir)
    import PraLib.utils.generic as generic;reload(generic)
    from PraLib.utils.generic import loadUiType
else:
    if PyQt4Dir not in sys.path:
        sys.path.append(PyQt4Dir)
    import PyQt4.QtCore      as qc
    import PyQt4.QtGui       as qg
    from PyQt4.uic import loadUiType

from functools import partial

dialog = None

#Path to the designer UI file
ui_filename = Dir+'/ui/name_it.ui'
form_class, base_class = loadUiType(ui_filename)

#--------------------------------------------------------------------------------#

class NameIt(base_class, form_class):
    def __init__(self):
        # Call base_class's __init__()
        super(NameIt, self).__init__()
        # Call .ui file's setup function
        self.setupUi(self)

        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setModal(False)









#--------------------------------------------------------------------------------#

def create():
    global dialog
    if dialog is None:
        dialog = NameIt()
    dialog.show()

def delete():
    global dialog
    if dialog is None:
        return

    dialog.deleteLater()
    dialog = None
