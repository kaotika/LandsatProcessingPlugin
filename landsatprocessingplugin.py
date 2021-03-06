# -*- coding: utf-8 -*-
"""
/***************************************************************************
 landsatProcessingPlugin
                                 A QGIS plugin
 Provides several processing steps on Landsat data. Landsat5 to Landsat7 conversion, DNs to radiance and reflectance conversion, TIR to temperature conversion, Indice calculation(NDVI, SAVI, NDWI, NDSI, tasseled cap indices)
                              -------------------
        begin                : 2013-02-14
        copyright            : (C) 2013 by Matthias Ludwig - Datalyze Solutions
        email                : development@datalyze-solutions.com
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from landsatprocessingplugindialog import landsatProcessingPluginDialog

class landsatProcessingPlugin:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/landsatprocessingplugin"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]

        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/landsatprocessingplugin_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = landsatProcessingPluginDialog()               

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/landsatprocessingplugin/icon.png"),
            u"Landsat Processing Plugin", self.iface.mainWindow())

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Landsat Processing Plugin", self.action)
        
        self.action.triggered.connect(self.run)
        self.dlg.filestuff.sendFilename.connect(self.test)
        self.dlg.filestuff.doNothingSignal.connect(self.test2)
        
        #print self.dlg.filestuff
        
        #QObject.connect(self.dlg, SIGNAL("xyCoordinates(const QString &)"), self.test)
        
        # start real work
        #self.getFile()

    def test(self, text):
	print text
	
    def test2(self):
	print "eigenes signal emitiert"
	
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Landsat Processing Plugin", self.action)
        self.iface.removeToolBarIcon(self.action)
        
    def run(self):
	self.dlg.show()
	#self.dlg.test()

class landsatMetadata():
    def __init__(self, filepath, viewWidget):
	self.filepath = filepath
	self.viewWidget = viewWidget
	self.metadata = None
	self.lastChangedDate = os.filepathDate
	
    def isUpToDate(self):
      if self.lastChangedDate != os.filepathDate:
	self.parseMetadata()
	self.lastChangedDate
	self.lastChangedDate = os.filepathDate
    	
    def parseMetadata(self):
      self.metadata = parserErgebnis
      
    def updateView(self):
      self.viewWidget.update(self.metadata)