Sure! Here's a step-by-step guide to extracting metadata from a directory of photos using Python and Notable:

Step 1: Install Notable

Notable is a Python library that allows you to extract metadata from images. You can install it using pip:
```
pip install notable
```
Step 2: Import the necessary libraries

In your Jupyter notebook, import the necessary libraries:
```python
import os
import notable
from PIL import Image
```
Step 3: Define the directory path

Define the path to the directory containing the photos you want to extract metadata from:
```python
directory_path = '/path/to/photos'
```
Step 4: Loop through the files in the directory

Use the `os` library to loop through the files in the directory:
```python
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
```
Step 5: Extract the metadata

Use the `notable` library to extract the metadata for each file:
```python
metadata = notable.extract(file_path)
```
Step 6: Store the metadata in a dictionary

Store the metadata in a dictionary, where the key is the file name and the value is the metadata:
```python
metadata_dict = {}
for filename, metadata in zip(os.listdir(directory_path), [notable.extract(file_path) for file_path in os.listdir(directory_path)]):
    metadata_dict[filename] = metadata
```
Step 7: Save the metadata to a Jupyter notebook

Save the metadata dictionary to a Jupyter notebook:
```python
notebook.save(metadata_dict, 'photos_metadata.ipynb')
```
Here's the complete code:
```python
import os
import notable
from PIL import Image

# Define the directory path
directory_path = '/path/to/photos'

# Loop through the files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    
    # Extract the metadata
    metadata = notable.extract(file_path)
    
    # Store the metadata in a dictionary
    metadata_dict = {}
    for filename, metadata in zip(os.listdir(directory_path), [notable.extract(file_path) for file_path in os.listdir(directory_path)]):
        metadata_dict[filename] = metadata
    
    # Save the metadata to a Jupyter notebook
    notebook.save(metadata_dict, 'photos_metadata.ipynb')
```
This code will extract the metadata for all images in the specified directory and store it in a Jupyter notebook named `photos_metadata.ipynb`. You can then use this notebook to view and analyze the metadata for each image.