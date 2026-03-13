from title import show_title
from register import register_sale
from historial import show_summary

def main():

    total_day = 0
    show_title()

    answer = "yes"
    while answer == "yes":

        total = register_sale()
        print("Total sale amount:", total)

        total_day = total_day + total

        answer = input("Do you want to register another product? (yes/no): ").lower()

    show_summary(total_day)


main()