FileComment
=========

## Overview
FileComment is a tool to make comments on files and display them. 
It will be very useful if you sometimes forgot what's the file is, especially the file is very large.
The comment information is storied in file .FileComment.json of current path, so when you move the folder, this information will also be moved to the new place.

## Usage
```
usage: fcomment [-h] [-f] [-a] [-m MESSAGE] [filename [filename ...]]

positional arguments:
  filename

optional arguments:
  -h, --help            show this help message and exit
  -f, --full            Show all comments of a file, will only show the latest
                        by default
  -a, --add             Add new comments to file
  -m MESSAGE, --message MESSAGE
                        Working with -a, specify the comment message

```
### Add comment on a file
```
fcomment -a FILENAME
```
This command will open the default editor to get the comments and save it.
Or you can also specify the command text by -m switch:
```
fcomment -a FILENAME -m 'Comment message'
```
### Show the comment of file
Following command will show the comment of files:
```
$ fcomment *
| File Name   | Comment                      | Added Time          |
|-------------+------------------------------+---------------------|
| file1       | 100000 user data             | 2014-04-01 15:25:15 |
| path1       | DB backup after create index | 2014-04-01 15:24:31 |
```
You can also viery all the historical comments of a file using -f switch
```
$ fcomment -f file1
| File Name   | Comment          | Added Time          |
|-------------+------------------+---------------------|
| file1       | Comment update   | 2014-04-01 15:30:19 |
| file1       | 100000 user data | 2014-04-01 15:25:15 |
```
