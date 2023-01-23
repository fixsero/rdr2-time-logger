import datetime
import os
import psutil
import time

def log_start_time():
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("RDR2_playtime_log.txt", "a") as file:
        file.write(date_time + " Red Dead Redemption 2 started\n")

def log_end_time():
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("RDR2_playtime_log.txt", "a") as file:
        file.write(date_time + " Red Dead Redemption 2 ended\n")

def check_if_playing():
    log_start_time()
    while True:
        if "RDR2.exe" not in (p.name() for p in psutil.process_iter()):
            log_end_time()
            break
        time.sleep(60)

check_if_playing()
