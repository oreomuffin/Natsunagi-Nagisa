import os
import time
import psutil

from telegram import ParseMode, __version__ as peler
from platform import python_version as memek
from telethon import __version__ as tlh
from pyrogram import __version__ as pyr

import Natsunagi.modules.no_sql.users_db as user_db
from Natsunagi import StartTime
from Natsunagi.modules.helper_funcs import formatter

# Stats Module


async def bot_sys_stats():
    bot_uptime = int(time.time() - StartTime)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
arya@MacBook:~$ NatsunagiProBot:
------------------
OS: Debian GNU/Linux 10 (buster) x86_64
Host: Google Compute Engine
Kernel: 4.19.0-18-cloud-amd64
Uptime: {formatter.get_readable_time((bot_uptime))}
Packages: 343 (dpkg)
Shell: bash 5.0.3
Release: 11
System: IOS
Node name: macOS
Machine: macOS Mojave 10.14.6
Bot: {round(process.memory_info()[0] / 1024 ** 2)} MB
CPU: Intel Xeon (96) @ 2.000GHz
Memory: 190876MiB / 593872MiB
CPU Usage: {cpu}%
Ram Usage: {mem}%
Disk: {disk}%
Python version: {memek()}
Library version: v{peler}
Telethon version: {tlh}
Pyrogram version: {pyr}
Users: {user_db.num_users()} users.
Groups: {user_db.num_chats()} groups.
"""

    return stats
