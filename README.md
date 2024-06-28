<div align="center">
# nonebot-plugin-crash-king

_✨ 自动分析 Minecraft 崩溃报告 ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/MinecCraftCrashCouncil/nonebot-plugin-crash-king.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-crash-king">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-crash-king.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

##  ⚠ 警告

本项目尚处于快速开发阶段！

## 📖 介绍

自动下载群文件内崩溃日志压缩包，并对其中的崩溃日志文件进行分析。此外预设了一套标准崩溃回复模板，可以使用`##`调用。

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-crash-king

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-crash-king
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-orangejuice
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-crash-king
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-orangejuice
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot-plugin-crash-king"]

</details>

## 🎉 .env 配置

暂无

## 🎉 使用

上传群文件即可触发，此外可以使用`##`指令头调用回复模板。

## 特别感谢

- [\<HMCL汉医堂\> Minecraft 报错崩溃交流群](https://qm.qq.com/q/u7TybvR54c)
- [IdeallandEarthDept/nonebot_plugin_statman](https://github.com/IdeallandEarthDept/nonebot_plugin_statman)
