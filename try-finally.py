def main():
  try:
    f = open ("data.txt", "w")
    
    try:
      f.write ("Pemrograman Python")
    finally:
      f.close()
  except IOError:
    print ("\nError: File tidak dapat" + "dibuka/ditulis")

if __name__ == "__main__":
  main()
