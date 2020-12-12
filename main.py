length = int(input('Enter room length: '))
width = int(input('Enter room width: '))

area = length * width
price = area * 20

discount = None

while discount not in ('y', 'n'):
    discount = input('Do you want to apply discount? (please answer "y" or "n"): ')
    if discount == 'y':
        discountValue = int(input('How much of discount in %: '))
        discountAmount = price * discountValue / 100
        finalDisAmount = price - discountAmount
        print('The discounted amount is ${}'.format(discountAmount))
        print('The total amount for the customer to pay is ${} for {}ft^2'.format(finalDisAmount, area))

    elif discount == 'n':
        print('The total amount for the customer to pay is ${} for {}ft^2'.format(price, area))
