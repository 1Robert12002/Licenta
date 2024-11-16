def compress(data):

    output = []
    current_position = 0
    data_length = len(data)

    while current_position < data_length:
        max_match_length = 0
        max_match_offset = 0

        for offset in range(1, current_position + 1):
            length = 0
            while (current_position + length < data_length and
                   data[current_position - offset + length] == data[current_position + length]):
                length += 1
            if length > max_match_length:
                max_match_length = length
                max_match_offset = offset

        if max_match_length > 0:
            match_length = max_match_length
            match_offset = max_match_offset
            if current_position + match_length < data_length:
                next_char = data[current_position + match_length]
                increment = match_length + 1
            else:
                next_char = ''
                increment = match_length
            output.append((match_offset, match_length, next_char))
            current_position += increment
        else:
            output.append((0, 0, data[current_position]))
            current_position += 1

    return output


data = input('')
compressed_data = compress(data)
print(compressed_data)