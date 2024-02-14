
  <div align="center">
  <h1 align="center">Youtube Downloader</h1>
  <h3>Codebase for the Youtube Downloader platform</h3>
  <h3>◦ Developed with the software and tools below.</h3>
  <p align="center"><img src="https://img.shields.io/badge/-Python-004E89?logo=Python&style=flat-square" alt='Python\' />
<img src="https://via.placeholder.com/1/0000/00000000" alt="spacer" /><img src="https://img.shields.io/badge/-PyInstaller-004E89?logo=PyInstaller&style=flat-square" alt='PyInstaller\' />
<img src="https://via.placeholder.com/1/0000/00000000" alt="spacer" /><img src="https://img.shields.io/badge/-YouTube%20dl-004E89?logo=YouTube%20dl&style=flat-square" alt='YouTube-dl\' />
<img src="https://via.placeholder.com/1/0000/00000000" alt="spacer" /><img src="https://img.shields.io/badge/-FFmpeg-004E89?logo=FFmpeg&style=flat-square" alt='FFmpeg\' />
<img src="https://via.placeholder.com/1/0000/00000000" alt="spacer" /><img src="https://img.shields.io/badge/-OpenCV-004E89?logo=OpenCV&style=flat-square" alt='OpenCV\' />
<img src="https://via.placeholder.com/1/0000/00000000" alt="spacer" /><img src="https://img.shields.io/badge/-TensorFlow-004E89?logo=TensorFlow&style=flat-square" alt='TensorFlow"' />
<img src="https://via.placeholder.com/1/0000/00000000" alt="spacer" />
  </p>
  </div>
  
  ---
  ## 📚 Table of Contents
  - [📚 Table of Contents](#-table-of-contents)
  - [🔍 Overview](#-overview)
  - [🌟 Features](#-features)
  - [📁 Repository Structure](#-repository-structure)
  - [💻 Code Summary](#-code-summary)
  - [🚀 Getting Started](#-getting-started)
  
  ---
  
  
  ## 🔍 Overview

 The project consists of a Python script named main.py and a specification file named main.spec that defines the behavior of the script. Additionally, there is a separate specification file named youtube-downloader.spec that defines the behavior of a YouTube video downloader module used by the script.

---

## 🌟 Features

 main.py, main.spec, youtube-downloader.spec

---

## 📁 Repository Structure

```sh
├── main.py
├── main.spec
├── youtube-downloader.spec

```

---

## 💻 Code Summary

<details><summary>Root</summary>

| File | Summary |
| ---- | ------- |
| main.py |  The code is a Python script that allows the user to download videos from a YouTube channel by providing a search query, retrieving the channel ID, and then downloading the video URLs from the XML feed of the channel. The script then uses Pytube to download the highest resolution video from each URL to a specified file path. |

</details>

---

## 🚀 Getting Started

 To get started with this project, follow these steps:<br>
1. Install the necessary dependencies by running `pip install -r requirements.txt` in your terminal.
2. Run the script by executing `python main.py` in your terminal.
3. Follow the prompts to enter the URL of the YouTube video you want to download and the desired output file name.
4. The script will then download the video and save it to the specified output file.

Note: This guide assumes that you have Python installed on your system and that you are comfortable using the terminal or command prompt. If you are new to Python or have any questions about the process, please refer to the documentation for the `youtube-downloader` module or seek help from a more experienced developer.

---

Generated with ❤️ by [ReadMeAI](https://www.readmeai.co/).
