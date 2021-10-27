a = [2.5, -0.5, -0.5, -0.5, 65.5, -33.5, -1.0, -0.6499999999999999, 1.5, 0.0, -3.5, 0.35, 16.0, 41.0, 49.5, -18.5, 56.5, 0.30000000000000004, -20.5, 1.5, -0.5, 130.0, -2.55, 0.5, -0.5, 41.0, -0.5, -0.5, 7.5, -11.0, -22.0, -0.5, -4.5, -0.5, 34.0, 38.5, -1.0, 0.5, -0.5, -12.0, 0.5, 1.5, 31.0]
b = [[1.0, 0.0], [0.0, 17.0], [0.0, 1.0], [1.0, 0.0], [1.0, 0.0], [0.0, 3.0], [1.0, 0.0], [0.0, 1.0], [3.0, 0.0], [3.0, 0.0], [0.0, 4.0], [13.0, 0.0], [0.0, 2.0], [3.0, 0.0], [0.0, 1.0], [4.0, 0.0], [41.0, 0.0], [0.0, 2.0], [8.0, 0.0], [1.0, 0.0], [0.0, 3.0], [1.0, 0.0], [0.0, 3.0], [1.0, 0.0], [0.0, 1.0], [0.0, 58.0], [1.0, 0.0], [4.0, 0.0], [0.0, 2.0], [0.0, 7.0], [1.0, 0.0], [0.0, 3.0], [0.0, 1.0], [3.0, 0.0], [0.0, 12.0], [3.0, 0.0], [0.0, 1.0], [0.0, 4.0], [1.0, 0.0], [0.0, 5.0], [4.0, 0.0], [0.0, 1.0], [0.0, 1.0], [9.0, 0.0]]


def predict_class(conditions, result):
    if conditions[0] <= 0:
        if conditions[1] <= 0:
            if conditions[2] <= 0:
                if conditions[3] <= 0:
                    if conditions[4] <= 0:
                        return result[0].index(max(result[0]))
                    else:  # condition is false
                        if conditions[5] <= 0:
                            return result[1].index(max(result[1]))
                        else:  # condition is false
                            if conditions[6] <= 0:
                                return result[2].index(max(result[2]))
                            else:  # condition is false
                                return result[3].index(max(result[3]))
                else:  # condition is false
                    if conditions[7] <= 0:
                        if conditions[8] <= 0:
                            if conditions[9] <= 0:
                                return result[4].index(max(result[4]))
                            else:  # condition is false
                                if conditions[10] <= 0:
                                    return result[5].index(max(result[5]))
                                else:  # condition is false
                                    return result[6].index(max(result[6]))
                        else:  # condition is false
                            return result[7].index(max(result[7]))
                    else:  # condition is false
                        return result[8].index(max(result[8]))
            else:  # condition is false
                if conditions[11] <= 0:
                    if conditions[12] <= 0:
                        return result[9].index(max(result[9]))
                    else:  # condition is false
                        return result[10].index(max(result[10]))
                else:  # condition is false
                    return result[11].index(max(result[11]))
        else:  # condition is false
            if conditions[13] <= 0:
                if conditions[14] <= 0:
                    return result[12].index(max(result[12]))
                else:  # condition is false
                    return result[13].index(max(result[13]))
            else:  # condition is false
                if conditions[15] <= 0:
                    if conditions[16] <= 0:
                        if conditions[17] <= 0:
                            return result[14].index(max(result[14]))
                        else:  # condition is false
                            return result[15].index(max(result[15]))
                    else:  # condition is false
                        return result[16].index(max(result[16]))
                else:  # condition is false
                    if conditions[18] <= 0:
                        return result[17].index(max(result[17]))
                    else:  # condition is false
                        return result[18].index(max(result[18]))
    else:  # condition is false
        if conditions[19] <= 0:
            if conditions[20] <= 0:
                if conditions[21] <= 0:
                    if conditions[22] <= 0:
                        return result[19].index(max(result[19]))
                    else:  # condition is false
                        if conditions[23] <= 0:
                            if conditions[24] <= 0:
                                if conditions[25] <= 0:
                                    return result[20].index(max(result[20]))
                                else:  # condition is false
                                    if conditions[26] <= 0:
                                        return result[21].index(max(result[21]))
                                    else:  # condition is false
                                        return result[22].index(max(result[22]))
                            else:  # condition is false
                                return result[23].index(max(result[23]))
                        else:  # condition is false
                            if conditions[27] <= 0:
                                return result[24].index(max(result[24]))
                            else:  # condition is false
                                return result[25].index(max(result[25]))
                else:  # condition is false
                    return result[26].index(max(result[26]))
            else:  # condition is false
                if conditions[28] <= 0:
                    if conditions[29] <= 0:
                        return result[27].index(max(result[27]))
                    else:  # condition is false
                        return result[28].index(max(result[28]))
                else:  # condition is false
                    if conditions[30] <= 0:
                        return result[29].index(max(result[29]))
                    else:  # condition is false
                        return result[30].index(max(result[30]))
        else:  # condition is false
            if conditions[31] <= 0:
                if conditions[32] <= 0:
                    if conditions[33] <= 0:
                        return result[31].index(max(result[31]))
                    else:  # condition is false
                        if conditions[34] <= 0:
                            return result[32].index(max(result[32]))
                        else:  # condition is false
                            return result[33].index(max(result[33]))
                else:  # condition is false
                    return result[34].index(max(result[34]))
            else:  # condition is false
                if conditions[35] <= 0:
                    if conditions[36] <= 0:
                        if conditions[37] <= 0:
                            if conditions[38] <= 0:
                                if conditions[39] <= 0:
                                    return result[35].index(max(result[35]))
                                else:  # condition is false
                                    return result[36].index(max(result[36]))
                            else:  # condition is false
                                if conditions[40] <= 0:
                                    return result[37].index(max(result[37]))
                                else:  # condition is false
                                    return result[38].index(max(result[38]))
                        else:  # condition is false
                            return result[39].index(max(result[39]))
                    else:  # condition is false
                        return result[40].index(max(result[40]))
                else:  # condition is false
                    if conditions[41] <= 0:
                        if conditions[42] <= 0:
                            return result[41].index(max(result[41]))
                        else:  # condition is false
                            return result[42].index(max(result[42]))
                    else:  # condition is false
                        return result[43].index(max(result[43]))


print(predict_class(a, b))
