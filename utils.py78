import random
import time
import math
import os
from vars import CREDIT
from pyrogram.errors import FloodWait
from datetime import datetime, timedelta

class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False

def hrb(value, digits=2, delim="", postfix=""):
    if value is None:
        return None
    chosen_unit = "B"
    for unit in ("KB", "MB", "GB", "TB"):
        if value > 1000:
            value /= 1024
            chosen_unit = unit
        else:
            break
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix

def hrt(seconds, precision=0):
    pieces = []
    value = timedelta(seconds=seconds)

    if value.days:
        pieces.append(f"{value.days}day")

    seconds = value.seconds

    if seconds >= 3600:
        hours = int(seconds / 3600)
        pieces.append(f"{hours}hr")
        seconds -= hours * 3600

    if seconds >= 60:
        minutes = int(seconds / 60)
        pieces.append(f"{minutes}min")
        seconds -= minutes * 60

    if seconds > 0 or not pieces:
        pieces.append(f"{seconds}sec")

    if not precision:
        return "".join(pieces)

    return "".join(pieces[:precision])

def generate_progress_bar(percentage):
    try:
        perc_float = float(percentage.strip('%'))
    except:
        perc_float = 0
    total_length = 20
    filled = int(total_length * perc_float / 100)
    bar = '█' * filled + '░' * (total_length - filled)
    return f"[{bar}]"

timer = Timer()

async def progress_bar(current, total, reply, start):
    if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return
        else:
            perc = f"{current * 100 / total:.1f}%"
            elapsed_time = round(diff)
            speed = current / elapsed_time
            remaining_bytes = total - current
            if speed > 0:
                eta_seconds = remaining_bytes / speed
                eta = hrt(eta_seconds, precision=1)
            else:
                eta = "-"
            sp = str(hrb(speed)) + "/s"
            tot = hrb(total)
            cur = hrb(current)

            progress_bar_display = generate_progress_bar(perc)

            try:
                await reply.edit(
                    f'🧬═══════════[ STRANGER  SYSTEM – 2050 ]═══════════🧬\n'
                    f'┃ 🛰 MODULE       : ⌈ DATA UPLINK CORE vX.1 ⌋\n'
                    f'┃ 🔁 STATUS       : TRANSMITTING PAYLOAD\n'
                    f'┃ ⚙️ ENGINE LOAD  : {progress_bar_display}\n'
                    f'┃ 📶 COMPLETION   : {perc}\n'
                    f'┃ 🚀 THROUGHPUT   : {sp}\n'
                    f'┃ 📂 TRANSFERRED  : {cur}\n'
                    f'┃ 💾 TOTAL SIZE   : {tot}\n'
                    f'┃ ⏱️ EST. TIME     : {eta}\n'
                    f'┃ 🤖 POWER SOURCE : {CREDIT}\n'
                    f'🧬═════════════════════════════════════════════════🧬'
                )
            except FloodWait as e:
                time.sleep(e.x)
