# reference:
# http://www.sublimetext.com/forum/viewtopic.php?f=6&p=45349
# http://www.metaltoad.com/blog/writing-simple-sublime-text-plugin
import sublime, sublime_plugin

def getDualChar(character, extra_space):
	"""
	get the counterpart of "character"
	"""
	LHS_char = character

	## define RHS_char
	if character == "(":
		RHS_char = ")"
	elif character == "{":
		RHS_char = "}"
	elif character == "<":
		RHS_char = ">"
	elif character == "[":
		RHS_char = "]"
	else:
		RHS_char = character

	## decides if needs extra spaces
	if (extra_space):
		LHS_char = LHS_char + " "
		RHS_char = " " + RHS_char

	return [LHS_char, RHS_char]

class InsertSurroundChars(sublime_plugin.TextCommand):
	"""
	when activated, insert the character and its counterpart, then move back cursor by one char
	"""
	def run(self, edit, character, extra_space):
		[LHS_char, RHS_char] = getDualChar(character, extra_space)
		self.view.run_command("insert", {"characters": LHS_char+RHS_char})
		self.view.run_command("move", {"by": "characters", "forward": False})
		if extra_space:
			self.view.run_command("move", {"by": "characters", "forward": False})

class InsertSurroundCharsSelection(sublime_plugin.TextCommand):
	"""
	insert when has selection
	"""
	def run(self, edit, character, extra_space):
		[LHS_char, RHS_char] = getDualChar(character, extra_space)
		for region in self.view.sel():
			selection = self.view.substr(region)
			self.view.replace(edit, region, LHS_char+selection+RHS_char)

class InsertSingleChar(sublime_plugin.TextCommand):
	"""
	Only insert one character, overwrite subl keymapping
	"""
	def run(self, edit, character):
		self.view.run_command("insert", {"characters": character})

class InsertSurroundCarriage(sublime_plugin.TextCommand):
	"""
	Insert two line breaks "\\n",
	effect: expand one empty line into three empty lines, with the cursor being center
	"""
	def run(self, edit):
		self.view.run_command("insert", {"characters": "\n\n"})
		self.view.run_command("move", {"by": "characters", "forward": False})

################################
# def getDualChar(character, symmetrical):
# 	"""
# 	get the counterpart of "character"
# 	"""
# 	LHS_char = character
# 	insertSpace = 0
# 	if symmetrical:
# 		if character == "(":
# 			RHS_char = ")"
# 		elif character == ")":
# 			LHS_char = "( "
# 			RHS_char = " )"
# 			insertSpace = 1
# 		elif character == "{":
# 			RHS_char = "}"
# 		elif character == "}":
# 			LHS_char = "{ "
# 			RHS_char = " }"
# 			insertSpace = 1
# 		elif character == "<":
# 			RHS_char = ">"
# 		elif character == ">":
# 			LHS_char = "< "
# 			RHS_char = " >"
# 			insertSpace = 1
# 		elif character == "[":
# 			RHS_char = "]"
# 		elif character == "]":
# 			LHS_char = "[ "
# 			RHS_char = " ]"
# 			insertSpace = 1
# 		else:
# 			RHS_char = character
# 	else:
# 		RHS_char = character

# 	insertSpace = bool(insertSpace)

# 	return [LHS_char, RHS_char, insertSpace]

# class InsertSurroundChars(sublime_plugin.TextCommand):
# 	"""
# 	when activated, insert the character and its counterpart, then move back cursor by one char
# 	"""
# 	def run(self, edit, character, symmetrical):

# 		[LHS_char, RHS_char, insertSpace] = getDualChar(character, symmetrical)
# 		# dual_character = getDualChar(character, symmetrical)

# 		# self.view.insert(edit, self.view.sel()[0].begin(), character+dual_character)
# 		self.view.run_command("insert", {"characters": LHS_char+RHS_char})
# 		self.view.run_command("move", {"by": "characters", "forward": False})
# 		if insertSpace:
# 			self.view.run_command("move", {"by": "characters", "forward": False})

# class InsertSurroundCharsSelection(sublime_plugin.TextCommand):
# 	"""
# 	insert when has selection
# 	"""
# 	def run(self, edit, character, symmetrical):

# 		[LHS_char, RHS_char, insertSpace] = getDualChar(character, symmetrical)
# 		# dual_character = getDualChar(character, symmetrical)

# 		for region in self.view.sel():
# 			selection = self.view.substr(region)
# 			self.view.replace(edit, region, LHS_char+selection+RHS_char)

# class InsertSurroundCarriage(sublime_plugin.TextCommand):
# 	"""
# 	Insert two line breaks "\\n",
# 	effect: expand one empty line into three empty lines, with the cursor being center
# 	"""
# 	def run(self, edit):

# 		self.view.run_command("insert", {"characters": "\n\n"})
# 		self.view.run_command("move", {"by": "characters", "forward": False})
