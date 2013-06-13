# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HelloPluginDialog
                                 A QGIS plugin
 A plugin to greet the user
                             -------------------
        begin                : 2013-06-13
        copyright            : (C) 2013 by Ismail Sunni
        email                : ismailsunni@yahoo.co.id
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_helloplugin import Ui_HelloPlugin
# create the dialog for zoom to point


class HelloPluginDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_HelloPlugin()
        self.ui.setupUi(self)
