#!/usr/bin/env bash
pip install -r requirements.txt
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
rm requirements.txt
pip freeze > requirements.txt
