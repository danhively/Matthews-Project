Sure! Here's a step-by-step guide to extracting metadata from a directory of photos using Python and Jupyter Notebook:

1. Install the necessary libraries:

You'll need to install the `pillow` library to read image files and the `pyexifread` library to extract metadata. You can install them using pip:
```
pip install pillow pyexifread
```
2. Import the libraries:

In your Jupyter Notebook, import the necessary libraries:
```python
from PIL import Image
from pyexifread import process_file
```
3. Loop through the images in the directory:

Use the `os` library to loop through all the files in the directory:
```python
import os

directory = '/path/to/images'

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Do something with the image file
        print(f"Processing {filename}")
        # Extract metadata
        image = Image.open(filepath)
        metadata = process_file(filepath, image._getexif())
        # Save metadata to a dictionary
        metadata_dict = {}
        for key, value in metadata.items():
            metadata_dict[key] = value
        # Save metadata to a CSV file
        with open(f"{filename}.csv", 'w', newline='') as csvfile:
            fieldnames = ['filename', 'metadata_key', 'metadata_value']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'filename': filename, 'metadata_key': key, 'metadata_value': value})
```
4. Extract metadata:

Use the `pyexifread` library to extract metadata from the image file. The `process_file()` function takes two arguments: the file path and the image object. It returns a dictionary containing the extracted metadata.

5. Save metadata to a dictionary:

Create an empty dictionary to store the metadata for each image. Iterate through the metadata dictionary and add each key-value pair to the corresponding image's dictionary.

6. Save metadata to a CSV file:

Use the `csv` library to save the metadata to a CSV file. Create a `DictWriter` object and write the header row. Then, iterate through the metadata dictionary and write each row to the CSV file.

7. Run the program:

Run the program by clicking the "Run" button or pressing Shift+Enter. The program will loop through all the images in the directory, extract metadata, and save it to a CSV file.

8. View the results:

Open the CSV file to view the extracted metadata. You should see a header row with the following columns: `filename`, `metadata_key`, and `metadata_value`. Each row represents a single image file, with the corresponding metadata key-value pairs.

That's it! You've successfully extracted metadata from a directory of images using Python and Jupyter Notebook. You can modify the code to extract different types of metadata or to handle different image file formats.