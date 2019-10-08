def main():
  print ("Program Pembagian Bilangan")
  
  try:
    a = float(input("Masukkan a: "))
    b = float(input("Masukkan b: "))
    
    hasil = a / b
    
  except ZeroDivisionError:
    print ("\nError: Nilai b tidak boleh nol")
    
  except ValueError:
    print ("\nError: a dan b harus berupa angka")
    
  except KeyboardInterrupt:
    print ("\nError: Jangan tekan Ctrl+C")
    
  else:
    print ("\na : ", a)
    print ("b : ", b)
    print ("a / b : ", hasil)

if __name__ == "__main__":
  main()
