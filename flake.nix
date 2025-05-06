{
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    packwiz2nix = {
      url = "github:snylonue/packwiz2nix";
      inputs = {
        nixpkgs.follows = "nixpkgs";
        flake-utils.follows = "flake-utils";
      };
    };
  };
  outputs = { self, nixpkgs, flake-utils, packwiz2nix, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pack = builtins.fromTOML (builtins.readFile ./pack.toml);
        inherit (packwiz2nix.packages.${system}) buildPackwizModpack;
      in {
        devShells.default =
          pkgs.mkShell { packages = with pkgs; [ packwiz yq ]; };

        packages = {
          curseforge = pkgs.stdenvNoCC.mkDerivation {
            inherit (pack) version;
            name = "GregTech-Odyssey";
            src = ./.;
            buildInputs = with pkgs; [ packwiz ];
            phases = [ "unpackPhase" "buildPhase" "installPhase" ];
            buildPhase = ''
              rm -rf config/ftbquests/quests
              cp -r .github/localization/quests config/ftbquests/quests
              packwiz cf export
            '';
            installPhase = ''
              mkdir $out
              mv "${pack.name}-${pack.version}.zip" $out
            '';
          };

          forge = let
            minecraftVersion = "1.20.1";
            forgeVersion = "47.4.0";
            version = "${minecraftVersion}-${forgeVersion}";
          in pkgs.runCommandNoCC "forge-${version}" {
            inherit version;
            nativeBuildInputs = with pkgs; [ cacert curl jre_headless ];

            outputHashMode = "recursive";
            outputHash = "sha256-EtqyOX9REjT5sCxm2s+dhSzXnIvuFEhdFqlwgVbEugw=";
          } ''
            mkdir -p "$out"

            curl https://maven.minecraftforge.net/net/minecraftforge/forge/${version}/forge-${version}-installer.jar -o ./installer.jar
            java -jar ./installer.jar --installServer "$out"
          '';

          modpack = buildPackwizModpack {
            src = ./.;
            name = "gregtech-odyssey";
            # packwiz may record file metadata that not gets managed by git
            allowMissingFile = true;
          };

          modpack-client = buildPackwizModpack {
            src = ./.;
            name = "gregtech-odyssey";
            # packwiz may record file metadata that not gets managed by git
            allowMissingFile = true;
            side = "client";
          };

          server = let inherit (self.packages.${system}) forge modpack;
          in pkgs.stdenvNoCC.mkDerivation {
            inherit (pack) version;
            pname = "gregtech-odyssey-server";

            dontUnpack = true;
            dontConfigure = true;

            installPhase = ''
              mkdir -p $out

              ln -s ${forge}/* $out
              cp -r ${modpack}/* $out
            '';
          };
        };
      });
}
