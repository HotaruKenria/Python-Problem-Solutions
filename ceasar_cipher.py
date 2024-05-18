class CeasarCipher():
  def __init__(self, shift):
    self.shift = shift


  def encrypt(self, text, shift=None):
    if shift is None:
      shift = self.shift

    result = ""

    for char in text:
      if char.isalpha():
        ascii_offset = 65 if char.isupper() else 97
        result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
      else:
        result += char

    return result

  def decrypt(self, encrypted_text):
      return self.encrypt(encrypted_text, -self.shift)

    
if __name__ == "__main__":
  shift = int(input("Enter a shift value : "))
  cipher = CeasarCipher(shift)

  text = input("Enter a message : ")
  encrypted_text = cipher.encrypt(text)
  print("Encryoted message : "+encrypted_text)

  decrypted_text = cipher.decrypt(encrypted_text)
  print("Decrypted messsage : "+decrypted_text)

                          
