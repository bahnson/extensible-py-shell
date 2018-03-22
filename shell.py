from shell.shell_factory import ShellFactory
import commands

context = {
	'shell_command_pkg': commands, 
	'shell_greeting': 'Welcome to simple python shell!',
	'shell_prompt': '> ',
	'my_own_context_var': 'TBD'
	# add further if you like .. 
}
ShellFactory.create_shell(context).cmdloop()
