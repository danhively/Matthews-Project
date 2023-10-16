
#######################
# A step-by-step guide to extracting metadata from a directory of photos using Python and Notable:
#
# Step 1: Install Notable
#
# Notable is a Python library that allows you to extract metadata from images. You can install it using pip:
#
# Step 2: Import the necessary libraries
#
# In your Jupyter notebook, import the necessary libraries:
# Step 3: Define the directory path
# 
# Define the path to the directory containing the photos you want to extract metadata from:
# Step 4: Loop through the files in the directory
# 
# Use the `os` library to loop through the files in the directory:
# Step 5: Extract the metadata
# 
# Use the `notable` library to extract the metadata for each file:
# Step 6: Store the metadata in a dictionary
# 
# Store the metadata in a dictionary, where the key is the file name and the value is the metadata:
# Step 7: Save the metadata to a Jupyter notebook
# 
# Save the metadata dictionary to a Jupyter notebook:
# 
# Here's the complete code:
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
# This code will extract the metadata for all images in the specified directory and store it in a Jupyter 
# notebook named `photos_metadata.ipynb`. You can then use this notebook to view and analyze the metadata for each image.