from zipfile import ZipFile
import os

# Create a ZipFile Object
with ZipFile('..//FileAutomation.zip', 'w') as zipObj2:
   # Add multiple files to the zip
   for dirpath, dirnames, files in os.walk("."):
      for file in files:
         path = os.path.join(dirpath, file)
         zipObj2.write(path, os.path.basename(path))