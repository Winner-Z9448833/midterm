def parking_fee(H):
    if H<=0:
        return 0
    if 4>=H>0:
        return (H-1)*20
    else:
        return 60+(H-4)*50
   
while True:
    try:
        fee=float(input("parking time(in hours): "))
        if fee<=0:
            print("parking time must be greater than 0.")
            continue
        fee=fee*60
        H=fee//60
        M=fee%60
        print(f"parking time: {H} hours and {M} minutes")
        if M>15:
            H+=1
        print(f"parking fee: {parking_fee(H)} baht")
    except ValueError:
        print("Please enter a valid number for parking hours.")