from title import show_title
from register import register_sale
from historial import show_summary

def main():

    total_day = 0

    show_title()

    sale = "yes"

    while sale.lower() in ["yes", "si", "sí"]:

        total = register_sale()
        print("Total sale amount:", total)

        total_day += total

        sale = input("Do you want to register another product? (yes/no): ").strip()

    show_summary(total_day)

main()