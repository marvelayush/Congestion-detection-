import statistics

def extract_features(rtts):

    mean_rtt = statistics.mean(rtts)

    std_dev = statistics.pstdev(rtts)

    min_rtt = min(rtts)

    elevation = mean_rtt - min_rtt

    return mean_rtt, std_dev, elevation