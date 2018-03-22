# extensible-py-shell

Extensible python-based shell/CLI with built-in tab completion, command backlog, and help function for your custom commands.

## Getting Started

Download repository files and run `python shell.py`. Start a little dialog to get a feeling for the behavior of the shell:

<pre><code>
Welcome to simple python shell!
> [hit TAB]
command_one    command_three  command_two    create_command help
> help

Documented commands (type help <topic>):
========================================
command_one  command_three  command_two  create_command  help

> com[hit TAB]
command_one    command_two
> command_one
executing command_one
> help create_command

        creates a new shell command with the passed name. command names should be lowercase words, separated by underscrores.

> create_command command_three
creating command class "CommandThree" in module ".../extensible-py-shell/commands/command_three.py"
</code></pre>

Extending the shell is straightforward: provide a new command class in a corresponding module in directory `extensible-py-shell/commands`, add the command description in the docstring of the constructor, and implement the `execute` method. There's a simple  naming rule to be followed, though: use lowercase words seperated by underscores for the module name, use the same words in CamelCase for the command class. See the existing commands for reference. Then restart the shell and your command should be integrated

### Prerequisites

The programm was developed and tested using Python 3.6.2. I'd expect it to run with Python 2.7 or 3.3. However, if you have trouble running it with your python version, feel free to contact me or post a comment.

## Author

[**Christopher Bahn**](mailto:bahnson@hotmail.de)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Hat tip to Python's `Cmd` class