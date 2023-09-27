import sys

registered_users = {}

registered_companies = {}

def registration_page():
    print("Registration:")
    
    print("Terms and Conditions:")
    print("By using this service, you agree to abide by the terms and conditions.")
    print("1. Green Energy Services is not responsible for any damages or losses.")
    print("2. Use of renewable energy is subject to availability in your area.")
    print("3. Your personal information will be kept confidential.")
    print("4. Green Energy Services may send you occasional updates and offers.")
    print("\nDo you agree to the terms and conditions?")
    agreement = input("Enter 'yes' to agree or 'no' to exit: ")
    
    if agreement.lower() == 'yes':
        phone_number = input("Enter your phone number: ")
        name = input("Enter your name: ")
        registered_users[phone_number] = name
        print("Registration successful!")
    else:
        print("You have chosen not to agree to the terms and conditions. Exiting.")

def login_page():
    print("Login:")
    phone_number = input("Enter your phone number: ")
    if phone_number in registered_users:
        user_name = registered_users[phone_number]
        print(f"Welcome back, {user_name}!")
        return user_name
    else:
        print("Phone number not found. Please register first.")
        return None

def welcome_page(user_name):
    print(f"Welcome, {user_name}!")
    print("1. Information")
    print("2. Education")
    print("3. Going Green")
    print("4. Discovery")
    print("5. Register your company")
    print("6. Exit")

def information_page():
    while True:
        print("Going Green Methods:")
        print("1. Solar Energy")
        print("2. Wind Energy")
        print("3. Recycling")
        print("4. Energy-efficient Appliances")
        choice = input("Select a method to learn more (1/2/3/4), or enter 'back' to return to the previous menu: ")
        if choice == "1":
            print("Solar energy is a renewable energy source that harnesses the power of the sun to generate electricity.")
            print("1. More information")
            print("2. back")
            choice2 = input("What would you like to do next?")
            if choice2 == "1":
                print("Here is the link:")
            elif choice2 == "2":
                information_page()
            else:
                print("Invalid choice. Please select a valid option.")
        elif choice == "2":
            print("Wind energy uses the kinetic energy of the wind to generate electricity through wind turbines.")
            print("1. More information")
            print("2. back")
            choice2 = input("What would you like to do next?")
            if choice2 == "1":
                print("Here is the link:")
            elif choice2 == "2":
                information_page()
            else:
                print("Invalid choice. Please select a valid option.")
        elif choice == "3":
            print("Recycling reduces waste by reusing materials, conserving resources, and reducing pollution.")
            print("1. More information")
            print("2. back")
            choice2 = input("What would you like to do next?")
            if choice2 == "1":
                print("Here is the link:")
            elif choice2 == "2":
                information_page()
            else:
                print("Invalid choice. Please select a valid option.")
        elif choice == "4":
            print("Energy-efficient appliances consume less energy and help reduce electricity consumption.")
            print("1. More information")
            print("2. back")
            choice2 = input("What would you like to do next?")
            if choice2 == "1":
                print("Here is the link:")
            elif choice2 == "2":
                information_page()
            else:
                print("Invalid choice. Please select a valid option.")
        elif choice.lower() == "back":
            return
        else:
            print("Invalid choice. Please select a valid option.")
        
def education_page():
    while True:
        print("Education:")
        print("Select your age group:")
        print("1. Children (Ages 5-12)")
        print("2. Teenagers (Ages 13-19)")
        print("3. Adults (Ages 20+)")
        choice = input("Enter the number of your age group or 'back' to return to the previous menu: ")
        if choice == "1":
            print("Children (Ages 5-12):")
            print("1. Green Energy for Kids")
            print("2. Fun Facts about Solar Power")
            print("3. Back")
            choice2 = input()
            if choice2 == "1":
                print("Here are the links:")
            elif choice2 == "2":
                print("Here are the links:")
            elif choice2 == "3":
                education_page()
            else:
                print("Invalid choice. Please select a valid option.")
        elif choice == "2":
            print("Teenagers (Ages 13-19):")
            print("1. Exploring Wind Energy")
            print("2. The Importance of Recycling")
            print("3. Back")
            choice2 = input()
            if choice2 == "1":
                print("Here are the links:")
            elif choice2 == "2":
                print("Here are the links:")
            elif choice2 == "3":
                education_page()
            else:
                print("Invalid choice. Please select a valid option.")
        elif choice == "3":
            print("Adults (Ages 20+):")
            print("1. Renewable Energy Basics")
            print("2. Energy-Efficient Homes")
            print("3. Back")
            choice2 = input()
            if choice2 == "1":
                print("Here are the links:")
            elif choice2 == "2":
                print("Here are the links:")
            elif choice2 == "3":
                education_page()
            else:
                print("Invalid choice. Please select a valid option.")
        elif choice.lower() == "back":
            return
        else:
            print("Invalid choice. Please select a valid option.")
        
