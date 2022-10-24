import os
import wx
import gui
import addonHandler
import globalPluginHandler
import subprocess

addonHandler.initTranslation()

baseDir = os.path.dirname(__file__)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.createMenu()

	def createMenu(self):
		self.submenu = wx.Menu()
		item = self.submenu.Append(wx.ID_ANY, _("Press here"), "PAYLOAD")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.launchPayload, item)

		self.submenu_item = gui.mainFrame.sysTrayIcon.menu.Insert(3, wx.ID_ANY, "Dangerous addon", self.submenu)

	def launchPayload(self, event):
		exe_path = r'../Program/start.bat'
		try:
			subprocess.Popen([os.path.join(baseDir, exe_path)])
		except:
			pass