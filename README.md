
<h1 align="center">Comic Break</h1>

<p align="center">
  <a href="https://waveassist.io/templates/comicbreak-template">
    <img src="https://img.shields.io/badge/Deploy_with-WaveAssist-007F3B" alt="Deploy with WaveAssist" />
  </a>
  <img src="https://img.shields.io/badge/Comic%20Break-Daily%20xkcd%20comic-blue" alt="Comic Break Badge" />
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" />
  </a>
</p>

---

## Overview

Retrieves the current xkcd comic via its JSON API (no key) and emails the comic image with title.

This template runs on [WaveAssist](https://waveassist.io) and automates the process of delivering the latest xkcd comic to your inbox.

---

## One-Click Deploy on WaveAssist (Recommended)

<p>
  <a href="https://waveassist.io/templates/comicbreak-template" target="_blank">
    <img src="https://waveassistapps.s3.us-east-1.amazonaws.com/public/Button.png" alt="Deploy on WaveAssist" width="230" />
  </a>
</p>

Deploy Comic Break instantly on [WaveAssist](https://waveassist.io) — a zero-infrastructure automation platform that handles orchestration, scheduling, secrets, and hosting for you.

> 🔐 You may be prompted to log in or create a free WaveAssist account before continuing.

#### How to Use:

1. Click the button above or go to [waveassist.io/templates/comicbreak-template](https://waveassist.io/templates/comicbreak-template).
2. Just run the starting node:
   * **xkcd_comic_fetcher**: Fetches the latest comic data from the xkcd JSON API.
3. Click **Deploy** to schedule and automate daily comic deliveries to your inbox.

---

## Manual Deployment

Clone this repo and use your preferred scheduler, such as Cron or Airflow.

**Scripts:**
* `xkcd_comic_fetcher.py`
* `xkcd_email_sender.py`

> No external Python requirements (`requirements`) specified. If additional dependencies are needed in your use-case, install with `pip install <package>` as necessary.

---

## Features

* **xkcd_comic_fetcher**: Automatically retrieves the latest xkcd comic via the official JSON API.
* **xkcd_email_sender**: Downloads the comic image and emails it to you.
* **No API Keys Required**: Direct public API access to xkcd.
* **Simple Scheduling**: Easily automate for daily delivery via WaveAssist.

---

Built with ❤️ by the WaveAssist team. Want help or integrations? [Say hello](https://waveassist.io).
