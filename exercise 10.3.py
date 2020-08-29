message = input(">")
emoji = {
    ':)': '😀',
    '(:': '😌'
}

msg_split = message.split(" ")
output = ""
for items in msg_split:
    if items not in emoji:
        output += items + " "
    else:
        output += emoji[items]

print(output)