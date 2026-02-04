import os
import shutil
import datetime
import schedule
import time

source_dir = r"C:\Users\DHRUV CHAURASIA\OneDrive\Pictures\Screenshots"
destination_base = r"C:\Users\DHRUV CHAURASIA\OneDrive\Desktop\Backups"


def copy_folder_to_directory(source, destination_base):
    today = datetime.date.today()
    dest_dir = os.path.join(destination_base, str(today))

    # Create the folder if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)

    # Copy files from source to destination
    for filename in os.listdir(source):
        src_file = os.path.join(source, filename)
        dst_file = os.path.join(dest_dir, filename)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_file)  # copy or overwrite existing files

    print(f"Backup updated for: {dest_dir}")


# Schedule backup every day at 7:00 AM
schedule.every().day.at("06:55").do(
    copy_folder_to_directory, source_dir, destination_base
)

print("Backup scheduler started... waiting for 06:55 AM")

while True:
    schedule.run_pending()
    time.sleep(30)
