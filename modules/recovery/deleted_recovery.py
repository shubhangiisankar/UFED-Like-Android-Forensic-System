import os
import shutil

# 🔹 File type definitions
VIDEO_EXTENSIONS = (".mp4", ".3gp", ".mkv", ".avi")
DOCUMENT_EXTENSIONS = (
    ".pdf", ".doc", ".docx",
    ".txt", ".ppt", ".pptx",
    ".xls", ".xlsx", ".csv"
)
IMAGE_EXTENSIONS = (
    ".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif"
)


# 🔹 Locations where deleted artifacts usually remain
SUSPICIOUS_KEYWORDS = [
    # Cache & residual locations
    "cache", "Cache", "temp", ".thumb", ".thumbnails",

    # Messaging / app data
    "WhatsApp", "Snapchat",

    # Media folders
    "Video", "Documents", "Download"
]


def is_suspicious_path(path):
    return any(keyword in path for keyword in SUSPICIOUS_KEYWORDS)


# ---------------- VIDEO RECOVERY ----------------

def recover_deleted_videos(source_dir, output_dir):
    videos_dir = os.path.join(output_dir, "videos")
    os.makedirs(videos_dir, exist_ok=True)

    recovered_videos = []

    print("[*] Scanning for deleted / cached video artifacts...")

    for root, _, files in os.walk(source_dir):
        if not is_suspicious_path(root):
            continue

        for file in files:
            if file.lower().endswith(VIDEO_EXTENSIONS):
                src = os.path.join(root, file)
                dst = os.path.join(videos_dir, file)

                if not os.path.exists(dst):
                    try:
                        shutil.copy2(src, dst)
                        recovered_videos.append(dst)
                        print(f"[RECOVERED VIDEO] {file}")
                    except Exception as e:
                        print(f"[ERROR] {file}: {e}")

    print(f"[✔] Total recovered videos: {len(recovered_videos)}")
    return recovered_videos


# ---------------- DOCUMENT RECOVERY ----------------

def recover_deleted_documents(source_dir, output_dir):
    documents_dir = os.path.join(output_dir, "documents")
    os.makedirs(documents_dir, exist_ok=True)

    recovered_documents = []

    print("[*] Scanning for deleted / cached document artifacts...")

    for root, _, files in os.walk(source_dir):
        if not is_suspicious_path(root):
            continue

        for file in files:
            if file.lower().endswith(DOCUMENT_EXTENSIONS):
                src = os.path.join(root, file)
                dst = os.path.join(documents_dir, file)

                if not os.path.exists(dst):
                    try:
                        shutil.copy2(src, dst)
                        recovered_documents.append(dst)
                        print(f"[RECOVERED DOCUMENT] {file}")
                    except Exception as e:
                        print(f"[ERROR] {file}: {e}")

    print(f"[✔] Total recovered documents: {len(recovered_documents)}")
    return recovered_documents
# ---------------- IMAGE RECOVERY ----------------

def recover_deleted_images(source_dir, output_dir):
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    recovered_images = []

    print("[*] Scanning for deleted / cached image artifacts...")

    for root, _, files in os.walk(source_dir):
        if not is_suspicious_path(root):
            continue

        for file in files:
            if file.lower().endswith(IMAGE_EXTENSIONS):
                src = os.path.join(root, file)
                dst = os.path.join(images_dir, file)

                if not os.path.exists(dst):
                    try:
                        shutil.copy2(src, dst)
                        recovered_images.append(dst)
                        print(f"[RECOVERED IMAGE] {file}")
                    except Exception as e:
                        print(f"[ERROR] {file}: {e}")

    print(f"[✔] Total recovered images: {len(recovered_images)}")
    return recovered_images
