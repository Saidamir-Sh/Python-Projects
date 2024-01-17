Use ```pylint``` for code analysing (coding standards code smells, type erros) PEP 8

```pip install pylint```

```pylint my_file.py ```

Outputs something like this:
```
my_file.py:23:0: C0301: Line too long (110/100) (line-too-long)
my_file.py:24:0: C0301: Line too long (109/100) (line-too-long)
my_file.py:31:0: C0301: Line too long (139/100) (line-too-long)
my_file.py:42:0: C0303: Trailing whitespace (trailing-whitespace)
my_file.py:43:0: C0301: Line too long (166/100) (line-too-long)
my_file.py:44:51: C0303: Trailing whitespace (trailing-whitespace)
my_file.py:45:0: C0303: Trailing whitespace (trailing-whitespace)
my_file.py:54:0: C0304: Final newline missing (missing-final-newline)
my_file.py:31:10: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
```