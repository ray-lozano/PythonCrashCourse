def make_album(artist_name, album_title, songs=None):
    if songs != None or songs == 0:
        album = {'artist': artist_name.title(), 'title': album_title.title(), 'songs': songs}
    else:
        album = {'artist': artist_name.title(), 'title': album_title.title()}    
    return album

while True:
    print("\nPlease enter album info: ")
    a_name = input("Artist name: ")
    if a_name == 'q':
        break

    a_title = input("Album title: ")
    if a_title == 'q':
        break

    song_count = input("Number of songs: ")
    if song_count == 'q':
        break

    if song_count == 0 or song_count == None:
        album = make_album(a_name, a_title)
    else:
        album = make_album(a_name, a_title, song_count)
    print(album)