## Introduction to the Command Line

This document outlines basic usage of the command line. For Linux and Mac users, these commands should work in **Terminal**. For Windows users, these should work in **Git Bash**.

### What is the command line?

The Command Line Interface (CLI) is a way of interacting with your computer using text-based commands. This is different from the way most people interact with their computers, using their mouse and a Graphical User Interface (GUI).

### Why should I use it?

Once you become comfortable with the basics, it can be a more powerful way to use your computer. You're able to do many things more quickly and programatically.

### General format for commands

`<command> -<options> <arguments>`
* `<command>` is the action we want the computer to take
* `<options>` (or "flags") modify the behavior of the command
* `<arguments>` are the things we want the command to act on

For Linux and Mac users, you can get view the **man**ual for a command by typing `man <command>`. For Windows users, you can view the help page by typing `<command> --help`.

### Tips

* If there are spaces in file or directory names, use a "\" to "escape" the space characters, or just put the entire file path in quotes.
* After typing the first few letters of a file or directory name, you can hit Tab to auto-complete the name. (This often auto-escapes spaces for you.)
* Use the up and down arrow keys to navigate previously entered commands.

### File paths

A **relative file path** specifies the path to a file, taking into account your current working directory. For example, if you were to give someone "relative" directions to your house, you would give them directions from their current location (the relative path from where they are to where you are).

An **absolute file path** specifies the complete path to a file, ignoring your current working directory. For example, if you were to give someone "absolute" directions to your house, you would start by telling them to be on earth, then go to your continent, then go to your country, then go to your region, etc.


### Basic commands

##### `pwd`
* **p**rints **w**orking **d**irectory (the directory you are currently in)

##### `ls`
* **l**i**s**ts files and subdirectories in your working directory
* `ls -a` lists **a**ll files, including hidden files
* `ls -l` lists the files in a **l**ong format with extra information (permissions, size, last modified date, etc.)
* `ls *` also lists the contents of subdirectories (one level deep) in your working directory
* `ls <path>` lists files in a specific directory (without changing your working directory)

##### `clear`
* **clear**s all output from your console

##### `cd`
* `cd <path>` **c**hanges **d**irectory to the path you specify, which can be a relative path or an absolute path
* `cd ..` moves you "up" one directory (to the parent directory)
* `cd` moves you to your "home" directory

##### `mkdir`
* `mkdir <dirname>` **m**a**k**es a new **dir**ectory called `<dirname>`

##### `touch`
* `touch <filename>` creates an empty file called `<filename>`
* This is useful for creating empty files to be edited at a later time.

##### `rm -i`
* `rm <filename>` **r**e**m**oves (deletes) a file permanently
* `rm -i <filename>` removes files in **i**nteractive mode, in which you are prompted to confirm that you really want to delete the file. It's best to always use `rm -i`.
* `rm -ir <dirname>` removes a directory and **r**ecursively deletes all of its contents

##### `mv`
* `mv <filename> <new path>` **m**o**v**es a file from its current location to `<new path>`
* `mv <filename> <new filename>` renames a file without changing its location

##### `cp`
* `cp <filename> <new path>` **c**o**p**ies a file from its current location to `<new path>`, leaving the original file unchanged
* `cp <filename> <new filename>` copies a file without changing its location


### Class exercise
* Open your command line interface.
* Navigate to your Desktop, and confirm you are there:
    * Print your working directory (it should end with `Desktop`).
    * List your files and subdirectories (they should match what you see on your Desktop).
* Create a directory called `project`, and then add the following contents:
    * Create three files in the `project` directory: `draft_paper.md`, `plot1.png`, `plot2.png`.
    * Create a subdirectory of `project` called `code`, and then create the following files in it: `processing.py`, `exploration.py`, `modeling.py`.
    * Create a subdirectory of `project` called `data`, and then create the following files in it: `original.csv`, `clean.csv`, `extra.csv`.
