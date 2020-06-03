## Getting Started

This is a project that will transform your user account or an alternate number into a bot account that will allow you to perform the "welcome" function on your group, ban, remove the ban, restrict a user from speaking in your group, remove the restriction and you can have more resources in the future

Below I am providing instructions for you to have a copy of the project, these instructions will show you how to start using it for learning, development and testing purposes.

:warning: Note: This project is for learning, development and testing purposes, I am not responsible for any use that has other purposes!

## Configuring the bot to run on the terminal

You must have your machine up to date and have Python 3 installed, as well as modules such as: telethon, if you don't have it, you will need to install it this way here:
```
# Tested on Ubuntu 14.04, 15.04 and 16.04, Debian 7, Linux Mint 17.2
$ sudo apt-get update && sudo apt-get upgrade   
$ sudo apt install python3 && python3-pip
$ sudo pip3 install telethon
```
With everything installed,  we will clone the repository like this:

```
$ git clone https://github.com/VycktorStark/Userbot.git
```
To add your token to the project, I advise you to configure your ".bashrc", putting something like:
```
export APIKEYHASID="12918981"
export APIKEYHASID="dFwnfweFw2oju28ru239r8389iEJOIJO"
export YOURID="-10001291898109"
export GROUPSNAME="MEU GRUPO"
```

Or just configure the `tools.py`

## Boot process

- To start the bot, run: sudo ./main.py
- To stop the bot, press Ctrl + C.
You can also start the bot with python3 main.py, to stop the bot, press Ctrl + C.

Also read the [Telethon](https://docs.telethon.dev/en/latest/basic/signing-in.html), lib documentation used to create this project.
