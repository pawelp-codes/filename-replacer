import os

def replace_text_in_filenames(folder_path: str, old: str, new: str) -> None:
    """
    Rename files inside a given folder by replacing a chosen substring.
    (EN) Rename files by replacing part of their names.

    Zmienia nazwy plików w podanym folderze, zastępując wybrany fragment tekstu.
    """

    # Check if the folder exists
    # (EN) Verify that the folder exists before processing
    # (PL) Sprawdź, czy podany folder istnieje
    if not os.path.isdir(folder_path):
        print(f"Folder '{folder_path}' does not exist. / Folder '{folder_path}' nie istnieje.")
        return

    # Iterate through all items in the folder
    # (EN) Loop through each item inside the folder
    # (PL) Iteruj przez każdy element w folderze
    for filename in os.listdir(folder_path):

        # Skip this script to avoid renaming itself
        # (EN) Skip renaming this script to avoid breaking it
        # (PL) Pomiń ten plik, aby skrypt nie zmienił swojej własnej nazwy
        if filename == "change name.py":
            continue

        old_path = os.path.join(folder_path, filename)

        # Process only files, ignore directories
        # (EN) Only rename files, skip subfolders
        # (PL) Zmieniaj tylko pliki, pomijaj podfoldery
        if os.path.isfile(old_path):

            # Replace the substring in the filename
            # (EN) Replace the target text within the filename
            # (PL) Zamień wskazany tekst w nazwie pliku
            new_filename = filename.replace(old, new)
            new_path = os.path.join(folder_path, new_filename)

            # Rename the file
            # (EN) Perform the actual renaming
            # (PL) Wykonaj zmianę nazwy
            os.rename(old_path, new_path)
            print(f"Renamed / Zmieniono: '{filename}' → '{new_filename}'")


# Example usage:
# (EN) Automatically detect the script's directory
# (PL) Automatycznie wykryj katalog, w którym znajduje się skrypt
script_directory = os.path.dirname(__file__)

# (EN) Replace underscores with spaces in filenames
# (PL) Zamień podkreślenia na spacje w nazwach plików
replace_text_in_filenames(script_directory, "_", " ")
