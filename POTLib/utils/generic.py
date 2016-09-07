from pymel import versions
try: versions.v2017
except: versions.v2017 = 201700

if versions.current() >= versions.v2017:
    import PySide2.QtCore    as qc
    import PySide2.QtWidgets as qg
    import pyside2uic as pyuic
else:
    import PySide.QtCore as qc
    import PySide.QtGui  as qg
    import pysideuic as pyuic

import xml.etree.ElementTree as xml
from cStringIO import StringIO



#--------------------------------------------------------------------------------#

def loadUiType(uiFile):
    """
    PySide2 lacks the "loadUiType" command, so we have to convert the ui file
    to py code in-memory first and then execute it in a special frame to
    retrieve the form_class.
    """
    parsed = xml.parse(uiFile)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text

    with open(uiFile, 'r') as f:
        o = StringIO()
        frame = {}

        pyuic.compileUi(f, o, indent=0)
        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec pyc in frame

        # Fetch the base_class and form class based on their type in the xml
        # from designer
        form_class = frame['Ui_%s'%form_class]
        base_class = eval('qg.%s'%widget_class)

    return form_class, base_class
