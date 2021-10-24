<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">IOTA Wiki Bot</h3>
  <p align="center">
    Discord bot for the <a href="https://wiki.iota.org">IOTA Wiki</a>
    <br />
    <br />
    <a href="https://github.com/iota-community/iota-wiki-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/iota-community/iota-wiki-bot/issuess">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This is a Discord bot for the IOTA Wiki. It's currently used for replacing the old links and for requesting the introduction page for a certain IOTA documentation.

<!-- GETTING STARTED -->
## Getting Started

This section explains how to install and configure the bot.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/iota-community/iota-wiki-bot.git
   ```
2. Go into the repo and build an executable with PyInstaller
   ```sh
   cd iota-wiki-bot
   pyinstaller --onefile bot.py
   ```
  
You can find the executable in the `dist/` folder.

### Configuration

First, create a `.env` file with the following content:
```
DISCORD_TOKEN={DISCORD_TOKEN}
```
Where you replace `{DISCORD_TOKEN}` with the actual token of your server.  
The bot can be configured through a `config.json` file. You can have a look at the [config.json](./config.json) in this repo for an example.

<!-- USAGE EXAMPLES -->
## Usage

If the bots detects an old link, he will add a message with the correct wiki link.  
You can also request a documentation link from the bot by mentioning  him a message and 
adding the topic you are interested in, for example `@IOTA-Wiki-Bot ISCP`

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/iota-community/iota-wiki-bot.svg?style=for-the-badge
[contributors-url]: https://github.com/iota-community/iota-wiki-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/iota-community/iota-wiki-bot.svg?style=for-the-badge
[forks-url]: https://github.com/iota-community/iota-wiki-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/iota-community/iota-wiki-bot.svg?style=for-the-badge
[stars-url]: https://github.com/iota-community/iota-wiki-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/iota-community/iota-wiki-bot.svg?style=for-the-badge
[issues-url]: https://github.com/iota-community/iota-wiki-bot/issues
[license-shield]: https://img.shields.io/github/license/iota-community/iota-wiki-bot.svg?style=for-the-badge
[license-url]: https://github.com/iota-community/iota-wiki-bot/blob/master/LICENSE
