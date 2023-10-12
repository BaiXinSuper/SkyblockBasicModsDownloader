import requests
import os
from bs4 import BeautifulSoup as bs
# import fake_useragent #use it will make exe very big
# ua=fake_useragent.UserAgent().chrome
import patcher
import github
from tqdm import tqdm
ua = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.2 Safari/530.5"
def main():
    choises = input(
        "[1] Patcher\n[2] Skytils\n[3] Dragon Rooms Mod\n[4] Not Enough Update(NEU)\n[5] Skyblock Addons\n[0] Exit\nYour wanna download: ")
    functions = [{"uname": "Skytils", 'fname': "SkytilsMod", "dname": "Skytils"}, {"uname": "Quantizr", 'fname': "DungeonRoomsMod", "dname": "DungeonRoomsMod"}, {"uname": "Moulberry", 'fname': "NotEnoughUpdatesd", "dname": "NEU"},
                 {"uname": "BiscuitDevelopment", 'fname': "SkyblockAddons", "dname": "SkyblockAddons"}]
    try:
        c = int(choises)
        if 2 <= c <= 5:
            github.main(ua, tqdm, bs, requests,
                        functions[c-2]["uname"], functions[c-2]["fname"], functions[c-2]["dname"])
            main()
        elif c == 1:
            patcher.main(ua, tqdm, bs, requests)
        elif c == 0:
            return 0
        else:
            os.system("cls")
            main()
    except:
        os.system("cls")
        main()
main()