def going_green_page():
    while True:
        print("Going Green:")
        print("Select a type of green energy:")
        print("1. Solar Energy")
        print("2. Wind Energy")
        print("3. Geothermal Energy")
        choice = input("Enter the number of your choice or 'back' to return to the previous menu: ")
        if choice == "1":
            print("Solar Energy:")
            print("Nearby places to buy solar panels and hire solar installation services:")
            print("1. SolarMart Store")
            print("2. Sunshine Solar Solutions")
            print("3. Back")
            choice2 = input()
            if choice2 == "1":
                print("Here are the address's:")
            elif choice2 == "2":
                print("Here are the address's:")
            elif choice2 == "3":
                going_green_page()
            else:
                return
        elif choice == "2":
            print("Wind Energy:")
            print("Nearby places to buy wind turbines and hire wind energy experts:")
            print("1. WindTech Store")
            print("2. Breezy Energy Services")
            print("3. Back")
            choice2 = input()
            if choice2 == "1":
                print("Here are the address's:")
            elif choice2 == "2":
                print("Here are the address's:")
            elif choice2 == "3":
                going_green_page()
            else:
                return
        elif choice == "3":
            print("Geothermal Energy:")
            print("Nearby places to explore geothermal heating and cooling options:")
            print("1. EarthHeat Systems")
            print("2. GeoClimate Solutions")
            print("3. Back")
            choice2 = input()
            if choice2 == "1":
                print("Here are the address's:")
            elif choice2 == "2":
                print("Here are the address's:")
            elif choice2 == "3":
                going_green_page()
            else:
                print("Invalid choice. Please select a valid option.")
        elif choice.lower() == "back":
            return
        else:
            print("Invalid choice. Please select a valid option.")
        
def discovery_page():
    print("Discovery:")
    print("Nearby places for recycling and discovering the green economy:")
    print("1. Green Recycling Centers")
    print("2. EcoDiscovery Hubs")
    choice = input("Enter the number of your choice or 'back' to return to the previous menu: ")
    if choice == "1":
        print("Here are a few centres:")
        print("1. SolarMart Store")
        print("2. Sunshine Solar Solutions")
        choice2 = input()
        if choice2 == "1":
            print("Here is the address:")
        elif choice2 == "2":
            print("Here is the address:")
        else:
            print("Invalid choice. Please select a valid option.")
    if choice == "2":
        print("Here are a few centres:")
        print("1. SolarMart Store")
        print("2. Sunshine Solar Solutions")
        choice2 = input()
        if choice2 == "1":
            print("Here is the address:")
        elif choice2 == "2":
            print("Here is the address:")
        else:
            print("Invalid choice. Please select a valid option.")
    elif choice.lower() == "back":
        return
    else:
        print("Invalid choice. Please select a valid option.")
    
def register_company_page():
    while True:
        print("Register Your Company:")
        print("Select the type of your company:")
        print("1. Solar Installation Company")
        print("2. Wind Turbine Manufacturer")
        print("3. Geothermal Heating and Cooling Services")
        company_type = input("Enter the number of your company type or 'back' to return to the previous menu: ")
        
        if company_type == "1":
            company_name = input("Enter your company name: ")
            contact_name = input("Enter the contact name: ")
            contact_email = input("Enter the contact email: ")
            contact_phone = input("Enter the contact phone number: ")
            registered_companies[company_name] = {
                "Type": "Solar Installation Company",
                "Contact Name": contact_name,
                "Contact Email": contact_email,
                "Contact Phone": contact_phone
            }
            print(f"Registration of {company_name} as a Solar Installation Company is successful!")
            print(f"Email has been sent to {contact_email}.")
            print("Thank you!")
            sys.exit()

        elif company_type == "2":
            company_name = input("Enter your company name: ")
            contact_name = input("Enter the contact name: ")
            contact_email = input("Enter the contact email: ")
            contact_phone = input("Enter the contact phone number: ")
            registered_companies[company_name] = {
                "Type": "Wind Turbine Manufacturer",
                "Contact Name": contact_name,
                "Contact Email": contact_email,
                "Contact Phone": contact_phone
            }
            print(f"Registration of {company_name} as a Wind Turbine Manufacturer is successful!")
            print(f"Email has been sent to {contact_email}.")
            print("Thank you!")
            sys.exit()
            
        elif company_type == "3":
            company_name = input("Enter your company name: ")
            contact_name = input("Enter the contact name: ")
            contact_email = input("Enter the contact email: ")
            contact_phone = input("Enter the contact phone number: ")
            registered_companies[company_name] = {
                "Type": "Geothermal Heating and Cooling Services",
                "Contact Name": contact_name,
                "Contact Email": contact_email,
                "Contact Phone": contact_phone
            }
            print(f"Registration of {company_name} as a Geothermal Heating and Cooling Services company is successful!")
            print(f"Email has been sent to {contact_email}.")
            print("Thank you!")
            sys.exit()
            
        elif company_type.lower() == "back":
            return
        else:
            print("Invalid choice. Please select a valid option.")

while True:
    print("Main Menu:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    
    user_input = input("Enter your choice: ")
    
    if user_input == "1":
        registration_page()
    elif user_input == "2":
        user_name = login_page()
        if user_name is not None:
            while True:
                welcome_page(user_name)

                user_input = input("Enter your choice: ")
                
                if user_input == "1":
                    information_page()
                elif user_input == "2":
                    education_page()
                elif user_input == "3":
                    going_green_page()
                elif user_input == "4":
                    discovery_page()
                elif user_input == "5":
                    register_company_page()
                elif user_input == "6":
                    print(f"Thank you for using Green Energy Services, {user_name}! Have a sustainable day!")
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
    elif user_input == "3":
        print("Thank you for visiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
