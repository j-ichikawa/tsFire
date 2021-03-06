#!/usr/bin/env bash

set -e

if [ $# -ne 1 ]; then
  echo "Please specify the kinmu PDF."
  exit 1
fi

python3 -m venv venv
source venv/bin/activate
# shellcheck disable=SC2144
if [ ! -e venv/lib/python*/site-packages/pdfminer ]; then
  echo "startin' pip install..."
  pip3 install --target venv/lib/python*/site-packages -r requirements.txt 1> /dev/null
  echo "complete."
fi
python3 __main__.py "$1"
deactivate