* Navigate back to `project`, and then confirm that you have created the correct structure by printing out (with a single command) all of its files, subdirectories, and the contents of those subdirectories.
* Create a subdirectory called `viz`, and then move `plot1.png` and `plot2.png` to `viz`.
* Rename `plot1.png` as `scatterplot.png`, and rename `plot2.png` as `histogram.png`.
* Delete `extra.csv` from `data`.
* Make a copy of `draft_paper.md` called `final_paper.md`.
* Once again, print out all of the contents of `project` to confirm you have the correct structure.


### Intermediate commands

##### `head`
* `head <filename>` prints the **head** (the first 10 lines) of the file
* `head -n20 <filename>` prints the first 20 lines of the file
* This is useful for previewing the contents of a large file without opening it.

##### `tail`
* `tail <filename>` prints the **tail** (the last 10 lines) of the file

##### `cat`
* `cat <filename>` prints the entire file

##### `less`
* `less <filename>` allows you to page or scroll through the file
* Hit the spacebar to go down a page, use the arrow keys to scroll up and down, and hit `q` to exit.

##### `wc`
* `wc <filename>` returns the **c**ount of lines, **w**ords, and characters in a file
* `wc -l <filename>` only counts lines, `wc -w <filename>` only counts words, and `wc -c <filename>` only counts characters
* A "word" is defined as any set of characters delimited by a space.

##### `find`
* `find <path> -name <name>` will recursively search the specified path (and its subdirectories) and **find** files and directories with a given `<name>`
    * Use `.` for the `<path>` to refer to the working directory.
* For the `<name>`, you can search for an exact match, or use wildcard characters to search for a partial match:
    * `*` specifies any number of any characters, such as `find . -name *.py` or `find . -name *data*.*`
    * `?` specifies one character, such as `find . -name ??_*.*`

##### `grep`
* `grep <pattern> <filename>` searches a file for a **r**egular **e**xpression **p**attern and prints the matching lines
    * The pattern should be in quotation marks to allow for multiple words.
    * The pattern is case-sensitive by default, but you can use the `-i` option to **i**gnore case.
    * You can use wildcards in the filename to search multiple files, but it only searches the working directory (not subdirectories).
* `grep -r <pattern> <path>` does a **r**ecursive search of the path (checks subdirectories) for matches within files
    * Use `.` for the `<path>` to refer to the working directory.
* `grep <pattern>` does a **g**lobal search (of your entire computer) for matches
    * Hit `Ctrl + c` if you want to cancel the search.
* Much more complex string-matching patterns can be used (which we will cover in a future class).

##### `|`
* `<command 1> | <command 2>` pipes the results from `<command 1>` into `<command 2>`, and then the results of `<command 2>` are printed to the console

##### `>`
* `<command> > <filename>` takes the output of `<command>` and saves it in `<filename>`
* This will overwrite the file if it already exists.

##### `>>`
* `<command> >> <filename>` takes the output of `<command>` and appends it to `<filename>`
* This will create the file if it does not yet exist.


### Exercise
1. Using `chipotle.tsv` in the `data` subdirectory:
    1. Look at the head and the tail, and think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)
    2. How many orders do there appear to be?
    3. How many lines are in the file?
    4. Which burrito is more popular, steak or chicken?
    5. Do chicken burritos more often have black beans or pinto beans?
2. Make a list of all of the CSV or TSV files in the DAT7 repo (using a single command). Think about how wildcard characters can help you with this task.
3. Count the number of occurrences of the word 'dictionary' (regardless of case) across all files in the DAT7 repo.
4. **Optional:** Use the the command line to discover something "interesting" about the Chipotle data. The advanced commands below may be helpful to you!


### Advanced commands

##### `cut`
* `cut -f1,2 <filename>` **cut**s a tab-delimited file into columns and returns the first two **f**ields
* `cut -f1,2 -d, <filename>` indicates that the file is **d**elimited by commas

##### `sort`
* `sort <filename>` **sort**s a file by the first field

##### `uniq`
* `uniq <filename>` discards all but one of the successive identical lines (thus it only keeps **uniq**ue lines)
* `uniq -c <filename>` also records the **c**ount of the number of occurrences
* Because lines must be successive to be counted as identical, you will usually use `sort` before `uniq`.
