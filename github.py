def get_download_url(uname, fname, version, bs, requests):
    url = f"https://github.com/{uname}/{fname}/releases/expanded_assets/{version}"
    r = requests.get(url, verify=False)
    index = bs(r.text, "lxml")
    r.close()
    links = index.find_all('a')
    for i in links:
        if "/download/" in i['href']:
            return str(i['href'])


def main(ua, tqdm, bs, requests, uname, fname, dname):
    headers = {"User-Agent": ua}
    url = f"https://github.com/{uname}/{fname}/tags"
    r = requests.get(url, verify=False)
    index = bs(r.text, "html.parser")
    r.close()
    links = index.find_all('a')
    version = None
    for i in links:
        if f"/{uname}/{fname}/releases/tag/" in i['href']:
            version = str(i['href']).split('/')[-1]
            break

    download_url = "https://github.com" + \
        get_download_url(uname, fname, version, bs, requests)
    c = requests.get(download_url, stream=True, headers=headers, verify=False)
    total_size_in_bytes = int(c.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(f'{dname}.jar', 'wb') as file:
        for data in c.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    print(f"Download Over ------------- {dname}.jar")
