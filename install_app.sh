#!/bin/bash

set -e

python3.8 -m venv .venv
echo "[info step 1/5] virtual environment was created"

source .venv/bin/activate
echo "[info step 2/5] application was activated"

pip3.8 install wheel
echo "[info step 3/5] wheel installed"

pip3.8 install -r requirements.txt
echo "[info step 4/5] dependencies were installed"

mkdir -p data/temp
echo "[info step 5/5] data/temp was created"
