from health_app.health import Health
from health_app.data import save, read, get_statistics

records = read("health_records.json")

def menu():
    while True:
        print("""
        ***HEALTH APPLICATION***
        --- Main Menu ---
        1. Add Health Record
        2. View All Records
        3. View Statistics
        4. Save & Quit
        """)

        option = input("Enter your choice (1-4): ")

        if option == "1":
            print("-- 1. Add Health Record --\n")

            flag = True
            while flag:
                while True:
                    name = input("Enter name: ")
                    if name == "":
                        print("Name cannot be empty, try again.")
                        continue
                    break

                while True:
                    input_weight = input("Enter weight (kg): ")
                    try:
                        weight = float(input_weight)
                    except ValueError:
                        print("Only numbers allowed, try again.")
                        continue
                    if weight <= 0:
                        print("Weight must be > 0.")
                        continue
                    break

                while True:
                    input_height = input("Enter height (m): ")
                    try:
                        height = float(input_height)
                    except ValueError:
                        print("Only numbers allowed, try again")
                        continue
                    if height <= 0:
                        print("Height must be > 0.")
                        continue
                    break

                person = Health(name, weight, height)
                records.append(person)
                save(records)
                print(f"\nAdded [{person.name}] | BMI: [{person.calculate_bmi()}] | Ideal: [{person.get_ideal_weight()}]kg | Advice: [{person.get_health_advice()}]")

                prompt = input("Do you want to add another person? y/n").lower()
                if prompt != "y":
                    flag = False

        elif option == "2":
            print("-- 2. View All Records --\n")
            if not records:
                print("List is empty, please add a health record first!")
                continue

            for person in records:
                weight_difference: float = round((person.weight_kg - person.get_ideal_weight()), 2)
                weight_format = ""
                if weight_difference > 0:
                   weight_format += "+" + str(weight_difference)
                else:
                    weight_format = str(weight_difference)
                print(f"Name: [{person.name}] | BMI: [{person.calculate_bmi()}] | Category: [{person.category_bmi()}] | Ideal Weight Difference: {weight_format}")

        elif option == "3":
            print("-- 3. View Statistics --\n")
            statistics = get_statistics("health_records.json")
            for key, value in statistics.items():
                if key == "total_records":
                    print(f"Total Records: {value}")
                elif key == "avg_bmi":
                    print(f"Average BMI: {value}")
                elif key == "most_common_category":
                    print(f"Most Common Category: {value}")
                elif key == "category_distribution":
                    print(f"Distribution Of Categories: {value}")

        elif option == "4":
            save(records)
            print("Saved to file. Exiting now....bye.")
            break
        else:
            print("Invalid option, please select a number between 1 - 4.")




def main():
    menu()

if __name__ == "__main__":
    main()


