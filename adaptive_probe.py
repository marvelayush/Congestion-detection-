def adaptive_probe_rate(is_congested, current_interval):

    if is_congested:
        # increase monitoring frequency
        return max(1, current_interval / 2)

    else:
        # reduce monitoring frequency
        return min(5, current_interval * 1.5)