#!/usr/bin/env sh

set -e

if [ $# -ne 1 ]; then
  echo "Please specify the kinmu PDF."
  exit 1
fi

# shellcheck disable=SC1035
if !(pip3 > /dev/null 2>&1); then
  if [ ! -e get-pip.py ]; then
    echo "startin' enable pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
    echo "complete."
  fi
  . ~/.profile
fi

python3 -m venv --without-pip venv
. venv/bin/activate
# shellcheck disable=SC2144
if [ ! -e venv/lib/python*/site-packages/pdfminer ]; then
  echo "startin' pip install..."
  pip3 install --target venv/lib/python*/site-packages -r requirements.txt 1> /dev/null
  echo "complete."
fi

python3 __main__.py "$1"
deactivate