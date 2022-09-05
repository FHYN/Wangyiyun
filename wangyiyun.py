import requests, execjs
import xml.dom.minidom
import csv

cookies = {
    '_ntes_nnid': '10302445a93a7b232e3aeb1987819cb6,1662300265437',
    '_ntes_nuid': '10302445a93a7b232e3aeb1987819cb6',
    'NMTID': '00Of_C22ns4yrRLN0z8jFUivjtU0pAAAAGDCNEkWQ',
    'WEVNSM': '1.0.0',
    'WNMCID': 'umjufj.1662300265690.01.0',
    'WM_TID': 'Q0yLA92qJVJARVQEREaUH1WFtkdYabKf',
    '__snaker__id': 'jCBhA3QPTjdbHMbz',
    'gdxidpyhxdE': '%2B6UUCRXo2hyj2U8XfR2%5CAXS2TTc%5C%2FfpsRRjiZ%2BGijNOU9K7Klfgn1AODd1xy5UAXyB%2B5BxUaIViEc96nGelVzlkka17BPZteRbTMnx7NV%5CSYPiWIXN4aZef%5Ctp%5CQIQ071Qbt9WpXf%5CN2PC7AXhXxO%2FB2ONovb%5CVZX9E%2FCjuVCaNIxfAz%3A1662301205040',
    '_9755xjdesxxd_': '32',
    'YD00000558929251%3AWM_NI': 'Iq26KxayPbuQmL5G2oxCagP5Q0e2CP62QDVhNPv0wMGYPsPJTVneSxaTci7f%2FMkFCa7pHFNUAeZGPmyE%2F0ViQK2Wf8MyFfHsqW196A0gH0f2y7EYc%2FlmHsVesmyyG0baQVk%3D',
    'YD00000558929251%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6ee89f75f8bf09997d842a9a88ba7d45a938f9a82c450f48d8b91fb5c89abab82f32af0fea7c3b92a8baffed7ca74a3a7a083f85baf94fba8b165bc9daf88d33f93f0abd3c25cf6ee9fa5d5648e90bad1f6478587a094d342988aa286d274a38cad8ab66eed93a5a7c26bf5b088a7cd5f83bb96a8d367bb9be1d1d5639395feb8e5348fa78a87cb79b389ffdab54bf4b988d1e53abbe98bbae225b0b38894d56fb1b3b79ac63ca2bf9fb7ea37e2a3',
    'YD00000558929251%3AWM_TID': 'kuQg%2FMSn6FdARFUQEFLQXxDQogLfvLft',
    '__csrf': '74e7528acf19ff8d36c2ace625855a10',
    'MUSIC_U': '8e558cf4c87f55ff043b177dce3a59c865bb4f96c094bc20612d511a9bc2d449993166e004087dd329dbb7f780aa78cc7d2c7836a1d3447774d960d358fbe489d8552e5b8a39aea8a0d2166338885bd7',
    'ntes_kaola_ad': '1',
    '_iuqxldmzr_': '32',
    'JSESSIONID-WYYY': 'zrxzWTW766fT8IgdpVc4x854Qt4w0R8d04zOH8aeGbR3zC69BET3oGT8uXr4Dyd7GB6d7Mq7oJs4b6DxbWIQJZxmoutD%2FZT7J3NgOd0yF10izFCTf1rvIlg1bZc9IIT2CMN%2B9BPzSlEAdvqTGZ1Me4n%2FhSGm5Kbcs%5CeXnzJaBkNMZxpa%3A1662389298928',
    'WM_NI': 'sfehW166bBEhnxUVKl4vb%2Fl69WDvrOe2KYxm%2B9GWIfuHLdLBWhqtu9SSp2df9rlyAZrq5FKT5G5Wy77PE8SfDhOyE1imn1l6Rzs3DVIA1bECgRQ7FFjxs%2FxW4Nbao8xjako%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6ee91f77dacb8a1b2d372948e8fb7c15e879b9a87d444a599f7a6c25f899b8aa5d82af0fea7c3b92ab1baab89d63bf6eaaea3c864aea89bb7ca68f8aaaed0ef3efb898c97f145a7ee85bafb67e9e789b8cc6eb7988485cf4a95b8bf95f833918dc0d3e76efbaea49ac452b2affba7ca60f799fbb8fc3df5908bd9d26e88b8819ac83babb3a2d2ef3e92a6bdd4c75e8b9fff83c849a58e9fd8c54eaaa8bdd0fb5df892ae82ee34bcb6af8cee37e2a3',
}

