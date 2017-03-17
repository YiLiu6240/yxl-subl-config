import os, platform, sublime, sublime_plugin

def homeAddress():
	if platform.system() == 'Windows':
		home =  os.environ['USERPROFILE'] # for Windows, use %USERPROFILE%, 'C:/Users/XXX' typically
	else:
		home = os.environ['HOME'] # for OS other than Windows, use $HOME
	return (home)

class OpenWikiIndex(sublime_plugin.WindowCommand):
	def run(self):
		textIndexAddress = '%s/OneDrive/inbox_wiki/index.md' % homeAddress()
		sublime.active_window().open_file(textIndexAddress)
