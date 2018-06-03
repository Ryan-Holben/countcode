# countcode

This script counts the lines of code (or whatever) that you might have.

Usage:

`./countcode.py [base_directory] [ext1 ext2 ext3 ...]`

If no extensions are provided, all types of files will be counted. Including the `.` in front of your extension is optional (e.g. both `.cpp` and `cpp` work). Results are sorted by number of lines.

Example output:

```
ryan@MyMachine:~/dev/countcode$ ./countcode.py ~/dev/Swaps/
Checking all extensions
| Extension   |   # files |   # lines |
|-------------+-----------+-----------|
| .o          |         6 |     46178 |
|             |        14 |      3365 |
| .cpp        |         6 |       530 |
| .sample     |         9 |       487 |
| .h          |         6 |       144 |
| .pack       |         1 |       123 |
| .md         |         2 |        49 |
| .idx        |         1 |        15 |

```

or

```
ryan@MyMachine:~/dev/countcode$ ./countcode.py ~/dev/Swaps/ .cpp .h md
Checking 3 extensions: ['.cpp', '.h', '.md']
| Extension   |   # files |   # lines |
|-------------+-----------+-----------|
| .cpp        |         6 |       530 |
| .h          |         6 |       144 |
| .md         |         2 |        49 |
```