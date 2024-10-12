# English | [中文](https://github.com/tydaytygx/Minecraft-plugins-updater/blob/main/README_CN.md)

# Introduction

This is a tool that automatically downloads the latest Minecraft plugins. You can specify the plugins to download by configuring `config.json`, and the program will automatically get the latest version of the plugin and download it.

## Supported sources

- [x] spigot
- [x] bukkit
- [x] github
- [x] essentialsX

## Usage steps

1. **Configure the `config.json` file**

First, you need to create or modify the `config.json` file.

**spigot**

**Get the resource number of the plugin**
s
You can get it from the plugin url of spigot, for example: 62325
```json
"gsit": "62325"
```

```url
https://www.spigotmc.org/resources/gsit-modern-sit-seat-and-chair-lay-and-crawl-plugin-1-16-1-21-1.62325/
```

**bukkit**

Just fill in the plugin name, for example:
worldedit
```url
https://dev.bukkit.org/projects/worldedit
```

**github**

Just fill in the organization (author)/warehouse name, for example gecolay/GSit

## Optional

1. **Multi-process**

```bash
python3 download_plugins.py
```

2. **Multiple processes**
```bash
python3 download_plugins.py --multiple 5
```
