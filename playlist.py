# playlist = dict(["song","album","artist","date","length"], None)

playlist = {
    'title':'patagonia',
    'author':'david',
    'songs':[
        {'title':'song1','artist':['david'], 'duration':2.5},
        {'title':'song2','artist':['david','lindsay'], 'duration':5.5},
        {'title':'song3','artist':['steve'], 'duration':12.5}
    ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)