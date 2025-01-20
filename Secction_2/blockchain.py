blockchain = []


def get_last_transaction():
    """ Returns the last transaction of the blockchain.
    .
    """
    # print("GETTING LAST... ")
    return blockchain[-1]


def add_transaction(new_value, last_value=[1]):
    """ Adds the new transaction to the blockchain.

    Arguments:
        : new_value -> It is the new amount of the transaction.
        : last_value -> It is the last series or transaction of the blockchain. Default value [1].
    """
    # print("new_value... ", new_value)
    blockchain.append([last_value, new_value])


def print_blockchain():
    """ Print the final value of the blockchain.
    .
    """
    print("FINAL Blockchain -> ", blockchain)


print("Starting...")

add_transaction(new_value=2)
add_transaction(last_value=get_last_transaction(), new_value=24)
add_transaction(new_value=8, last_value=get_last_transaction())
add_transaction(new_value=54, last_value=get_last_transaction())

print_blockchain()
