# Arma 3 Server/Client Mod Synchronizer
The idea for this program is that it takes two directories, a local mod directory (probably your Steam Workshop folder)
and a remote directory (the mod folder on your Arma 3 server), and makes sure the mods specified by you are the same
version in both places.

An issue I run into hosting an Arma server on my own hardware is mod version incompatibility when mods update on my 
gaming machine and not my server automatically. There are other utilities that do something similar to what I'm attempting
to do with this one, but I figured that I can turn this issue into a learning opportunity!

It's written in Python because that's what I know (well, know more than anything else, anyway), but I could see
implementing it into another language someday.

## How to use
Currently, it's not usable so there isn't much to write here :) But I intend to release a Windows binary at the very
least, with a Linux binary coming afterwards hopefully (if I can learn how to compile a Linux binary, that is). My rough
idea for the code makes me think it will be cross-platform by nature, but we'll see if that actually ends up happening.

My current plan is for the .env file to be populated with the both the local and remote mod directory file paths and for
the mods themselves to be read from a CSV file. Once those are configured, the user should have to just run the program.

## Planned features
At its core, this is a pretty simple project trying to solve a pretty simple problem, so the feature set will likely
stay pretty small. But who knows what the future holds! For now, this is what I'm going for:

- Compares mod files quickly and accurately to determine what needs to be copied to the server mod directory
- Simple GUI to keep users from having to use the command line if they are not comfortable with that
- Requires minimal intervention on the part of the user aside from specifying the two directories and a list of mods
  - I'm not sure if I want the folder paths to be specified via GUI or in the mod list itself.

## Current limitations
The one glaring issue I see right now is that all of the file paths used in this program are Windows-style file paths,
meaning that copying from a from Linux system to another does not work. This is not an issue in my environment because
I play on a Windows PC and copy mod files to my Linux server mounted via SMB, but it is something that I will need to
address in the future.

## Contribution guidlines
I am still such a novice programmer, so I welcome basically any interaction with this project that could help me learn.
Because of that, I have very few guidelines for contributing to the project. If you want to help or have an idea for 
an improvement, jump in and let me know! Just don't be a dick and we should be good.

Anyway, thanks for reading! Feel free to reach out if you have any questions or want to contribute.