#!/bin/bash

set -e

python3.8 -m venv .venv
echo "[info step 1/6] virtual environment was created"

source .venv/bin/activate
echo "[info step 2/6] application was activated"

pip3.8 install wheel
echo "[info step 3/6] wheel installed"

pip3.8 install -r requirements.txt
echo "[info step 4/6] dependencies were installed"

mkdir -p data/temp
echo "[info step 5/6] data/temp was created"

mkdir db
echo "[info step 6/6] database folder was created"
