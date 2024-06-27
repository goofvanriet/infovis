#!/usr/bin/env python3

"""
Helper script to ensure every code cell is being hidden before deploying.
This is done by adding the `remove_input` metadata to each cell.
"""

import nbformat as nbf
from os import path
import json

ROOT_DIR = path.realpath(path.join(path.dirname(__file__), '..'))
DATASTORY_NB_FILEPATH = path.join(ROOT_DIR, 'notebooks', 'story.ipynb')

if __name__ == '__main__':
    try:
        with open(DATASTORY_NB_FILEPATH, 'r', encoding='utf-8') as f:
            ntbk = nbf.read(f, as_version=4)
    except (json.JSONDecodeError, nbf.reader.NotJSONError) as e:
        print(f"Error reading the notebook file: {e}")
        exit(1)

    for cell in ntbk.cells:
        # Retrieve existing cell tags.
        cell_tags = cell.get('metadata', {}).get('tags', [])

        if 'remove_input' not in cell_tags:
            cell_tags.append('remove_input')

        cell['metadata']['tags'] = cell_tags

    with open(DATASTORY_NB_FILEPATH, 'w', encoding='utf-8') as f:
        nbf.write(ntbk, f)

    print('NOTE: Some files might have been changed, run "git status" to see which files have changed.')