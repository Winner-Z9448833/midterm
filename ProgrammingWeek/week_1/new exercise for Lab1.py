while True:
    try:
        user_input = input('change: ')
        
    
        change = float(user_input) * 100
        if change < 0 :
            print("number can not less than 0")
            continue
        
        lib = {
            "1000baht": 100000, "500baht": 50000, "100baht": 10000,
            "50baht": 5000, "20baht": 2000, "10baht": 1000,
            "5baht": 500, "2baht": 200, "1baht": 100,
            "0.5baht": 50, "0.25baht": 25
        }
        
        print("change:")
        for name, value in lib.items():
            count=change//value
            change=change%value
            print(f"{name} = {count}")
        change=change/100
        print(f'and {change:.5f} baht')
            
        print("................................")
        
    except ValueError:
        print("number only\n##############")