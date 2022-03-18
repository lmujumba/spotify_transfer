import glob,os

path = "/home/lewis/Music/"

songs = []  

for root,dirs,files in os.walk(path):
    for x in files:
          if x.lower().endswith((".mp3",".m4a")):# look for mp3,m4a files
              songs.append(x) 
              #print(x)
          else:
              pass   
print(len(songs))
print(songs)