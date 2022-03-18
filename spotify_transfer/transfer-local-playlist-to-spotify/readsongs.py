#search for songs that end in .mp3 or m4a
#list the songs
#search the songs on spotify

songs = []                                                                                                                                                                                            
with open("spotify_transfer/transfer-local-playlist-to-spotify/songs2.txt", "r") as f:
      line = f.read().split('\n')
      #print(len(line))

      for x in line:
          if x.lower().endswith((".mp3",".m4a")):# look for mp3,m4a files
              songs.append(x) 
              #print(x)
          else:
              pass                
        
print(len(songs))

#print(songs)

    
    
