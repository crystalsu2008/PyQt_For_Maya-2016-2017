# PyQt_For_Maya-2016-2017
&emsp; This is my practice for learning Mike Cole's tutorial, the ["Advanced PyQt for Maya"](https://app.pluralsight.com/library/courses/advanced-pyqt-maya-2122/table-of-contents). The tutorial used Maya 2015 and ```PyQt4```. But I worked under Maya 2016 and ```PySide```, I even want to use Maya 2017. The Maya 2017 came with a big change, PyQt4 and PySide no longer works with this version of Maya. Maya now uses ```Qt5``` and ```PySide2```. And I also try to use the Qt-Designer to build my UI.

&emsp; So in this practices, I'm going to try to convert the original scripts to some compatible scripts that can be compatible with ```PyQt4```, ```PySide``` and ```PySide2```. And I will replace the hand-craft UI code with the .ui file that generated by Qt-Designer. I hope that it can be performed on any version of Maya with no issues.

&emsp; Here is a very useful guide to help convert Maya PySide script to PySide2 script, [Dealing with Maya 2017 and PySide2](https://fredrikaverpil.github.io/2016/07/25/dealing-with-maya-2017-and-pyside2/). It's form Fredrik's Blog, thanks a lot.

### PyQt, PySide in Maya 2014 and before
&emsp; I often use three versions of Maya. Those are Maya 2014, Maya 2016 and Maya 2017. The PySide, PyQt, and shiboken modules are not distributed with Maya 2014 and before versions, and must be installed separately.

&emsp; I work on 64-bit Windows 10 and [Python 2.7.12(64-bit)](https://www.python.org/downloads/release/python-2712/). So I just need to download and install the Windows 64-bit Installer, [PyQt4-4.11.4-gpl-Py2.7-Qt4.8.7-x64.exe](https://riverbankcomputing.com/software/pyqt/download) , no need to build and install SIP or build PyQt4.

>&emsp; I also work with Maya 2013, but Maya 2013 uses [Python 2.6](https://www.python.org/download/releases/2.6.6/)(Since Maya 2014 they use Python 2.7). So I installed the Python 2.6 and [PyQt4-4.10-Py2.6](https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.10/). When I try to import PyQt4.QtCore and PyQt4.QtGui in the Maya Script Editor, I get the following error:
```python
import PyQt4.QtCore
# Error: ImportError: file <maya console> line 1: DLL load failed: The specified procedure could not be found. #
```
But it can be imported in the Python command line or IDLE with no problem. I don't know why it doesn't work on Maya, maybe I should build and install SIP and PyQt4. If anyone knows how to fix it, please tell me.
