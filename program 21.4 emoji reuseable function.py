def converter(message):
    split_message = message.split(" ")
    emoji = {
            ":)": "😀",
            ":(": "☹"
    }
    output = ""
    for items in split_message:
        output += emoji.get(items, items) +" "
    return output


msg = input("Message >")
print(converter(msg))