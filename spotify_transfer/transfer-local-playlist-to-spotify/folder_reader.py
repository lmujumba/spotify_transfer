import os

def scan_folder(parent):
    # iterate over all the files in directory 'parent'

    for file_name in os.listdir(parent):
        
        if file_name.endswith((".mp3",".m4a")):
            # if it's a mp3 file, print its name (or do whatever you want)
            print(file_name)                                                                                                                                                                                                                                                            
    
            
        else:
            current_path = "".join((parent, "/", file_name))

            if os.path.isdir(current_path):
                # if we're checking a sub-directory, recursively call this method
                scan_folder(current_path)
        

scan_folder("/home/lewis/Music/MP3")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             