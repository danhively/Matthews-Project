import os
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata_from_photos(directory):
    """
    Extracts metadata from photos in the given directory.

    Parameters:
    - directory (str): Path to the directory containing photos.

    Returns:
    - dict: A dictionary containing metadata for each photo.
    """
    metadata_dict = {}
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            filepath = os.path.join(directory, filename)
            image = Image.open(filepath)
            metadata = {}
            for tag, value in image._getexif().items():
                tag_name = TAGS.get(tag, tag)
                metadata[tag_name] = value
            metadata_dict[filename] = metadata
    return metadata_dict
