import os

m4a_path = "歌曲/"  #m4a文件所在文件夹
mp3_path = "mp3/"

m4a_file = os.listdir(m4a_path)
for i, m4a in enumerate(m4a_file):
    org_p = m4a_path + m4a 
    tar_p = mp3_path + m4a[:-4] + ".mp3"
    print(tar_p)
    os.system("C:/Users/86186/Desktop/bin/ffmpeg -i " + '"' + org_p + '" "' + tar_p + '"' )