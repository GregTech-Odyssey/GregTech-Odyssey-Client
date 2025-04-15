![gregtech_odyssey_title](https://github.com/user-attachments/assets/89f48741-a6ab-4f45-9dd6-e3669fd49cde)

<h1 align="center">
    <a href="https://discord.gg/fASxuRMjtS"><img src="https://discordapp.com/api/guilds/1361351361257672876/widget.png" alt="加入Discord服务器 | Join Discord Server"></a>
    <a href="https://qm.qq.com/q/H4mWY1GfSK"><img src="https://img.shields.io/badge/QQ-加入交流群-12B7F5?logo=qq&logoColor=white" alt="加入QQ群 | Join QQ Group"></a>
</h1>

[中文](README_zh.md)

## Introduction

GregTech-Odyssey is a fully performance optimized tech-oriented GT modpack designed to offer players a diverse and challenging experience based on GregTech Modern. Here's Costom mechanical machines, varaity of useful functional hatches to ultimately boost your machines, magic mods such as Botania, which providing a balanced blend of technology and magic, and also implemented additional blocking modes for ME Pattern Providers, cross-recipe parallelism, and multithreading optimization, give players a comfortable and smooth gaming experience in the late game.

## License

- All content in this series is prohibited for commercial use.
- This modpack is licensed under [Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/).
- The [core mod code](https://github.com/GregTech-Odyssey/GTOCore) (`src/main/java/` portion) is licensed under the [GNU GENERAL PUBLIC LICENSE Version 3](https://www.gnu.org/licenses/gpl-3.0.html).
- Rights to quests (texts) and original textures are reserved. Unauthorized use is prohibited.

## Usage

### Exporting the CurseForge Modpack

1. Install [packwiz](https://github.com/packwiz/packwiz).
2. Clone this repository:
```
git clone https://github.com/GregTech-Odyssey/GregTech-Odyssey.git
```
3. Export with packwiz:
```
packwiz cf export
```

### Downloading Modpacks Built with GitHub Actions

### Download from Release

[Releases](https://github.com/GregTech-Odyssey/GregTech-Odyssey/releases)

The nightly release contains the latest builds.

## Development

See detailed usage at <https://packwiz.infra.link/tutorials/creating/getting-started/>.

### Managing Modpack Files

- Copy files to the desired folder (e.g., `config/ftbquests/quests`).
- Execute `packwiz refresh`.
- Commit changes with Git.

## Develop

### Managing Mods

#### Mods from CurseForge or Modrinth

Install mods with:
```
packwiz curseforge install https://www.curseforge.com/minecraft/mc-mods/<mod id>
packwiz modrinth install https://modrinth.com/mod/<mod id>
```

This generates a `.pw.toml` file in the `mods` folder to record mod information. The `side` field specifies whether the mod is for the client, server, or both (`both, client, server`).

(Optional) After adding CurseForge mods, run `fixup.sh` to generate download links. This requires [yq](https://github.com/mikefarah/yq). The script is sourced from [Misterio77/Modpack](https://github.com/Misterio77/Modpack).

- Update mods with `packwiz update [mod]`.
- To update all mods: `packwiz update --all`.

#### Directly Provided JAR Files

Handle them the same way as managing modpack files.

#### Providing Alternative Download Links

Manually write a `.pw.toml` file with the file name, download URL, and hash.

Example:
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
