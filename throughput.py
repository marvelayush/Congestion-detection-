import subprocess
import re

def measure_throughput(server="127.0.0.1"):
    try:
        result = subprocess.run(
            [
                r"C:\Users\ayush\OneDrive\Desktop\iperf-3.21-win64\iperf3.exe",
                "-c", "127.0.0.1",
                "-p", "5201",
                "-t", "3",
                "-P", "4"
            ],
            capture_output=True,
            text=True
        )

        output = result.stdout + result.stderr

        print("DEBUG OUTPUT:\n", output)

        matches = re.findall(r"(\d+\.?\d*)\s+(Mbits/sec|Gbits/sec)", output)

        if matches:
            value, unit = matches[-1]

            value = float(value)

            if unit == "Gbits/sec":
                value *= 1000

            return value

        return None

    except Exception as e:
        print("ERROR:", e)
        return None