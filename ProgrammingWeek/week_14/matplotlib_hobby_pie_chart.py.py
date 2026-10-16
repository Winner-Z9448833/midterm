import matplotlib.pyplot as plt

def main():
    hobbies = ['Gaming', 'Reading', 'Exercise', 'Gardening']
    hours = [10, 6, 5, 3]

    plt.figure(figsize=(6, 6))
    plt.pie(hours, labels=hobbies, autopct='%1.1f%%', startangle=140)
    plt.title('Weekly Time Spent on Hobbies')
    plt.show()

if __name__ == "__main__":
    main()