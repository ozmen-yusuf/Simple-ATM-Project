# PROJE ADI:MINI-ATM
# Oncelikle baslangic bakiyemizi tanimliyoruz.
balance = 1000

# Kullanici 'q'ya basana kadar calisacak ana dongu
while True:
    # '\n' karakteri bir alt satira gecmeyi saglar, menuyu daha okunakli yapar.
    print("\n--- Financial Control Simulator ---")
    print("1: Check Balance")
    print("2: Deposit Money")
    print("3: Withdraw Money")
    print("q: Quit")

    # Kullanicidan secimini aliyoruz.
    choice = input("Please select an operation (1,2,3, or q)")

    # Kullanicinin secimini if-elif-else ile analiz ediyoruz
    if choice == '1':
        print("\n--- Balance Inquiry ---")
        print(f"Your current balance is {balance} TL")

    elif choice == '2':
        print("\n--- Deposit Money ---")
        # input ile string olarak al, int() ile aninda sayiya cevir
        amount_str = input("Amount to deposit: ")
        try:
            # Bu blogu calistirmayi DENE
            amount = int(amount_str)
            # Yatirilan tutarin pozitif olup olmadigini kontrol edelim
            if amount > 0:
                # Bakiyeyi guncelle
                balance = balance + amount
                print(f"Deposit successful. New balance is: {balance} TL")
            else:
                print("\nInvalid amount. Please enter a positive number.")
        except ValueError:
            # Eger 'try' blogunda bir ValueError HATASI olursa, burayi calistir
            print("\nError! Please enter only numbers.")        

            
        

    elif choice == '3':
        print("\n--- Withdraw Money ---")
        amount_str = input("Amount to withdraw: ")

        try:
            amount = int(amount_str)
            # Bakiye kontrolu (ic ice if/else)
            if amount > balance:
                print(f"\nInsufficient balance! Error! You only have {balance} TL.")

            else:
                if amount > 0:
                    balance = balance - amount
                    print(f"Withdrawal successful. New balance is: {balance} TL")
                else:
                    print("\nInvalid amount. Please enter a positive number.")       
        except ValueError:
            print("\nError! Please enter only numbers.")     

    elif choice == 'q':
        print("\nExiting protocol...")
        break  

    else:
        print("\nInvalid operation. Please try again.")  

# Dongu kirildiktan sonra calisacak son satir
print("\nProtocol finished. Thank you for using the system.")    
