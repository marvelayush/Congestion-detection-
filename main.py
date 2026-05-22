import time
import matplotlib.pyplot as plt   # 🔥 NEW

from probe import get_rtt
from udp_probe import udp_probe
from tcp_probe import tcp_probe

from features import extract_features
from svm_model import detect_congestion

from adaptive_probe import adaptive_probe_rate
from traffic_control import throttle_traffic

from filter import moving_average
from predictor import predict_congestion

from throughput import measure_throughput
from logger import log_data


# 🔥 IMPORTANT: Use Laptop B IP
targets = [
    "192.168.0.3"
]

probe_interval = 1
sending_rate = 1

# 🔥 NEW: store data for graph
rtt_history = []
throughput_history = []


try:
    while True:

        print("\n========= Monitoring Cycle =========")

        for host in targets:

            print("\nTarget:", host)
            print("Monitoring path: Laptop A →", host)

            rtts = []

            # collect RTT samples
            for i in range(5):

                icmp_rtt = get_rtt(host)
                udp_rtt = udp_probe(host)
                tcp_rtt = tcp_probe(host)

                print("ICMP RTT:", icmp_rtt)
                print("UDP RTT:", udp_rtt)
                print("TCP RTT:", tcp_rtt)

                # prioritize ICMP
                if icmp_rtt:
                    rtt = icmp_rtt
                elif udp_rtt:
                    rtt = udp_rtt
                elif tcp_rtt:
                    rtt = tcp_rtt
                else:
                    rtt = None

                if rtt:
                    rtts.append(rtt)

                time.sleep(probe_interval)

            if len(rtts) == 0:
                print("No RTT samples collected")
                continue

            # smooth RTT
            rtts = moving_average(rtts)

            print("All RTT samples:", rtts)

            # extract features
            mean_rtt, std_dev, elevation = extract_features(rtts)

            print("Mean RTT:", mean_rtt)
            print("Std Dev:", std_dev)
            print("Latency Elevation:", elevation)

            # SVM detection
            state = detect_congestion(mean_rtt, std_dev, elevation)

            if state == 1:
                print("Network State: CONGESTED")
                congested = True
            else:
                print("Network State: NORMAL")
                congested = False

            # prediction
            if predict_congestion(rtts):
                print("⚠ Congestion trend detected")

            # throughput
            throughput = measure_throughput("192.168.0.130")

            print("Throughput:", throughput, "Mbps")

            # 🔥 NEW: SAVE DATA
            rtt_history.append(mean_rtt)
            throughput_history.append(throughput if throughput else 0)

            # log
            log_data(mean_rtt, std_dev, elevation, state, throughput)

            # adaptive control
            probe_interval = adaptive_probe_rate(congested, probe_interval)
            sending_rate = throttle_traffic(sending_rate, congested)

            print("Probe interval:", probe_interval)
            print("Sending rate:", sending_rate)

        print("\n--------------------------------------")


# 🔥 WHEN YOU PRESS CTRL + C → GRAPH WILL SHOW
except KeyboardInterrupt:
    print("\n\nStopped! Showing graph...")

    time_axis = list(range(len(rtt_history)))

    plt.figure()

    plt.plot(time_axis, rtt_history, 'r-o', label="RTT (ms)")
    plt.plot(time_axis, throughput_history, 'b-o', label="Throughput (Mbps)")

    plt.xlabel("Time (cycles)")
    plt.ylabel("Value")
    plt.title("RTT vs Throughput")

    plt.legend()
    plt.grid()

    plt.show()