def main():
  print ("Program Pembagian Bilangan")
  
  a = float(input("Masukkan a: "))
  b = float(input("Masukkan b: "))
  
  try:
    hasil = a / b
  except ZeroDivisionError:
    print ("\nError: Nilai b tidak boleh nol")
    
    print ("\na : ", a)
    print ("b : ", b)
    
    print ("a / b = ", hasil)
    
if __name__ == "__main__":
  main()
