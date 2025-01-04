def make_album(artist_name, album_title, songs=None):
    if songs != None:
        album = {'artist': artist_name.title(), 'title': album_title.title(), 'songs': songs}
    else:
        album = {'artist': artist_name.title(), 'title': album_title.title()}    
    return album

print(make_album('system of a down', 'toxicity', 12))
print(make_album('dream theater', 'when dream an day unite'))
print(make_album('gooba', 'gabba'))