import os
import exifread
from IPython.core.display import HTML

# Set the path to the directory containing the photos
photo_dir = '/path/to/photo/directory'

# Create a list to store the metadata for each photo
metadata_list = []

# Loop through each file in the directory
for filename in os.listdir(photo_dir):
    # Check if the file is a JPEG image
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        # Open the file for reading
        with open(os.path.join(photo_dir, filename), 'rb') as f:
            # Read the metadata using exifread
            tags = exifread.process_file(f)
            # Add the metadata to the list
            metadata_list.append(tags)

# Create a new Jupyter notebook cell to display the metadata
display(HTML('<h2>Photo Metadata</h2>'))
display(HTML('<table><tr><th>Filename</th><th>Metadata</th></tr>'))
for i, metadata in enumerate(metadata_list):
    display(HTML('<tr><td>{}</td><td>{}</td></tr>'.format(
        os.listdir(photo_dir)[i], metadata)))
display(HTML('</table>'))