from modules.recovery.deleted_recovery import (
    recover_deleted_videos,
    recover_deleted_documents,
    recover_deleted_images
)

from modules.acquisition.adb_check import check_adb_device
from modules.acquisition.pull_data import pull_sdcard
from modules.filesystem.parser import parse_filesystem
from modules.metadata.metadata_extractor import extract_video_metadata
from modules.metadata.hash_generator import generate_file_hashes
from modules.ui.cli_report import generate_forensic_report


if __name__ == "__main__":

    # 🔁 Recovery mode
    # Options: "video", "document", "image", "all"
    RECOVERY_MODE = "document"

    # 📌 Paths
    ANDROID_DUMP_PATH = "android_dump"
    RECOVERED_FILES_PATH = "android_dump/recovered_files"

    if check_adb_device():

        # 1️⃣ Acquire data (comment this if evidence already pulled)
        pull_sdcard()

        # 2️⃣ Parse filesystem
        parse_filesystem()

        # 🔹 Initialize empty results
        recovered_videos = []
        recovered_documents = []
        recovered_images = []

        # 3️⃣ Conditional recovery based on mode
        if RECOVERY_MODE == "video":
            recovered_videos = recover_deleted_videos(
                ANDROID_DUMP_PATH,
                RECOVERED_FILES_PATH
            )

        elif RECOVERY_MODE == "document":
            recovered_documents = recover_deleted_documents(
                ANDROID_DUMP_PATH,
                RECOVERED_FILES_PATH
            )

        elif RECOVERY_MODE == "image":
            recovered_images = recover_deleted_images(
                ANDROID_DUMP_PATH,
                RECOVERED_FILES_PATH
            )

        elif RECOVERY_MODE == "all":
            recovered_videos = recover_deleted_videos(
                ANDROID_DUMP_PATH,
                RECOVERED_FILES_PATH
            )
            recovered_documents = recover_deleted_documents(
                ANDROID_DUMP_PATH,
                RECOVERED_FILES_PATH
            )
            recovered_images = recover_deleted_images(
                ANDROID_DUMP_PATH,
                RECOVERED_FILES_PATH
            )

        else:
            print("[-] Invalid RECOVERY_MODE selected")

        # 4️⃣ Extract metadata (supports all file types)
        extract_video_metadata(RECOVERED_FILES_PATH)

        # 5️⃣ Generate hashes
        generate_file_hashes(RECOVERED_FILES_PATH)

        # 6️⃣ Generate forensic report
        generate_forensic_report()

        # 7️⃣ Final summary
        print("\n===== RECOVERY SUMMARY =====")
        print("[+] Deleted video files recovered:", len(recovered_videos))
        print("[+] Deleted document files recovered:", len(recovered_documents))
        print("[+] Deleted image files recovered:", len(recovered_images))

    else:
        print("[-] Device not connected")
