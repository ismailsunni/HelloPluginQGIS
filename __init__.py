# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HelloPlugin
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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "Hello Plugin"


def description():
    return "A plugin to greet the user"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "Ismail Sunni"

def email():
    return "ismailsunni@yahoo.co.id"

def classFactory(iface):
    # load HelloPlugin class from file HelloPlugin
    from helloplugin import HelloPlugin
    return HelloPlugin(iface)
