from __future__ import print_function # for using print in lambda
import pkgutil
import imp
import inspect
import importlib
import string

from cmd import Cmd
from types import MethodType
from string import Template

class ShellFactory(object):
	# template for functions to be added to the Shell class
	do_cmd_template = Template(
		"def $func_name(self, args): 				\n"
		"	$doc_string								\n"
		"	from $mod_name import $class_name		\n"
		"	cmd = $class_name(args,self.context)	\n"
		"	cmd.execute()		 					\n"
	)
	dummy_module = imp.new_module('myfunctions')

	# For each command-class module in package pkg_with_commands an instance method "do_<command>" is added to the python's Cmd class, 
	# with "<command>" being the name of the command-class module. E.g., for module "commands.shellcommands.my_cmd" a method "do_my_cmd" 
	# is added to the Cmd class and a command "my_cmd" becomes available in the shell. An instance of the Cmd class is returned.  
	@staticmethod
	def create_shell(shell_context):
		help_func = lambda _: print("\n\thelp [command-name]\n\tdisplays help for specific commands or an overview of available commands (if command-name is ommitted)\n")
		setattr(Cmd, 'help_help', help_func)
		setattr(Cmd, 'intro', shell_context['shell_greeting'])
		setattr(Cmd, 'prompt', shell_context['shell_prompt'])
		
		for importer, pkgname, ispkg in pkgutil.walk_packages(shell_context['shell_command_pkg'].__path__, shell_context['shell_command_pkg'].__name__+"."):
			ismodule = not ispkg
			if ismodule: ShellFactory.add_to_shell(pkgname)

		shell = Cmd()
		shell.context = shell_context
		return shell
	
	@staticmethod
	def add_to_shell(modname): 
		
		modname_short = modname.split(".")[modname.count(".")]

		mod = importlib.import_module(modname)

		for class_info in inspect.getmembers(mod, inspect.isclass):
			for base_class_info in class_info[1].__bases__:
				if base_class_info.__module__ == 'shell.shell_command':
					className = class_info[1].__name__
					doc_string = '"""' + getattr(mod, className).__doc__ + '"""'
					func_name = 'do_' + modname_short
					func_code = ShellFactory.do_cmd_template.safe_substitute(func_name=func_name, mod_name=modname,class_name=className, doc_string=doc_string)
					
					exec(func_code,ShellFactory.dummy_module.__dict__)
					
					setattr(Cmd, func_name, getattr(ShellFactory.dummy_module,func_name))		

