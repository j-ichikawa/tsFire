#!/usr/bin/env bash

set -e

if [ $# -ne 1 ]; then
  echo "Please specify the kinmu PDF."
  exit 1
fi

python3 -m venv venv 1> /dev/null
source venv/bin/activate 1> /dev/null
pip3 install -r requirements.txt 1> /dev/null
python3 main.py "$1"
deactivate