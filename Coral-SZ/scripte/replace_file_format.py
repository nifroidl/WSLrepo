"""Tool for replacing a specific string inside specific file. Replaces the file format ending in the annotations file from ".png" to ".jpg"
"""
import os, sys
import glob
import shutil


def convertFileFormatString(file_path, export_path, input_file_format, output_file_format, textOutput):

    os.makedirs(export_path, exist_ok=True)

    #Input Parameters
    input_path = file_path
    output_path = export_path
    old_string = input_file_format
    new_string = output_file_format

    file_count = 0

    # convert files
    for file in sorted(glob.glob(f"{input_path}/*.xml")):
        s = open(file).read()
        if old_string not in s:
            textOutput('"{old_string}" not found in {filename}.'.format(**locals()))
        else:
            # copy file to export dir
            filename = os.path.basename(file)
            new_file = os.path.join(output_path, filename)
            shutil.copyfile(file, new_file)

            # replace the old string in copied file
            with open(new_file, 'w') as f:
                textOutput('\tChanging "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
                s = s.replace(old_string, new_string)
                f.write(s)
                file_count+=1
    return 1
