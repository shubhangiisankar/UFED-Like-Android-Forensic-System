import subprocess

def check_adb_device():
    try:
        result = subprocess.check_output(["adb", "devices"]).decode()
        lines = result.strip().split("\n")

        if len(lines) > 1 and "device" in lines[1]:
            print("[✔] Android device detected")
            return True
        else:
            print("[✘] No Android device detected")
            return False
    except:
        print("[✘] ADB not installed or device issue")
        return False
