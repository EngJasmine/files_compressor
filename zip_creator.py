import zipfile
import pathlib


def compress(file_path,dest_dir):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path,'w') as archive:

        for filepath in file_path:
            filepath = pathlib.Path(filepath)
            archive.write(filepath,arcname=filepath.name)


