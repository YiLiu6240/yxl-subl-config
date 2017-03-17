import os, sublime, sublime_plugin

class OpenCurrentFileInNewWindow(sublime_plugin.WindowCommand):
	def run(self):
		file_path = self.window.active_view().file_name()
		# print(file_path) # debug
		self.window.run_command("new_window")
		sublime.active_window().open_file(file_path)
