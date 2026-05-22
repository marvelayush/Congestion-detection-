# Congestion Detection System

---

## Overview

This project simulates a small congestion detection pipeline. It continuously checks the network path to a target machine and measures:

- **ICMP RTT** to estimate basic reachability and latency
- **UDP RTT** to check delay under UDP probing
- **TCP RTT** to check response delay over TCP
- **Throughput** using `iperf3` to measure bandwidth

The idea is simple:

- If delay is low and throughput is healthy, the network is likely **normal**
- If delay increases and throughput drops, the network may be **congested**

This makes the project a good example of real-time network performance monitoring.

---

## Features

- ICMP latency measurement
- UDP latency measurement
- TCP latency measurement
- Throughput measurement with `iperf3`
- Congestion state detection
- Live console output
- Graph output for results
- Works in both:
  - **single-laptop testing**
  - **two-laptop demonstration**

---

## What this project does

The project repeatedly:

1. Pings a target laptop and collects RTT samples.
2. Tries UDP and TCP probe measurements as fallback.
3. Smooths RTT values.
4. Extracts features such as mean RTT, standard deviation, and elevation.
5. Predicts congestion using a trained SVM model.
6. Measures throughput using iPerf3.
7. Saves everything into `network_log.csv`.
8. Optionally plots the logs.

---

## Requirements

Install these before running the project:

- Python 3.10+ on Windows
- `pip`
- `matplotlib`
- `numpy`
- `pandas`
- `scikit-learn`
- iPerf3 (`iperf3.exe`)

Install the Python packages with:

```bash
pip install matplotlib numpy pandas scikit-learn
```

---

## iPerf3 setup

Download iPerf3 for Windows, extract it, and keep `iperf3.exe` somewhere easy to find.

You will need the full path to `iperf3.exe` in `throughput.py`.

Example:

```python
r"C:\Users\YourName\Desktop\iperf-3.21-win64\iperf3.exe"
```

---

## Configuration: single-laptop mode

Use this mode when the client and server are on the same laptop.

### `main.py`

Set `targets` to your laptop’s Wi-Fi IP address:

```python
targets = ["<YOUR_LAPTOP_IP>"]
```

Example:

```python
targets = ["192.168.0.3"]
```

### `throughput.py`

Set the iPerf target to localhost:

```python
def measure_throughput(server="127.0.0.1"):
```

And inside the subprocess command, keep:

```python
"-c", "127.0.0.1",
```

### Why this works

- `192.168.0.3` (example) is your real network IP for ping/RTT checks.
- `127.0.0.1` is localhost, so iPerf client connects to iPerf server on the same laptop.

---

## Configuration: two-laptop demo

Use this mode when you want to demonstrate the project across two laptops.

### Laptop A
This is the monitoring laptop. It runs `main.py`.

### Laptop B
This is the server laptop. It runs:

```bash
iperf3.exe -s
```

### `main.py` on Laptop A

Set `targets` to Laptop B’s IP address:

```python
targets = ["<LAPTOP_B_IP>"]
```

Example:

```python
targets = ["192.168.0.10"]
```

### `throughput.py` on Laptop A

Set the iPerf server value to Laptop B’s IP:

```python
def measure_throughput(server="192.168.0.10"):
```

And inside the subprocess command, use:

```python
"-c", "192.168.0.10",
```

### Laptop B terminal command

Run the server on Laptop B:

```bash
iperf3.exe -s
```

If Windows Firewall asks for permission, allow access.

---

## How to run the project

### 1) Extract the ZIP file

Unzip the project folder.

### 2) Open the folder in VS Code

Open the extracted folder in Visual Studio Code.

### 3) Open a terminal

Use VS Code Terminal or CMD/PowerShell.

### 4) Install dependencies

Run:

```bash
pip install matplotlib numpy pandas scikit-learn
```

### 5) Edit the IP values

Update the following files:

- `main.py` → `targets = [...]`
- `throughput.py` → `server="..."`
- `throughput.py` → `"-c", "..."`

Choose either:
- **single-laptop mode**: use `127.0.0.1` in `throughput.py`
- **two-laptop mode**: use Laptop B’s real IP in both files

### 6) Start iPerf3 server

#### Single-laptop mode
Open a second terminal and run:

```bash
iperf3.exe -s
```

or, from the folder that contains `iperf3.exe`:

```bash
.\iperf3.exe -s
```

#### Two-laptop mode
Run the same command on **Laptop B**.

### 7) Run the main project

In the project terminal, run:

```bash
python main.py
```

### 8) Optional: plot the log

After the run creates `network_log.csv`, plot it with:

```bash
python plot_graph.py
```

---

## Commands a user will type

### Install packages

```bash
pip install matplotlib numpy pandas scikit-learn
```

### Start iPerf server

```bash
.\iperf3.exe -s
```

### Run project

```bash
python main.py
```

### Plot results

```bash
python plot_graph.py
```

---

## Expected output

During execution, you should see lines like:

- `ICMP RTT: ...`
- `UDP RTT: ...`
- `TCP RTT: ...`
- `Throughput: ... Mbps`
- `State: NORMAL` or `State: CONGESTED`
- ![Project Demo]()

---

## Project Structure

```text
project-folder/
│
├── main.py
├── throughput.py
├── congestion.py
├── utils.py
├── requirements.txt
├── 6th.png
├── image61.png
└── README.md
