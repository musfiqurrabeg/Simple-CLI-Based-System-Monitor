# Simple-CLI-Based-System-Monitor

**Never miss a beat! Keep a watchful eye on your system's vital signs with this sleek, simple, and powerful performance logger.**

![System Monitor in Action](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&pause=1000&color=3670F7&center=true&vCenter=true&width=550&lines=Logging+CPU+and+Memory...;Timestamp%3A+2023-10-27+10%3A30%3A05;CPU%3A+12.5%25+%7C+Memory%3A+45.8%25;New+data+logged+successfully!)

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/dependencies-psutil-brightgreen.svg" alt="Dependencies">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey.svg" alt="License">
  <img src="https://img.shields.io/badge/status-active-success.svg" alt="Status">
</p>

---

## 🤔 What Does It Do?

System Pulse Monitor is a lightweight Python script that elegantly tracks and records your computer's performance over time. It captures the two most critical metrics:

* 🧠 **CPU Usage (%)**: Know how hard your processor is working.
* 💾 **Memory Usage (%)**: Keep tabs on your RAM consumption.

All data is neatly logged into a clean `.csv` file, timestamped and ready for analysis. Wondering why your machine slowed down last Tuesday at 4:17 PM? Now you can find out!

---

## ✨ Why You Need This

* **Diagnose Performance Issues**: Pinpoint exactly when and why your system is lagging.
* **Resource Planning**: Analyze usage trends to decide if it's time for a hardware upgrade.
* **Application Impact Analysis**: See how a new application or process affects your system's resources.
* **Peace of Mind**: Sleep better at night knowing you have a detailed log of your system's health.
* **It Just Looks Cool**: Impress your friends with a live-updating terminal of your system's pulse!

---

## 🌟 Features

* ✅ **Real-time Monitoring**: See live CPU and Memory stats printed directly to your terminal.
* ✅ **CSV Logging**: Automatically saves historical data to `system_performance_log.csv`.
* ✅ **Lightweight & Efficient**: Uses the `psutil` library for minimal performance overhead.
* ✅ **Easy to Use**: Get started with just two commands.
* ✅ **Customizable**: Easily change the logging interval to suit your needs.
* ✅ **Cross-Platform**: Runs anywhere Python and `psutil` are supported (Windows, macOS, Linux).

---

## 🛠️ Installation & Setup

Getting started is as easy as 1-2-3.

**1. Clone the Repository:**

```bash
git clone https://github.com/musfiqurrabeg/Simple-CLI-Based-System-Monitor.git
```

2. Install the Required Dependency:

The script relies on the amazing psutil library. Install it using pip:
```bash
pip install psutil
```
🏃‍♀️ How to Use
Simply run the Python script from your terminal:
```bash
python system_monitor.py
```

You'll immediately see the monitor come to life!

```bash
--- System Performance Monitor ---
Logging CPU and memory usage every 5 seconds.
Data will be saved to 'system_performance_log.csv'.
Press Ctrl+C to stop the script.
Log file 'system_performance_log.csv' created with headers.
2023-10-27 10:30:05 - CPU: 12.5% | Memory: 45.8%
2023-10-27 10:30:10 - CPU: 25.1% | Memory: 46.2%
2023-10-27 10:30:15 - CPU: 18.9% | Memory: 46.1%
```

To stop the monitor, press Ctrl+C. Your log file will be waiting for you.

📄 Log File Output
The generated system_performance_log.csv file will look like this, perfect for importing into Excel, Google Sheets, or a data analysis script.


⚙️ Customization
Want to log more or less frequently? It's easy!

Open sys_monitor.py and change the LOG_INTERVAL_SECONDS variable:

# --- Configuration ---
LOG_INTERVAL_SECONDS = 2  # Change this value (in seconds)

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
