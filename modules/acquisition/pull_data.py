import subprocess
import os

DEST = "android_dump/internal_storage"

def pull_sdcard():
    os.makedirs(DEST, exist_ok=True)
    print("[*] Pulling data from /sdcard")
    subprocess.run(["adb", "pull", "/sdcard/", DEST])
    print("[✔] Acquisition complete")
