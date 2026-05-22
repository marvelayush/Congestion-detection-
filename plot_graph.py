import pandas as pd
import matplotlib.pyplot as plt

# load CSV log
data = pd.read_csv("network_log.csv")

# convert state values
data["State"] = data["State"].replace({0: "Normal", 1: "Congested"})

plt.figure(figsize=(8,5))

plt.plot(data["Mean RTT"], label="Mean RTT")

plt.title("Network Latency Monitoring")
plt.xlabel("Sample Number")
plt.ylabel("RTT (ms)")
plt.legend()

plt.show()