while True:
      try:
          a = int(input())
          print(hex(a)[2:].upper())
      except EOFError:
          break