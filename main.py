import requests
import subprocess
import shlex
import time
import addict
import shutil

REDDIT_URL = 'https://www.reddit.com/r/photoshopbattles/top.json?sort=top&t=hour&limit=1'  # noqa
INTERVAL = 60 * 60  # 1h


def save_image(url, img):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(img, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
            pass
        pass
    pass


def change_wallpaper():
    subprocess.call(
        shlex.split(
            'gsettings set org.gnome.desktop.background picture-uri file:///tmp/PSBATTLE_TOPIMG'  # noqa
        ))
    pass


def main():
    while True:
        rj = requests.get(REDDIT_URL).json()
        rj = addict.Dict(rj)
        obj = rj.data.children[0]
        if obj.kind != 't3':
            continue
        save_image(obj.data.url, '/tmp/PSBATTLE_TOPIMG')
        change_wallpaper()
        time.sleep(INTERVAL)
        pass

    pass


if __name__ == '__main__':
    main()
