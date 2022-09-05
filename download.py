import csv, os, requests
if not os.path.exists('歌曲'):
    os.mkdir('歌曲')

def get_songs_by_url(folder_path, name, url):
    file = folder_path + '/' + name + '.mp4'  # 保存本地的路径
    song = requests.get(url)  #根据文件的大小，这一步为主要耗时步骤
    with open(file, "wb") as code:
        code.write(song.content)
    print('-' * 20)
    print('歌曲:{} 下载完毕。'.format(name))

with open('歌曲.csv', "r", encoding="utf-8", newline="") as f:
    csv_reader = csv.reader(f)
    for i, (name, id, url) in enumerate(csv_reader):
        if i == 0:
            continue
        if url is not '':
            get_songs_by_url('歌曲', name, url)
        else:
            print('歌曲:{} 下载失败！缺少正确url'.format(name))
    f.close()

