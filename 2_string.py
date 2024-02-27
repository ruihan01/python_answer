def replace_duplicate_chars(input_str, k):
    result = list(input_str)
    last_seen = {}

    for i, char in enumerate(input_str):
        if char in last_seen and i - last_seen[char] <= k:
            result[i] = '-'
        last_seen[char] = i

    return ''.join(result)

# 测试
input_str = "abcdefaxc"
k = 10
output_str = replace_duplicate_chars(input_str, k)
print(output_str)  # 输出: abcdef-x-

input_str = "abcdefaxcqwertba"
k = 10
output_str = replace_duplicate_chars(input_str, k)
print(output_str)  # 输出: abcdef-x-qw-rtb-