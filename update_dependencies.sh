#!/bin/bash

source .venv/bin/activate
echo "[info] virtual env was activated"

pip3.8 freeze > requirements.txt
echo "[info] dependencies were updated"
