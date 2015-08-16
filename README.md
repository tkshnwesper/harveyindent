## HarveyIndent

Easily fix indentation issues (defaults made for Python).

## Syntax

If your file is named test.py

test.py
```
for i in range(0, 10):
print i
```
Note the incorrect indentation.

Run `$ python harveyindent.py test.py`

It creates a file `test.hi.py`.

test.hi.py
```
for i in range(0, 10):
    print i
```
