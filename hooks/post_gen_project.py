#!/usr/bin/env python
import os
from glob import glob

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_files(fileglob, exclude=[], recursive=True):
    for file in glob(fileglob, recursive=recursive):
        if not file in exclude:
            remove_file(file)

if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if '{{ cookiecutter.docs }}' == "RST":
        remove_files("**/*.md")
    elif '{{ cookiecutter.docs }}' == "Markdown":
        remove_files("**/*.rst", exclude=glob("**/api.rst"))
