# PyDescriber

This is a command-line tool for analyzing Python code in a set of files. It extracts information about the imports, functions, and comments in each file, and outputs the results in JSON format.

## Usage

You can run the tool by specifying a list of files to analyze. You can either provide the file list as command-line arguments, or read it from `stdin`. The tool will process each file and output the results in JSON format.

### Command-line arguments

```
python pydescriber.py file1.py file2.py file3.py
```

### Reading file list from `stdin`

```
ls *.py | python pydescriber.py -
```

### Output format

The output is a dictionary with one entry per file, where the key is the file name and the value is a dictionary with the following keys:

- `imports`: A list of strings representing the imported modules.
- `functions`: A list of strings representing the names of the functions defined in the file.
- `comments`: A list of strings representing the comments found in the file.

The purpose of this output is to provide a standardized format for input to ChatGPT, for the automatic generation of documentation.

Here's an example output:

```json
{
  "file1.py": {
    "imports": ["os", "sys"],
    "functions": ["main"],
    "comments": ["This is a comment."]
  },
  "file2.py": {
    "imports": ["numpy"],
    "functions": ["add", "subtract"],
    "comments": []
  }
}
```