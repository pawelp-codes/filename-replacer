# Filename Replacer / Zmieniacz Nazw Plików

A simple Python tool that automatically renames files in a folder by replacing one substring with another.  
Prosty skrypt w Pythonie, który automatycznie zmienia nazwy plików w folderze, zastępując wskazany fragment tekstu innym.

The script works directly in the folder where it is placed, ignores directories, and avoids renaming itself.  
Skrypt działa w folderze, w którym się znajduje, pomija katalogi i nie zmienia własnej nazwy.

## Usage / Użycie

1. Place the script in the folder containing the files you want to rename.  
   Umieść skrypt w folderze z plikami, które chcesz zmienić.

2. Run the script.  
   Uruchom skrypt.

3. All filenames will be updated according to the replacement rule.  
   Wszystkie nazwy plików zostaną zmienione zgodnie z zasadą zamiany.

## Examples / Przykłady

- Replace underscores with spaces  
  Zamiana podkreśleń na spacje  
  `("_", " ")`

- Replace spaces with dashes  
  Zamiana spacji na myślniki  
  `(" ", "-")`

- Remove unwanted fragments  
  Usuwanie niechcianych fragmentów  
  `("_old", "")`

- Add suffixes or prefixes  
  Dodawanie sufiksów lub prefiksów  
  `(".jpg", "_edited.jpg")`
