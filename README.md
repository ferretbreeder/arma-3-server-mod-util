# Arma 3 Server/Client Mod Synchronizer
The idea for this program is that it takes two directories, a local mod directory (probably your Steam Workshop folder)
and a remote directory (the mod folder on your Arma 3 server), and makes sure the mods specified by you are the same
version in both places.

An issue I run into hosting an Arma server on my own hardware is mod version incompatibility when mods update on my 
gaming machine and not my server automatically. There are other utilities that do something similar to what I'm attempting
to do with this one, but I figured that I can turn this issue into a learning opportunity!

It's written in Python because that's what I know (well, know more than anything else, anyway), but I could see
implementing it into another language someday.

This is still very much in beta, so use at your own risk!

## How to use
**NOTE**: This program overwrites folders in your destination mod folder without any sort of backup. 
I haven't done extensive testing to see if this will destroy any saved games or have other unintended consquences, 
but in my experience, manually copying these mod folders over to my server has not created any issues for me.

In its current state the setup is fairly exact, but not difficult. 

1. Make sure you've got python-dotenv installed. 
2. In the .env file included in the repo, replace the file paths with the file locations on your own machines. 
"local_path" is the mod folder on your machine ({Drive}:\Steam\steamapps\workshop\content\107410 on Windows) and 
"server_path" is the mod folder on the machine hosting your server
   1. IMPORTANT: For the time being, this program only supports Windows-style file names. I get around this by mounting
   my Linux server to my Windows machine via SMB and assigning it a Windows drive letter, but if your setup is different,
   that is something to keep in mind
3. Edit the file "modlist.csv" included in this repo to include the list of mods you want to keep up-to-date. This file
must stick to this formatting for this program to work. The names in column 1 on the left are the names of the mods in
on my local machine in the Steam mods folder (in other words, the mods that update automatically) and the names in column 2
on the right are the mod folders on my server (where the updated mods need to be copied to). In this case, the destination
mod folders are named following the convention that should be used for Linux Arma 3 servers. This is the example modlist
I've included:

<table>
  <tr>
    <td>463939057</td>
    <td>@ace</td>
  </tr>
  <tr>
    <td>1355571744</td>
    <td>@addtl-zeus-things</td>
  </tr>
  <tr>
    <td>2867537125</td>
    <td>@antistasi</td>
  </tr>
  <tr>
    <td>1673456286</td>
    <td>@cb</td>
  </tr>
  <tr>
    <td>450814997</td>
    <td>@cba-a3</td>
  </tr>
  <tr>
    <td>497661914</td>
    <td>@cup-units</td>
  </tr>
  <tr>
    <td>541888371</td>
    <td>@cup-vehicles</td>
  </tr>
  <tr>
    <td>497660133</td>
    <td>@cup-weapons</td>
  </tr>
  <tr>
    <td>843425103</td>
    <td>@rhsafrf</td>
  </tr>
  <tr>
    <td>843593391</td>
    <td>@rhsgref</td>
  </tr>
  <tr>
    <td>843632231</td>
    <td>@rhssaf</td>
  </tr>
  <tr>
    <td>843577117</td>
    <td>@rhsusaf</td>
  </tr>
  <tr>
    <td>1779063631</td>
    <td>@zeus-enhanced</td>
  </tr>
</table>

4. Once all of that is configured, navigate to the repo folder and run mod-copy.py from the command line. Depending on
the file sizes of the mods being copied, it could take some time.

## Planned features
At its core, this is a pretty simple project trying to solve a pretty simple problem, so the feature set will likely
stay pretty small. But who knows what the future holds! For now, this is what I'm going for:

- Compares mod files quickly and accurately to determine what needs to be copied to the server mod directory
- Simple GUI to keep users from having to use the command line if they are not comfortable with that
- Requires minimal intervention on the part of the user aside from specifying the two directories and a list of mods
  - I don't hate my current solution for this, but it might not be the most user-friendly so it could change at some point

## Current limitations
The one glaring issue I see right now is that all of the file paths used in this program are Windows-style file paths,
meaning that copying from one Linux system to another does not work and vice versa. This is not an issue in my environment because
I play on a Windows PC and copy mod files to my Linux server mounted via SMB, but it is something that I will need to
address in the future.

## Contribution guidlines
I am still such a novice programmer, so I welcome basically any interaction with this project that could help me learn.
Because of that, I have very few guidelines for contributing to the project. If you want to help or have an idea for 
an improvement, jump in and let me know! Just don't be a dick and we should be good.

Anyway, thanks for reading! Feel free to reach out if you have any questions or want to contribute.