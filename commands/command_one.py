from shell.shell_command import ShellCommand

class CommandOne(ShellCommand):
	"""
	help entry for command_one.
	"""
	def __init__(self, args, context):
		ShellCommand.__init__(self, args, context)

	def execute(self):
		print("executing command_one")
		self.context['my_own_context_var'] = 'command_one already executed'
		