import subprocess
import telebot

# Telegram bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# Create an instance of the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Variables to store the last directory and command
last_directory = ''
last_command = ''

# Command handler for the /exec command
@bot.message_handler(commands=['exec'])
def handle_exec_command(message):
    global last_directory, last_command

    command = message.text.split(' ', 1)[1]  # Extract the command from the message
    if command.startswith('cd '):
        directory = command.split(' ', 1)[1]
        last_directory = directory
        output = change_directory(directory)
    else:
        last_command = command
        output = execute_command(command)

    bot.reply_to(message, output)  # Send the output back to the user

# Execute a command and return the output
def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()
    except subprocess.CalledProcessError as e:
        output = e.output.decode()
    return output

# Change the current directory and return the output
def change_directory(directory):
    global last_directory

    try:
        output = subprocess.check_output(f'cd /d {directory} && cd', shell=True, stderr=subprocess.STDOUT).decode()
        last_directory = directory
    except subprocess.CalledProcessError as e:
        output = e.output.decode()
    return output

# Start the bot
bot.polling()
