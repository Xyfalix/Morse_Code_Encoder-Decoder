morse_code_encoder = {"A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
                      "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
                      "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
                      "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
                      "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
                      "Z": "--.. ", "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ",
                      "5": "..... ", "6": "-.... ", "7": "--... ", "8": "----. ", "9": "----. ",
                      "0": "----- ", ",": "--..-- ", ".": ".-.-.- ", "?": "..--.. ",
                      ":": "---... ", "'": ".----. ", "-": ".----. ", "/": "-..-. ",
                      "(": "-.--. ", ")": "-.--.- ", " ": " / ", '"': ".-..-. "}


# use dictionary comprehension to flip the encoder to create the decoder
morse_code_decoder = {v: k for k, v in morse_code_encoder.items()}


def morse_code_program():
    print("Welcome to the Morse Code Encoder/Decoder!")
    operation = input("Key in 'encode' if you want to convert a string into morse code or 'decode' if you want to"
                      "convert morse code back into string. ")
    if operation != "encode" and operation != "decode":
        print("Your input was invalid, please try again.")
        morse_code_program()

    elif operation == "encode":  # morse code encoder
        user_encode_input = input("Key in the text you want to convert into morse code: ").upper()
        user_encode_input_list = list(user_encode_input)
        encoded_morse_code_list = []
        for letter in user_encode_input_list:
            try:
                encoded_morse_code_list.append(morse_code_encoder[letter])
            except KeyError:
                print("Your input string contains elements not in the encoder!")
                return
        encoded_morse_code = ''.join(encoded_morse_code_list)
        print(f'Your encoded morse code is {encoded_morse_code}')

    else:  # morse code decoder
        user_decode_input = input("Key in the morse code you want to decode back into text: ")
        code_list = user_decode_input.split()  # split each morse code into an element of code_list
        morse_code_list = []
        decoded_list = []

        # convert morse code string into a list
        for code in code_list:
            if code == "/":  # check for word spacing in the morse code
                code = " / "
                morse_code_list.append(code)
            else:
                morse_code_list.append(code + " ")

        #  convert morse code list back into list of letters, numbers and symbols
        for element in morse_code_list:
            try:
                decoded_list.append(morse_code_decoder[element])
            except KeyError:
                print("Your input string contains elements not in the decoder!")
                return
        decoded_string = ''.join(decoded_list)
        print(f'Your decoded string is {decoded_string}.')

    # ask user if they would like to run the program again
    user_repeat = input("Would you like to run the Morse Code Encoder/Decoder"
                        " again? Press 'y' for yes, 'n' for no.").lower()
    if user_repeat == 'y':
        morse_code_program()
    elif user_repeat == 'n':
        print("Thank you for using the Morse Code Encoder/Decoder, have a nice day!")
    else:
        print("Your input was not recognized, the program will terminate.")


morse_code_program()
