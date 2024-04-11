#Veronica Ocampo
def encode(password):
    encoded_pass = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10) #shifts each digit up by 3 numbers
        encoded_pass += encoded_digit
    return encoded_pass

#Tonuka Sultan
def decode(password):
    ps = password
    decoded = ""
    a = 0
    for i in range(len(ps)):
        a = int(ps[i]) + 3
        decoded += str(a)
    return decoded





def main():
    while True:
        print('Menu\n'
            '-------------\n'
            '1. Encode\n'
            '2. Decode\n'
            '3. Quit\n')

        option = input('Please enter an option: ')
        if option == '1':
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!\n')



        if option == '3':
            break

if __name__ == '__main__':
    main()
