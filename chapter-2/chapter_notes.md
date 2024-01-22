sys.exit -> terminates the program, exit the interpreter. and aises SystemExit exceptions.

- sys.exit(1) - exit status code. general error unspecified issue
- sys.exit(0) - indicates success or a normal
- sys.exit(2) - used to indicate misuse or incorrect usage of program, ex: passed invalid argument
- sys.exit(127) - indicates requested command or programm is not found or (nonexistent command)
- sys.exit(128+) - specific meaning depending on the program or the context, some programs use specific codes to convey details about error