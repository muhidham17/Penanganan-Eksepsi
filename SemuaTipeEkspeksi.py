def main():
  print ("Program Pembagian Bilangan")
  
  try:
  
    a = float(input("Masukkan a: "))
    b = float(input("Masukkan b: "))
  
    hasil = a / b
    
  except (ZeroDivisionError, ValueError, KeyboardInterrupt):
    print("\nError: Anda telah melakukan " + "kesalahan")
    
  else:
    print("\na : ", a)
    print("b : ", b)
    print("a / b = ", hasil)
    
if __name__ == "__main__":
  main()
