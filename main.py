from sales_analyzer.data import create_sample_data
from sales_analyzer.analyzer import SalesAnalyzer
from sales_analyzer.reports import ConsoleReport
from sales_analyzer.utils import get_int_input


def show_menu():
    print("\n" + "=" * 50)
    print("           SALES DATA ANALYZER")
    print("=" * 50)
    print("1. Display all sales")
    print("2. Total sales")
    print("3. Total profit")
    print("4. Average order value")
    print("5. Best-selling product")
    print("6. Most profitable product")
    print("7. Sales by category")
    print("8. Sales by region")
    print("9. Search product")
    print("10. Complete sales summary")
    print("0. Exit")
    print("=" * 50)


def main():
    # The project creates its own sample data.
    # No CSV file or external dataset is needed.
    records = create_sample_data()

    analyzer = SalesAnalyzer(records)
    report = ConsoleReport()

    while True:
        show_menu()
        choice = get_int_input("Enter your choice: ")

        if choice == 1:
            report.display_records(records)
        elif choice == 2:
            report.show_value("Total Sales", analyzer.total_sales())
        elif choice == 3:
            report.show_value("Total Profit", analyzer.total_profit())
        elif choice == 4:
            report.show_value("Average Order Value", analyzer.average_order_value())
        elif choice == 5:
            report.show_product("Best-Selling Product", analyzer.best_selling_product())
        elif choice == 6:
            report.show_product("Most Profitable Product", analyzer.most_profitable_product())
        elif choice == 7:
            report.show_dictionary("Sales by Category", analyzer.sales_by_category())
        elif choice == 8:
            report.show_dictionary("Sales by Region", analyzer.sales_by_region())
        elif choice == 9:
            product = input("Enter product name: ").strip()
            report.display_records(analyzer.search_product(product))
        elif choice == 10:
            report.show_summary(analyzer)
        elif choice == 0:
            print("\nThank you for using Sales Data Analyzer!")
            break
        else:
            print("Invalid choice. Please select a number from the menu.")


if __name__ == "__main__":
    main()
