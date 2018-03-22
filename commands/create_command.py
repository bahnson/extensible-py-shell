from shell.shell_command import ShellCommand
from string import Template
import re
import os

class CreateCommand(ShellCommand):
	"""
	creates a new shell command with the passed name. command names should be lowercase words, separated by underscrores. 
	"""

	def __init__(self, args, context):
		ShellCommand.__init__(self, args, context)
		
		self.cmd_file_template = Template(
			"from shell.shell_command import ShellCommand		\n"
			"													\n"
			"class $command_class_name(ShellCommand):			\n"
			"	\"\"\"											\n"
			"	help entry for $command_name.					\n"
			"	\"\"\"											\n"
			"	def __init__(self, args, context):				\n"
			"		ShellCommand.__init__(self, args, context)	\n"
			"													\n"
			"	def execute(self):								\n"
			"		pass										\n"
		)

	def execute(self):
		command_name = self.args[0].lower()
		module_file_name = os.path.dirname(__file__) + os.sep + command_name + '.py'
		command_class_name = re.sub(r'(?:^|_)([a-z])', lambda match: match.group(1).upper(), command_name)
		
		print('creating command class "' + command_class_name + '" in module "' + module_file_name + '"')

		with open(module_file_name, 'w') as module_file:
			module_file.write(self.cmd_file_template.safe_substitute(command_name=command_name, command_class_name=command_class_name))