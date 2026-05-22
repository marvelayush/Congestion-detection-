def moving_average(data, window=3):

    if len(data) < window:
        return data

    smoothed = []

    for i in range(len(data)):
        start = max(0, i - window + 1)
        subset = data[start:i+1]
        smoothed.append(sum(subset) / len(subset))

    return smoothed