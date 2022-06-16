from time import sleep
from utils.fetchData import isAlreadyCheckIn
from utils.fetchData import checkIn
from utils.loader import Loader
import sys



if __name__ == "__main__":

  argument = sys.argv
  user = argument[1]
  alreadyCheckIn = False

  with Loader("...checking user status", "\033[32m Done! ✅\033[0m"):
    try:
      alreadyCheckIn = isAlreadyCheckIn(user)
    except KeyError:
      print("Library Data Fetch Error!")
      exit(1)

  if alreadyCheckIn:
    print(f"\033[33m {user} Already Check In 🚀 \033[0m")
  else:
    with Loader("...update user status", "\033[32m Done! ✅\033[0m"):
      try:
        checkIn(user)
      except KeyError:
        print("Library Data Fetch Error!")
    print("\033[34m Check In Success 🚀 \033[0m")