headers = {
    'authority': 'music.163.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh-SG;q=0.9,zh;q=0.8,zh-TW;q=0.7,en;q=0.6',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ntes_nnid=10302445a93a7b232e3aeb1987819cb6,1662300265437; _ntes_nuid=10302445a93a7b232e3aeb1987819cb6; NMTID=00Of_C22ns4yrRLN0z8jFUivjtU0pAAAAGDCNEkWQ; WEVNSM=1.0.0; WNMCID=umjufj.1662300265690.01.0; WM_TID=Q0yLA92qJVJARVQEREaUH1WFtkdYabKf; __snaker__id=jCBhA3QPTjdbHMbz; gdxidpyhxdE=%2B6UUCRXo2hyj2U8XfR2%5CAXS2TTc%5C%2FfpsRRjiZ%2BGijNOU9K7Klfgn1AODd1xy5UAXyB%2B5BxUaIViEc96nGelVzlkka17BPZteRbTMnx7NV%5CSYPiWIXN4aZef%5Ctp%5CQIQ071Qbt9WpXf%5CN2PC7AXhXxO%2FB2ONovb%5CVZX9E%2FCjuVCaNIxfAz%3A1662301205040; _9755xjdesxxd_=32; YD00000558929251%3AWM_NI=Iq26KxayPbuQmL5G2oxCagP5Q0e2CP62QDVhNPv0wMGYPsPJTVneSxaTci7f%2FMkFCa7pHFNUAeZGPmyE%2F0ViQK2Wf8MyFfHsqW196A0gH0f2y7EYc%2FlmHsVesmyyG0baQVk%3D; YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee89f75f8bf09997d842a9a88ba7d45a938f9a82c450f48d8b91fb5c89abab82f32af0fea7c3b92a8baffed7ca74a3a7a083f85baf94fba8b165bc9daf88d33f93f0abd3c25cf6ee9fa5d5648e90bad1f6478587a094d342988aa286d274a38cad8ab66eed93a5a7c26bf5b088a7cd5f83bb96a8d367bb9be1d1d5639395feb8e5348fa78a87cb79b389ffdab54bf4b988d1e53abbe98bbae225b0b38894d56fb1b3b79ac63ca2bf9fb7ea37e2a3; YD00000558929251%3AWM_TID=kuQg%2FMSn6FdARFUQEFLQXxDQogLfvLft; __csrf=74e7528acf19ff8d36c2ace625855a10; MUSIC_U=8e558cf4c87f55ff043b177dce3a59c865bb4f96c094bc20612d511a9bc2d449993166e004087dd329dbb7f780aa78cc7d2c7836a1d3447774d960d358fbe489d8552e5b8a39aea8a0d2166338885bd7; ntes_kaola_ad=1; _iuqxldmzr_=32; JSESSIONID-WYYY=zrxzWTW766fT8IgdpVc4x854Qt4w0R8d04zOH8aeGbR3zC69BET3oGT8uXr4Dyd7GB6d7Mq7oJs4b6DxbWIQJZxmoutD%2FZT7J3NgOd0yF10izFCTf1rvIlg1bZc9IIT2CMN%2B9BPzSlEAdvqTGZ1Me4n%2FhSGm5Kbcs%5CeXnzJaBkNMZxpa%3A1662389298928; WM_NI=sfehW166bBEhnxUVKl4vb%2Fl69WDvrOe2KYxm%2B9GWIfuHLdLBWhqtu9SSp2df9rlyAZrq5FKT5G5Wy77PE8SfDhOyE1imn1l6Rzs3DVIA1bECgRQ7FFjxs%2FxW4Nbao8xjako%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee91f77dacb8a1b2d372948e8fb7c15e879b9a87d444a599f7a6c25f899b8aa5d82af0fea7c3b92ab1baab89d63bf6eaaea3c864aea89bb7ca68f8aaaed0ef3efb898c97f145a7ee85bafb67e9e789b8cc6eb7988485cf4a95b8bf95f833918dc0d3e76efbaea49ac452b2affba7ca60f799fbb8fc3df5908bd9d26e88b8819ac83babb3a2d2ef3e92a6bdd4c75e8b9fff83c849a58e9fd8c54eaaa8bdd0fb5df892ae82ee34bcb6af8cee37e2a3',
    'dnt': '1',
    'origin': 'https://music.163.com',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

params = {
    'csrf_token': '74e7528acf19ff8d36c2ace625855a10',
}

data = {
    'params': '/Nzbh1eS1Q8p2bTastgARKuGwb1iAnef+iCWlr4rx7cdTL9xDHcflq/GlRfZkUZTRSXIO+V3yWHzGzItcxYN9x8Sjdp1ElUecT8vHu6NSKrVN4XOgUwuukAuqDTOh6RkyAytiLRfuLlJZO36zTMNDt/tLCBium+Vn0gyKTAwIlmLeW1rqY/pC+Bqfl0U6UYIkUHprUEsqP4MHWfyfygnzw==',
    'encSecKey': 'b04c21e9fc777e848d66dacb1e6ad0e8c1a777e8de114bcf9adfad33b4041cfd805564099bda9f05c494231afde9e47fe9720821af9b2e9b17feed6f6fdaf0ec4404a324b1562169c4f1a1b2d58725453904e4762503259acc71d5c46e68efbd96ce9fa2fd6da998075f4adf26725bf9f2af3e2c13c717e3f12379f8e9b3d5c2',
}

with open('./wangyiyun.js', 'r', encoding = 'utf-8') as o:
    jscode = o.read()

dom = xml.dom.minidom.parse('songlist.xml')
root = dom.documentElement
elm = root.getElementsByTagName('li')

notFind = dict()

with open('歌曲.csv', "w", encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    
    csv_writer.writerow(["name", "id", "url"])

    for item in elm:
        vals = item.getElementsByTagName("a")[0]
        id = vals.getAttribute('href').split('id=')[1]
        name = vals.firstChild.data
        d1 = '{{"ids":"[{}]","level":"standard","encodeType":"aac","csrf_token":""}}'.format(id)
        data = execjs.compile(jscode).call('main', d1)
        response = requests.post('https://music.163.com/weapi/song/enhance/player/url/v1', params=params, cookies=cookies, headers=headers, data=data).json()
        url = response['data'][0]['url']
        print('name:{}    id:{}    url:{}'.format(name, id, url))
        csv_writer.writerow([name, id, url])
        if url is None:
            notFind[name] = id     
    f.close()
print(notFind)
    
