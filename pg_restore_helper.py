#!/usr/bin/env python3

from os import listdir, getcwd, system
import subprocess

import inquirer

try:
    # get database config
    db_config = open('config/database.yml').read()

    db_names = []

    # parse names from YAML
    for line in db_config.split('\n'):
        # only parse lines that list the database name
        if 'database: ' in line:
            db_names.append(line.split(': ')[1])

    # ask user which db they want to restore
    db_name = inquirer.list_input(
        'Which database do you want to restore?', choices=db_names,
    )

    # find dump files in current directory
    files = listdir('.')
    dump_files = [file for file in files if '.dump' in file]

    # ask which .dump file the user wants to use to restore
    dump_file = inquirer.list_input(
        'Which dump file do you want to use to restore your database?',
        choices=dump_files,
    )

    system(
        f"pg_restore --verbose --clean --no-acl --no-owner -h localhost -U $USER -d {db_name} {getcwd()}/{dump_file}"
    )

except Exception as err:
    raise
