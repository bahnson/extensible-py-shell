from shell.shell_command import ShellCommand

class CommandTwo(ShellCommand):
	"""
	help entry for command_two.
	"""
	def __init__(self, args, context):
		ShellCommand.__init__(self, args, context)

	def execute(self):
		print("executing command_two")
		if self.context['my_own_context_var'] != 'command_one already executed':
			print("command_one has not been executed, yet")
		else:
			print("thats's it. one little step after another..")