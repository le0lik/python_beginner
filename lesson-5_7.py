import json

filename = "lesson-5_7.txt"
outfile = "lesson-5_7.json"

with open(filename, encoding="UTF8") as txtfile:
    avg_profit = 0
    cnt_profit = 0
    profits_dict = {}
    for line in txtfile:
        name, form, income, costs = line.split(" ")
        profit = int(income) - int(costs)

        profits_dict[name] = profit

        if profit > 0:
            avg_profit += profit
            cnt_profit += 1

    avg_profit /= cnt_profit
    s_list = [profits_dict, {"average_profit": avg_profit}]

    print(s_list)

with open(outfile, "w") as jsonfile:
    json.dump(s_list, jsonfile)