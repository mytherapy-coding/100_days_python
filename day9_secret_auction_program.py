auction_log = {}
name = input("What's your name?:")
bid = input("What is your bid?: $")
auction_log[name] = bid
new_bidder = input(f"Is there a new bidder? 'yes' or 'no:' ") 
print(name)
print(bid)
print(new_bidder)
print(auction_log)


def winner():
    list_values = []
    for a in auction_log:
        list_values.append(auction_log[a])
    winner_found = max(list_values)
    return winner_found


members = True

while members:
    if new_bidder == "yes".lower():
        name = input("What's your name?:")
        bid = input("What is your bid?: $")
        auction_log[name] = bid
        new_bidder = input("Is there a new bidder?" "yes or no?") 
    else:
        res =winner()
        print(res)
        members = False
