f = open("input.txt", 'r')
ascii_numbers = f.read().strip().split()

characters = [chr(int(num)) for num in ascii_numbers]

text = ''.join(characters)

f = open('output.txt', 'w')
f.write(text)

print("Matn muvaffaqiyatli yangi faylga yozildi!")