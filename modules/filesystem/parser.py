import os

ROOT = "android_dump/internal_storage"

def parse_filesystem():
    print("[*] Parsing file system")
    for root, dirs, files in os.walk(ROOT):
        for file in files:
            print(os.path.join(root, file))
