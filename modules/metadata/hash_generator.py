import os
import hashlib

# 🔹 Supported files (videos + documents)
SUPPORTED_EXTENSIONS = (
    ".mp4", ".mkv", ".avi",
    ".pdf", ".doc", ".docx",
    ".xls", ".xlsx", ".txt", ".csv"
)


def generate_file_hashes(recovered_base_dir):
    print("[*] Generating hash values for recovered files...\n")

    for root, _, files in os.walk(recovered_base_dir):
        for file in files:
            if file.lower().endswith(SUPPORTED_EXTENSIONS):
                file_path = os.path.join(root, file)

                try:
                    sha256 = hashlib.sha256()

                    with open(file_path, "rb") as f:
                        for chunk in iter(lambda: f.read(4096), b""):
                            sha256.update(chunk)

                    print(f"File: {file}")
                    print(f"SHA-256: {sha256.hexdigest()}")
                    print("-" * 60)

                except Exception as e:
                    print(f"[ERROR] Hashing {file}: {e}")


if __name__ == "__main__":
    generate_file_hashes("android_dump/recovered_files")
