#!/bin/zsh

# create venv
echo "create venv"
python -m venv venv

# activate venv
echo "activate venv"
source aiogram-chat-bot/venv/scripts/activate.bat

# upgd pip in venv
echo "upgd pip"
pip install pip --upgrade

# install requirements
echo "install requirements"
python -m install -r requirements.txt

# run
echo "run"
python app.py
