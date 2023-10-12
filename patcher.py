#https://sk1er.club/mods/patcher
def main(ua,tqdm,bs,requests):
    
    headers={"User-Agent":ua}
    r=requests.get("https://sk1er.club/mods/patcher",headers=headers)
    index=bs(r.text,"html.parser")
    r.close()
    url=''
    for i in index.find_all('a'):
        i=str(i)
        if "/1.8.9/" in i and "https://static.sk1er.club/repo/mods/patcher/" in i:
            url=i
            break
    url=url.split("href=")[1].split(" target=")[0].replace('"','')
    c=requests.get(url, stream=True,headers=headers)
    total_size_in_bytes = int(c.headers.get('content-length', 0))
    block_size = 1024 # 1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open('Patcher.jar', 'wb') as file:
        for data in c.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    print("Download Over ------------- Patcher.jar")