"""
You are the designated 'technology specialist' of a local Sporting Organization
(S.O.). Numerous teams of athletes participate in races organized by the
association. Each time, you receive a string containing the race results for
all participating teams. Here's an example string representing the individual
results of a team of 5 runners:

'01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17'

In this format, each part of the string represents the time taken by a runner
in the format 'h|m|s', where 'h' represents hours, 'm' represents minutes,
and 's' represents seconds. Each result is separated by a comma or a comma
followed by a space.

To evaluate and compare the performance of the teams, you need to calculate
three statistics: range, average, and median.

Range: The range is the difference between the lowest and highest values in a
set of numbers. For example, given the set {4, 6, 9, 3, 7},
the lowest value is 3 and the highest value is 9.
Therefore, the range is calculated as 9 - 3 = 6.

Average: The average, also known as the mean, is obtained by adding up all the
numbers in a set and dividing the sum by the total count of numbers.

Median: The median is the middle number that separates the higher half from the
lower half of a data sample. If the sample size is odd, the median is the
middle value. If the sample size is even, the median is the mean of the two
middle values.

Your task is to calculate these three values and return a string in the
following format:

'Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss'

where 'hh', 'mm', and 'ss' represent two-digit integers
(represented as strings).

Please note:

If a result in seconds has decimals (e.g., ab.xy...), it should be truncated to
'ab'. If the given string is empty, your function should return an empty string
as well.
"""
def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return  f"{hours:02d}|{minutes:02d}|{seconds:02d}"

def stat(race_results):
    """ Your solution here """

    if not race_results:
        return ""

    times = race_results.split(', ')
    total_seconds = []

    # Convert each race result time in to total seconds
    for time in times:
        h, m, s = map(int, time.split('|'))
        total_seconds.append(h * 3600 + m * 60 + s)

    range = max(total_seconds) - min(total_seconds)

    average = sum(total_seconds) // len(total_seconds)

    total_seconds.sort()
    n = len(total_seconds)
    
    if n % 2 == 1:
        median_seconds = total_seconds[n // 2]
    else:
        median_seconds = (total_seconds[n // 2 - 1] + total_seconds[n // 2]) //2

    range_str = format_time(range)
    average_str = format_time(average)
    median_str = format_time(median_seconds)

    return f'Range: {range_str} Average: {average_str} Median: {median_str}'


# Test cases
test_1 = stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17")

assert test_1 == "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34", \
    "❌ Test 1 failed!"
print("✅ Test 1 passed!")

test_2 = stat(
    "02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41")

assert test_2 == "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00", \
    "❌ Test 2 failed!"
print("✅ Test 2 passed!")

test_3 = stat("")

assert test_3 == "", "❌ Test 3 failed!"
print("✅ Test 3 passed!")
