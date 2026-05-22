import csv
import os
import time

FILE_NAME = "network_log.csv"

def log_data(mean_rtt, std_dev, elevation, state, throughput):

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Time",
                "Mean RTT",
                "Std Dev",
                "Elevation",
                "State",
                "Throughput"
            ])

        writer.writerow([
            time.ctime(),
            mean_rtt,
            std_dev,
            elevation,
            state,
            throughput
        ])