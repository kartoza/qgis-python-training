# This is not actually needed - the python console in QGIS
# does it automagically for you...
from qgis.utils import iface
# Get the main application window
window = iface.mainWindow()
# Size it
window.resize(400, 400)



for child in window.children():
    print child.objectName()


# Find a toolbar icon and disable it
from PyQt4.QtGui import QAction
window.findChild(QAction, 'mActionSaveProject')
action = window.findChild(QAction, 'mActionSaveProject')
action.setDisabled(True)
# Look on the toolbar / file menu, it will be grayed out
# Now get it back to normal....
action.setDisabled(False)
# or
action.setEnabled(True)



