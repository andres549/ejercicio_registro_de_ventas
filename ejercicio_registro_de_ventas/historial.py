from register import history

def show_summary(total_day):

    print("\n================================")
    print("        DAY SUMMARY")
    print("================================")

    for product in history:
        print("Product:", product)
        print("Quantity sold:", history[product])
        print("----------------------------")

    print("Total collected:", total_day)