def consensus():
    global blockchain

    longest_chain = None
    current_len = len(blockchain)

    for node in peers:
        response = re