import os

folder = "C:\Users\parth\OneDrive\Desktop\Jewellery Pics\Cat\Nath"  # or specify full path
extension = '.jpg'  # Change to your file type
files = sorted([f for f in os.listdir(folder) if f.endswith(extension)])
for i, filename in enumerate(files, 1):
    new_name = f"Nath {i}{extension}"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))