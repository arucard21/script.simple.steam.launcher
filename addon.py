import subprocess
import shlex
import os

import xbmc
import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()
provided_path = addon.getSetting("SteamLocation")
if provided_path:
	tokenized_path = shlex.split(provided_path)
	if os.path.isfile(tokenized_path[0]):
		if os.access(tokenized_path[0], os.X_OK):
			# the user-provided location points to a file which can be executed, so now we can execute it
			launchProc = subprocess.Popen(tokenized_path)
		else:
			xbmcgui.Dialog().notitication(addon.getLocalizedString(32004), addon.getLocalizedString(32007), xbmcgui.NOTIFICATION_ERROR)
	else:
		xbmcgui.Dialog().notitication(addon.getLocalizedString(32004), addon.getLocalizedString(32006), xbmcgui.NOTIFICATION_ERROR)
else:
	xbmcgui.Dialog().notitication(addon.getLocalizedString(32004), addon.getLocalizedString(32005), xbmcgui.NOTIFICATION_ERROR)

if addon.getSetting("QuitKodi") == "true":
	# Quit Kodi
	xbmc.log(addon.getLocalizedString(32008))
	xbmc.executebuiltin("XBMC.Quit()")
