

# 中文 | [ENGLISH](https://github.com/tydaytygx/Minecraft-plugins-updater/blob/main/README.md)

# 简介


这是一个自动下载最新 Minecraft 插件的工具。你可以通过配置 `config.json` 来指定要下载的插件，并且程序会自动获取插件的最新版本并下载。

## 支持的源

- [x] spigot
- [x] bukkit
- [x] github
- [x] essentialsX

## 使用步骤

1. **配置 `config.json` 文件**

   首先，你需要创建或修改 `config.json` 文件。

   **spigot**

    **获取插件的资源号码**
s
   你可以从spigot的插件url中获取，例如：62325
   ```json
   "gsit": "62325"
   ```

   ```url
   https://www.spigotmc.org/resources/gsit-modern-sit-seat-and-chair-lay-and-crawl-plugin-1-16-1-21-1.62325/
   ```

   **bukkit**
   
   填入插件名即可，例如：
   worldedit
   ```url
   https://dev.bukkit.org/projects/worldedit
   ```

   **github**

   填入组织（作者）/仓库名即可，例如 gecolay/GSit
   

   


## 可选项

1. **多进程**

```bash
python3 download_plugins.py
```

2. **多进程**
```bash
python3 download_plugins.py --multiple 5
```



