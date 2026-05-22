def throttle_traffic(current_rate, congested):

    if congested:
        # reduce traffic rate
        return max(current_rate * 0.6, 0.1)

    else:
        # increase traffic slowly
        return min(current_rate * 1.1, 10)