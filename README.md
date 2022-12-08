# batch-rename-py
A Python script to batch rename files in a directory.

## Installation and usage

You must have `Python3` installed.

Download via:

```
git clone https://github.com/ge-king/batch-rename-py.git
```

Run the program with:

```
python3 batch-rename-py.py
```

You'll then be asked for the path to the directory containing the files to rename. Enter the path.

Then you'll be asked for the filename you want to rename to. The files will be renamed to `filename-YYYY-MM-DD-HH-MM-SS`, where the date and time renamed to are the date and time of file creation.

The program will batch rename all files then close.

## To do

* Add options to change date format (remove hours, minutes and seconds etc.)
* Add more batch rename options

