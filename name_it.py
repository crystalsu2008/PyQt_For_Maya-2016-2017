'''
# It's loading code for maya, just put it in Maya Python script editor and run.
import sys
Dir = 'C:/Users/Administrator/Documents/DEV/PyQt_To_Maya-2016-2017'
if Dir not in sys.path:
    sys.path.append(Dir)

import name_it;reload(name_it)

name_it.delete()
name_it.create()
'''

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
    import PySide.QtGui      as qg
    from PyQt4.uic import loadUiType

from functools import partial

import PraLib.utils.names as names

dialog = None

#Path to the designer UI file
ui_filename = Dir+'/ui/name_it.ui'
form_class, base_class = loadUiType(ui_filename)

#------------------------------------------------------------------------------#

class NameIt(base_class, form_class):
    def __init__(self):
        # Call base_class's __init__()
        super(NameIt, self).__init__()
        # Call .ui file's setup function
        self.setupUi(self)

        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setModal(False)

        # As far as I know, this is not possible from QtDesigner.
        # The only way to access setVisible directly from QtDesigner is when
        # modifying connects you can find it as a slot.
        # The simplest way is just to set the visibility to false by hand code.
        self.lower_radio.setVisible(False)
        self.upper_radio.setVisible(False)

        reg_ex = qc.QRegExp("^(?!^_)[a-zA-Z_]+")
        text_validator = qg.QRegExpValidator(reg_ex, self.rename_le)
        self.rename_le.setValidator(text_validator)

        self.prefix_le.setValidator(text_validator)
        self.suffix_le.setValidator(text_validator)

        reg_ex = qc.QRegExp("[a-zA-Z_]+")
        text_validator = qg.QRegExpValidator(reg_ex, self.replace_le)
        self.replace_le.setValidator(text_validator)
        self.with_le.setValidator(text_validator)

        # connect modifiers
        #
        self.prefix_check.stateChanged.connect(self._updateExampleRename)
        self.suffix_check.stateChanged.connect(self._updateExampleRename)

        self.rename_mult_method_combo.currentIndexChanged.connect(self._toggleMultNamingMethod)
        self.rename_mult_method_combo.currentIndexChanged.connect(self._updateExampleRename)

        self.lower_radio.clicked.connect(self._updateExampleRename)
        self.upper_radio.clicked.connect(self._updateExampleRename)
        self.frame_pad_spin.valueChanged.connect(self._updateExampleRename)

        self.rename_le.textChanged.connect(self._updateExampleRename)
        self.prefix_le.textChanged.connect(self._updateExampleRename)
        self.suffix_le.textChanged.connect(self._updateExampleRename)

        self._updateExampleRename()

#------------------------------------------------------------------------------#


    #----------------------------------------------------------------------#

    def _toggleMultNamingMethod(self, index):
        self.lower_radio.setVisible(index)
        self.upper_radio.setVisible(index)
        self.frame_pad_lb.setVisible(not(index))
        self.frame_pad_spin.setVisible(not(index))

    #----------------------------------------------------------------------#

    def _getRenameSettings(self):
        text = str(self.rename_le.text()).strip()

        naming_method = bool(self.rename_mult_method_combo.currentIndex())

        padding = 0; upper = True
        if naming_method == 0:
            padding = self.frame_pad_spin.value()
        else:
            upper   = self.upper_radio.isChecked()

        prefix = ''; suffix = ''
        if self.prefix_check.isChecked():
            prefix = str(self.prefix_le.text()).strip()
        if self.suffix_check.isChecked():
            suffix = str(self.suffix_le.text()).strip()

        return text, prefix, suffix, padding, naming_method, upper

    #----------------------------------------------------------------------#

    def _updateExampleRename(self):
        example_text = ''

        text, prefix, suffix, padding, naming_method, upper = self._getRenameSettings()

        if not text:
            self.rename_lb.setText('<font color=#646464>e.g.</font>')
            return

        if prefix: example_text += '%s_' %prefix

        example_text += '%s_' %text

        if naming_method:
            if upper: example_text += 'A'
            else:     example_text += 'a'
        else:
            example_text += (padding * '0') + '1'

        if suffix: example_text += '_%s' %suffix

        self.rename_lb.setText('<font color=#646464>e.g. \'%s\'</font>' %example_text)

    #----------------------------------------------------------------------#






#------------------------------------------------------------------------------#

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
