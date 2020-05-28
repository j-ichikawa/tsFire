#!/usr/bin/env bash

set -e

if [ $# -ne 1 ]; then
  echo "Please specify the kinmu PDF."
  exit 1
fi

# shellcheck disable=SC1035
if !(pip3 > /dev/null 2>&1); then
  echo "start install pip..."
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python3 get-pip.py
  # shellcheck disable=SC2016
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bash_profile
  source ~/.bash_profile
  echo "complete."
fi

python3 -m venv --without-pip venv 1> /dev/null
source venv/bin/activate 1> /dev/null
pip3 install -r requirements.txt 1> /dev/null
python3 __main__.py "$1"
deactivate