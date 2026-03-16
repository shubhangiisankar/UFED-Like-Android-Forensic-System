import os
import datetime

# 📌 Common recovered files directory
RECOVERED_FILES_DIR = "android_dump/recovered_files"

# 📌 Supported file types (VIDEOS + DOCUMENTS)
SUPPORTED_EXTENSIONS = (
    ".mp4", ".mkv", ".avi",
    ".pdf", ".doc", ".docx",
    ".xls", ".xlsx", ".txt"
)


def extract_video_metadata(recovered_base_dir=RECOVERED_FILES_DIR):
    print("[*] Extracting metadata from recovered files...\n")

    for root, _, files in os.walk(recovered_base_dir):
        for file in files:
            if file.lower().endswith(SUPPORTED_EXTENSIONS):

                file_path = os.path.join(root, file)

                if os.path.isfile(file_path):
                    stats = os.stat(file_path)

                    metadata = {
                        "File Name": file,
                        "File Type": os.path.splitext(file)[1],
                        "File Size (KB)": round(stats.st_size / 1024, 2),
                        "Created Time": datetime.datetime.fromtimestamp(stats.st_ctime),
                        "Modified Time": datetime.datetime.fromtimestamp(stats.st_mtime),
                        "Accessed Time": datetime.datetime.fromtimestamp(stats.st_atime),
                        "File Path": file_path
                    }

                    for key, value in metadata.items():
                        print(f"{key}: {value}")

                    print("-" * 60)


if __name__ == "__main__":
    extract_video_metadata()
