class ShellCommand(object):
	def __init__(self, args, context):
		self.args = args.split(" ")
		self.context = context
	def execute(self):
		self.context = context
		pass
