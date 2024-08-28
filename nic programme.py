import time
print("\t ------------ \n \t Project NIC \n \t ------------")

def choice():
    while True:
        choice = input("\n Do you want to continue (Yes or No)? ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("\t exit the programme...")
            time.sleep(2)
            return False
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

def main():
    while True:
        nic = input("\n Type your NIC number : ")
        if len(nic) == 10:
            
            if int(nic[2:6]) > 500:
                print("\t You are Female.")
                time.sleep(2)
            else:
                print("\t You are Male.")
                time.sleep(2)
            
            if nic[-1].lower() == "v":
                print("\t NIC type : old")
                time.sleep(2)
                print(f"\t You were born on 19{nic[0:2]}")
                time.sleep(2)
                print("\t You are a voter.")
                time.sleep(2)

            elif int(nic[0:4]) >= 2004:
                print(f"\t You were born on {nic[0:4]}")
                time.sleep(2)
                print("\t NIC type : New")
                time.sleep(2)
                print("\t You are not voter.")
                time.sleep(2)
            else:
                print("\t NIC type : new")
                print(f"\t You were born on {nic[0:4]}")
                time.sleep(2)
                print("\t You are a voter.")
                time.sleep(2)
            
            if not choice():
                break
        else:
            print("Invalid NIC. Try again.")

if __name__ == "__main__":
    main()
