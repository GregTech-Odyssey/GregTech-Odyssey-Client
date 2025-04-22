
![gregtech_odyssey_title](https://github.com/user-attachments/assets/89f48741-a6ab-4f45-9dd6-e3669fd49cde)

<h1 align="center">
    <a href="https://discord.gg/PxruFSbtCn"><img src="https://discordapp.com/api/guilds/1361351361257672876/widget.png" alt="加入Discord服务器 | Join Discord Server"></a>
    <a href="https://qm.qq.com/q/H4mWY1GfSK"><img src="https://img.shields.io/badge/QQ-加入交流群-12B7F5?logo=qq&logoColor=white" alt="加入QQ群 | Join QQ Group"></a>
</h1>

## 介绍
- GregTech-Odyssey 是一个经过极致性能优化的科技导向的格雷整合包, 致力于在现代格雷的基础上为玩家提供多样的, 有挑战性的体验. 游戏中包含复杂又有趣的各种自定义机制机器，以及能够带来巨大产能提升的的功能仓室。同时也包含了魔法模组, 各种辅助模组和优化模组提升游戏体验. 此整合包所使用的独特Mod - GTOCore不仅包含更多定制化的游戏流程内容, 还实现了例如ME样板供应器的增强阻挡模式, 机器的跨配方并行和多线程优化，以进一步优化游戏体验.

## 协议

- 该系列全部内容禁止商业使用
- 本整合包使用 [Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- [核心模组代码](https://github.com/GregTech-Odyssey/GTOCore)（src/main/java/部分）使用 [GNU GENERAL PUBLIC LICENSE Version 3](https://www.gnu.org/licenses/gpl-3.0.html)
- 任务（文本），原创纹理保留所有权利，未经授权禁止使用

## 使用

### 导出 Curseforge 整合包

- 安装 [packwiz](https://github.com/packwiz/packwiz)
- 克隆该仓库
```
git clone https://github.com/GregTech-Odyssey/GregTech-Odyssey.git
```
- 使用 packwiz 导出
```
packwiz cf export
```

### 下载 github actions 自动构建的整合包

### 从 release 下载

<https://github.com/GregTech-Odyssey/GregTech-Odyssey/releases>

nightly release 是最新的打包

## 开发

详细用法见 <https://packwiz.infra.link/tutorials/creating/getting-started/>

安装 [packwiz](https://github.com/packwiz/packwiz)

### 管理整合包文件

- 将文件复制至所需的文件夹 (如 `config/ftbquests/quests`)
- 执行 `packwiz refresh`
- 用 git 提交更改

### 管理模组

#### CurseForge 或 Modrinth 模组

```
packwiz curseforge install https://www.curseforge.com/minecraft/mc-mods/ex-pattern-provider
packwiz modrinth install https://modrinth.com/mod/appleskin
```

会在 `mods` 文件夹下生成 `.pw.toml` 文件记录 mod 信息，其中 `side` 声明了该 mod 是否应该存在于客户端或服务端，可取值 `both, client, server`

(可选：添加 curseforge 模组后运行 `fixup.sh` 生成下载链接，须安装 [yq](https://github.com/mikefarah/yq)，脚本来自 [Misterio77/Modpack](https://github.com/Misterio77/Modpack))

使用 `packwiz update [mod]` 更新

如更新 `mods/applied-energistics-2.pw.toml`: `packwiz update applied-energistics-2`
更新全部模组: `packwiz update --all`

#### 直接提供 jar

同管理整合包文件

#### 提供其他下载地址

需要手写 .pw.toml 文件，提供文件名，下载地址和 hash

```toml
name = "Flamingo"
filename = "flamingo.jar"
side = "both"

[download]
url = "https://example.com/flamingo.jar"

# A number of tools can generate the hash for you, including 7-zip and sha256sum
# packwiz supports a number of hashes, including sha256, sha512, sha1 and md5
hash-format = "sha256"
hash = "b22d1d8fe5752533954028172c9bf3ac01b57f40c82946a3e7b1eaff389e2b87"
```
