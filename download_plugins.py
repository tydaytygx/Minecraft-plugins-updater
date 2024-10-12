import os
import requests
import json
from multiprocessing import Pool
import argparse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}

# Parse essentialsX
EssentialsX_plugins = {
    "EssentialsX": None,
    "EssentialsX Chat": None,
    "EssentialsX Spawn": None,
}

process_number = None
github_repo = None
bukkit_repo = None
spigot_base_url = None
spigot_repo = None
download_url_list = []
filename_list = []

# Read from config
if os.path.exists("config.json"):
    with open("config.json", "r") as config_file:
        data = json.load(config_file)
        EssentialsX_plugins["EssentialsX"] = data["essentials"]
        github_repo = data["github"]
        bukkit_base_url = data["bukkit_base_url"]
        bukkit_repo = data["bukkit"]
        spigot_base_url = data["spigot_base_url"]
        spigot_repo = data["spigot"]
else:
    with open("config.json", "a"):
        pass
    
if os.path.exists("plugins"):
    pass
else:
    os.mkdir('plugins')


def download_file(url, custom_filename=None):
    # Read name from url
    filename = (
        custom_filename if custom_filename else os.path.basename(url.split("?")[0])
    )

    print(f"Downloading {filename}...")

    # Download with stream
    r = requests.get(url, headers=headers, allow_redirects=True, stream=True)

    if r.status_code == 200:
        with open(r"plugins/" + filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"{filename} downloaded successfully!")
    else:
        print(f"Failed to download {filename}. HTTP status code: {r.status_code}")


def parse_args():
    parser = argparse.ArgumentParser(description="Download arguments.")
    parser.add_argument(
        "--single", action="store_true", help="Use single process for downloading."
    )
    parser.add_argument(
        "--multiple",
        type=int,
        default=None,
        help="Use multiple processes for downloading, provide process number.",
    )
    return parser.parse_args()


# 
if __name__ == "__main__":
    args = parse_args()

    # Download from Github 
    for item in github_repo:
        github_api_url = "https://api.github.com/repos/%s/releases/latest" % item
        response = requests.get(github_api_url, headers=headers)
        if response.status_code == 200:
            release_data = response.json()
            assets = release_data.get("assets", [])
            for asset in assets:
                if asset["name"].endswith(".jar"):
                    jar_file_url = asset["browser_download_url"]
                    download_url_list.append(jar_file_url)
                    filename_list.append(os.path.basename(jar_file_url))
                    break

    # Download from Bukkit
    for item in bukkit_repo:
        bukkit_download_url = bukkit_base_url + item
        filename = item + ".jar"
        download_url_list.append(bukkit_download_url)
        filename_list.append(filename)

    # Download from spigot
    for item in spigot_repo:
        spigot_download_url = spigot_base_url % spigot_repo[item]
        filename = item + ".jar"
        download_url_list.append(spigot_download_url)
        filename_list.append(filename)

    # Single process or multiprocess
    if args.single:
        for i in range(len(download_url_list)):
            download_file(download_url_list[i], filename_list[i])
    elif args.multiple:
        process_number = args.multiple if args.multiple else process_number
        if process_number:
            with Pool(process_number) as p:
                p.starmap(download_file, zip(download_url_list, filename_list))
    else:
        # On default: single process
        for i in range(len(download_url_list)):
            download_file(download_url_list[i], filename_list[i])
