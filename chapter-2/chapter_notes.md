sys.exit -> terminates the program, exit the interpreter. and aises SystemExit exceptions.

- sys.exit(1) - exit status code. general error unspecified issue
- sys.exit(0) - indicates success or a normal
- sys.exit(2) - used to indicate misuse or incorrect usage of program, ex: passed invalid argument
- sys.exit(127) - indicates requested command or programm is not found or (nonexistent command)
- sys.exit(128+) - specific meaning depending on the program or the context, some programs use specific codes to convey details about error


word = "SCHOOL"
word[:] -> "SCHOOL"
word[::-1] -> "LOOCHS"
word[2::-1] -> "LOO"
word[::-2] -> "LOC" # -2 stepper

words_list = ["Hello", "Python", "Learner"]
print(*words_list, sep="\n")
* -> unpacker operator, it prints each item separately
sep -> separator param

Profiling - analytical process that gathers statics on programs behavior. number and duration of function calls, memory it takes.
profile - measurment output

Sets are faster than lists when using `in` keyword. Sets use hashtable for lookup, downside is you cannot you cannot control order,