import asyncio
import getpass
import os
from configparser import ConfigParser

import click
import discord
import keyring

client = discord.Client()
user_section = "UserInfo"
discord_keyring_name = "term_shitter.discord"
cfg_location = os.path.expanduser('~/.term_shitter.cfg')

def channel_formatter(ch):
    return "{}:{}:{}".format(id(ch), ch.server.name, ch.name)


term_shitter_config = ConfigParser()
term_shitter_config.read([cfg_location])
if not term_shitter_config.has_section(user_section):
    term_shitter_config.add_section(user_section)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print()
    channels = [c for c in client.get_all_channels()]
    while True:
        for i, ch in enumerate(channels):
            print(i, channel_formatter(ch))
        channel_index = int(input("Channel: "))
        msg = input("Message: ")
        ch = channels[channel_index]
        print("Planning to send message to {}".format(ch.name))
        tmp = await client.send_message(ch, msg)


@click.command()
@click.option('--save', is_flag=True)
def term_shitter(save):
    if save:
        password, username = get_user_pass()

        term_shitter_config.set(user_section, 'username', username)
        with open(cfg_location, 'w') as fp:
            term_shitter_config.write(fp)
        keyring.set_password(discord_keyring_name, username, password)
    else:
        if term_shitter_config.has_option(user_section, 'username'):
            username = term_shitter_config.get(user_section, 'username')
        else:
            username = input("Username: ")
        password = keyring.get_password(discord_keyring_name, username)
        if password is None:
            password = getpass.getpass("Password: ")

    client.run(username, password)


def get_user_pass():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return password, username


def main():
    term_shitter()
