def show_report():
    print("[*] CLI report generation placeholder")
import os
import csv
import hashlib
import datetime

VIDEO_DIR = "android_dump/recovered_files/videos"
REPORT_PATH = "reports/forensic_report.csv"


def generate_forensic_report():
    os.makedirs("reports", exist_ok=True)

    print("[*] Generating forensic report...")

    with open(REPORT_PATH, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "File Name",
            "File Path",
            "File Size (KB)",
            "Created Time",
            "Modified Time",
            "MD5",
            "SHA256"
        ])

        for filename in os.listdir(VIDEO_DIR):
            file_path = os.path.join(VIDEO_DIR, filename)

            if os.path.isfile(file_path):
                stats = os.stat(file_path)

                # Generate hashes
                md5 = hashlib.md5()
                sha256 = hashlib.sha256()

                with open(file_path, "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        md5.update(chunk)
                        sha256.update(chunk)

                writer.writerow([
                    filename,
                    file_path,
                    round(stats.st_size / 1024, 2),
                    datetime.datetime.fromtimestamp(stats.st_ctime),
                    datetime.datetime.fromtimestamp(stats.st_mtime),
                    md5.hexdigest(),
                    sha256.hexdigest()
                ])

    print(f"[✔] Forensic report generated: {REPORT_PATH}")


if __name__ == "__main__":
    generate_forensic_report()
