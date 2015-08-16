## HarveyIndent

Easily fix indentation issues (defaults made for Python). This script is used as a rescue method in case you start getting indentation errors and you need a quick fix.

## Syntax


#### Basic usage

Suppose your file is named test.py


test.py
```
for i in range(0, 10):
print i
```
Note the incorrect indentation.

Run:
`$ python harveyindent.py test.py`


It creates a file named `test.hi.py`.


test.hi.py
```
for i in range(0, 10):
    print i
```

Now running `$ python harveyindent.py test.py` on this input
```
for i in range(0, 10):
print i #~
if i == 9:
print 'done'
```

Gives:
```
for i in range(0, 10):
    print i #~
if i == 9:
    print 'done'
```
Notice the `#~` which informs the script to decrease the indent.


#### Defining the indent

You can redefine the default indent by giving an option `-s` for spaces and `-t` for tabs followed by the number of spaces or tabs respectively.

For example,

`$ python harveyindent.py test.py -s 4`

will use 4 spaces as an indent.

`$ python harveyindent.py test.py -t 2`

This will use two tabs as an indent.


#### Changing the default unindent symbol

This can be done by giving an option `-u` followed by the symbol in quotes.

For example,

`$ python harveyindent.py test.py -u "#end"`


#### Coding conventions

While programming, make it a point to add the unindent character wherever necessary. So, if indentation errors start occurring you can just run this script to fix them.

```
for i in range(0, 10):
    print i
#end

if i == 9:
    print 'done'
#end
```
