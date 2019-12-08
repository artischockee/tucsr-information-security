def get_appropriate_phrase_len(divider: int, phrase_len: int) -> int:
    appropriate_phrase_len = phrase_len

    safe_iterations_amount = 1000
    while appropriate_phrase_len % divider != 0 and safe_iterations_amount > 0:
        appropriate_phrase_len += 1
        safe_iterations_amount -= 1
    if safe_iterations_amount == 0:
        print('Safe iterations amount is over, will return', appropriate_phrase_len)

    return appropriate_phrase_len


# Yield successive n-sized
# chunks from l.
def divide_chunks(list_of_chunks: list, n: int):
    # looping till length l
    for i in range(0, len(list_of_chunks), n):
        yield list_of_chunks[i:i + n]
