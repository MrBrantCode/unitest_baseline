"""
QUESTION:
Write a function `detect_anomaly(lst, n)` that identifies the index of an element that deviates from a sequence in a list of integers from 1 to n (inclusive) with no repetition, finds the index of the subsequent most suitable substitute, and computes the total number of replacements made. The function should return a dictionary with keys 'anomaly_index', 'replace_with', and 'total_replacements'. If no abnormal element is found, the function should return {'anomaly_index': -1, 'replace_with': -1, 'total_replacements': 0}.
"""

def detect_anomaly(lst, n):
    # a sorted version of lst to compare it with
    sorted_lst = sorted(lst)
    
    anomaly = {'anomaly_index': -1, 'replace_with': -1, 'total_replacements': 0}
    abnormal = False
    
    # go through each element in the list
    for i in range(len(lst)):
        
        # if this is not the expected value for this position
        # that means it's abnormal
        if lst[i] != sorted_lst[i]:
            
            # anomaly index is the place where the abnormality is
            anomaly['anomaly_index'] = i
            
            # the substitute must be the number that is supposed to be in here
            anomaly['replace_with'] = sorted_lst[i]
            
            # increment the total of replacements
            anomaly['total_replacements'] += 1
            
            # replace the anomalous number with the correct one
            lst[i] = sorted_lst[i]
            
            # set abnormal to True to indicate that an abnormality has been found
            abnormal = True
        
        # if an abnormality has been found there can't be another one
        # (given the description says there's at most one)
        if abnormal:
            break
            
    return anomaly