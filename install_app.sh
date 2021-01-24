#!/bin/bash

set -e

python3.8 -m venv .venv
echo "[info step 1/4] virtual environment was created"

source .venv/bin/activate
echo "[info step 2/4] application was activated"

pip3.8 install wheel
echo "[info step 3/4] wheel installed"

pip3.8 install -r requirements.txt
echo "[info step 4/4] dependencies were installed"
