#!/usr/bin/env python3

from os import listdir, getcwd, system
import subprocess

import inquirer

# 1. Read database config from yaml file
db_config = open('config/database.yml').read()

db_names = []

# 2. Get database names from database config
for line in db_config.split('\n'):
    if 'database: ' in line:
        name = line.split(': ')[1]
        db_names.append(name)

# 3. Ask user which database they want to restore
db_name = inquirer.list_input(
    "Which database do you want to restore?", choices=db_names
)

# 4. Ask user which dump file they want to use
files = listdir('.')
dump_files = [file for file in files if '.dump' in file]

dump_file = inquirer.list_input(
    "Which dump file do you want to use to restore?", choices=dump_files
)

# 5. Run pg_restore command
system(
    f"pg_restore --verbose --clean --no-acl --no-owner -h localhost -U $USER -d {db_name} {getcwd()}/{dump_file}"
)
