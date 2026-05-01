# G-TASK
'''
Shunday function tuzingki unga integerlardan iborat array pass bolsin va 
function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
'''


def get_highest_index(array):
    high_number = 0
    high_ind = 0
    for ind, val in enumerate(array):
        if val > high_number:
            high_number = val
            high_ind = ind
    return high_ind


result = get_highest_index([58, 5, 21, 12, 21, 38, 8])
print(result)
