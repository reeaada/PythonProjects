"""
=============================================================
  PROGRAM 1 — Fetch ALL files on Windows and store their
              full paths in a list.
=============================================================

HOW IT WORKS (explained like you're 6):
  Imagine your hard drive is a HUGE building.
  This program sends a robot (os.walk) into that building.
  The robot goes into EVERY room (folder), including rooms
  inside rooms inside rooms.
  In each room, it picks up every OBJECT (file) it finds,
  reads the full address on it (full path), and drops it
  into a big bag (the list).
  When the robot is done, you have a bag with the address
  of literally every single file on your drive.
=============================================================
"""

import os          # Our main tool for working with the file system
import time        # We use this to measure how long the scan takes
import sys         # Used to print progress on the same line (no newline spam)


def fetch_all_files(root_path: str) -> list[str]:
    """
    Walks the entire directory tree starting at `root_path`
    and returns a list containing the full absolute path of
    every file found.

    Parameters
    ----------
    root_path : str
        The folder where the scan should start.
        Example: "C:\\" to scan the entire C drive.

    Returns
    -------
    list[str]
        A flat list of full file paths (strings).
        Example: ["C:\\Windows\\notepad.exe", "C:\\Users\\You\\notes.txt", ...]
    """

    all_files = []        # This is our "bag" — starts empty, we fill it up
    start_time = time.time()   # Record when we started (to measure speed)
    file_count = 0        # Counter so we can show progress

    # -------------------------------------------------------
    # os.walk(root_path) is the CORE of this whole program.
    #
    # It's a generator — every time you ask it for the next
    # value, it goes one folder deeper and returns:
    #
    #   folder_path  → the FULL PATH of the current folder
    #                  example: "C:\Users\You\Desktop"
    #
    #   subfolders   → a LIST of folder names inside that folder
    #                  example: ["projects", "photos"]
    #                  (just the NAMES, not full paths)
    #
    #   files        → a LIST of file names inside that folder
    #                  example: ["todo.txt", "photo.jpg"]
    #                  (just the NAMES, not full paths)
    #
    # The loop automatically goes into every subfolder too,
    # so we don't need to write any recursion ourselves.
    # os.walk does ALL the heavy lifting for us!
    # -------------------------------------------------------
    for folder_path, subfolders, files in os.walk(root_path):

        # files is a list like ["notes.txt", "photo.jpg"]
        # But we need the FULL path, not just the name.
        # We combine folder_path + file name using os.path.join()
        # to get something like "C:\Users\You\Desktop\notes.txt"
        for file_name in files:

            # os.path.join() glues the folder path and file name together.
            # It's smarter than just writing folder_path + "\\" + file_name
            # because it handles edge cases and works on all operating systems.
            full_path = os.path.join(folder_path, file_name)

            # Drop the full path into our bag (the list)
            all_files.append(full_path)
            file_count += 1

            # Print progress every 1000 files so we can see it's working.
            # "\r" moves the cursor back to the start of the line (no new lines)
            # end="" prevents print() from adding a newline character
            if file_count % 1000 == 0:
                elapsed = time.time() - start_time
                sys.stdout.write(
                    f"\r  Scanning... {file_count:,} files found | "
                    f"{elapsed:.1f}s elapsed | Current: {folder_path[:50]}..."
                )
                sys.stdout.flush()   # Force the output to actually show up

    # Print a final newline so the next print() starts on a clean line
    print()
    return all_files


# -------------------------------------------------------
# MAIN SCRIPT — This is what actually runs when you
# execute the file. The if __name__ == "__main__" guard
# means this code only runs when YOU directly run this
# file, NOT when another script imports it.
# -------------------------------------------------------
if __name__ == "__main__":

    # ---- CONFIGURE YOUR SCAN HERE ----------------------
    # Change this to any folder you want to scan.
    # Use "C:\\" for the full C drive (takes a while!).
    # Use os.path.expanduser("~") for just your home folder.
    ROOT = os.path.expanduser("~")    # Scans your home folder (C:\Users\YourName)
    # ROOT = "C:\\"                   # Uncomment to scan the FULL C drive
    # ROOT = r"C:\Users\You\Documents"  # Or a specific folder
    # -------------------------------------------------------

    print("=" * 60)
    print("  FILE SCANNER — Program 1")
    print("=" * 60)
    print(f"  Root directory : {ROOT}")
    print(f"  Starting scan  ...")
    print("-" * 60)

    # Run the scan — this returns our big list of paths
    file_list = fetch_all_files(ROOT)

    # ---- RESULTS ------------------------------------------
    elapsed_total = time.time()
    print("-" * 60)
    print(f"  Total files found : {len(file_list):,}")
    print("=" * 60)

    # Show a preview — just the first 20 paths so we don't
    # flood the terminal with thousands of lines
    print("\n  PREVIEW (first 20 results):")
    print("-" * 60)
    for i, path in enumerate(file_list[:20], start=1):
        print(f"  [{i:>3}]  {path}")

    if len(file_list) > 20:
        print(f"  ... and {len(file_list) - 20:,} more files.")

    # ---- OPTIONAL: SAVE TO A TEXT FILE --------------------
    # Uncomment the block below to save ALL paths to a file.
    # output_file = "all_files.txt"
    # with open(output_file, "w", encoding="utf-8") as f:
    #     f.write("\n".join(file_list))
    # print(f"\n  Saved to: {output_file}")