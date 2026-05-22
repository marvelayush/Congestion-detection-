def predict_congestion(rtts):

    if len(rtts) < 5:
        return False

    recent = rtts[-5:]

    trend = recent[-1] - recent[0]

    if trend > 20:
        return True

    return False