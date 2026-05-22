import subprocess

def get_rtt(host):

    result = subprocess.run(
        ["ping", "-n", "1", host],   # Windows ping
        capture_output=True,
        text=True
    )

    for line in result.stdout.split("\n"):

        if "time=" in line:
            try:
                rtt = line.split("time=")[1].split("ms")[0]
                return float(rtt)
            except:
                return None

        elif "time<" in line:  # handles "time<1ms"
            return 1.0

    return None