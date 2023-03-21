import sys
import ast
import json
import click


def parse_file(filename):
    with open(filename) as f:
        tree = ast.parse(f.read())

    imports = []
    functions = []
    comments = []

    for node in tree.body:
        if isinstance(node, ast.Import):
            imports.extend([alias.name for alias in node.names])
        elif isinstance(node, ast.ImportFrom):
            imports.extend([node.module])
        elif isinstance(node, ast.FunctionDef):
            functions.extend([node.name])
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
            comments.extend([node.value.s])

    return {
        'imports': imports,
        'functions': functions,
        'comments': comments
    }


@click.command()
@click.argument('files', nargs=-1)
@click.help_option('-h', '--help')
def cli(files):
    """
    Analyze Python code in a set of files.

    \b
    Usage:
    $ pydescriber.py file1.py file2.py ...
    $ ls *.py | pydescriber.py -
    """
    if len(files) == 0 or (len(files) == 1 and files[0] == '-'):
        files = sys.stdin.read().splitlines()

    results = {}

    for filename in files:
        try:
            results[filename] = parse_file(filename)
        except Exception as e:
            results[filename] = str(e)
            continue

    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    cli()

