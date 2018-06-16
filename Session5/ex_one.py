def dec_list(n):
    dec = 0
    result = [2]

    if n == 0:
        result = []
    
    for i in range(n):
        if i % 2 == 0 and i != 0:
            dec += 0.5
            result.append(result[0] - dec)
        elif i % 2 != 0:
            result.append(-1)

    return result

