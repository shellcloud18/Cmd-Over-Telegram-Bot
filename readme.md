# Telegram Command Prompt (CMD) Bot

The Telegram Command Prompt (CMD) Bot is a Python script that allows you to execute commands via a Telegram bot and receive the output as a reply. It combines the functionalities of a Windows command prompt (cmd) application and a Telegram bot.

## Features

- Execute commands using the `/exec` command followed by the desired command.
- Change the current directory using the `/exec cd <directory>` command.
- Retrieve the output of the executed command as a reply from the bot.
- Keeps track of the last executed directory and command.

## Prerequisites

- Python 3.6 or above
- `telebot` library (`pip install pyTelegramBotAPI`)

## Setup

1. Clone the repository or download the script file (`cmd_bot.py`) to your computer.

2. Install the required dependencies by running the following command:
3. Obtain a Telegram bot token by following these steps:
- Create a new bot on Telegram by talking to the BotFather bot.
- Copy the bot token provided by the BotFather.

4. Open the `cmd_bot.py` script in a text editor.

5. Replace `'YOUR_BOT_TOKEN'` with the bot token obtained in the previous step.

## Usage

1. Start the script by running the following command:
```
python cmd_bot.py
