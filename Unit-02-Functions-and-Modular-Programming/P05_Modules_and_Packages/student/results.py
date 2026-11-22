
# Student Results Module

def calculate_result(*marks):

    total = sum(marks)

    average = total / len(marks) if marks else 0

    highest = max(marks) if marks else 0

    return total, average, highest
