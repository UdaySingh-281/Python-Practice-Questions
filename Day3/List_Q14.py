# Write a python program to check whether two lists are circularly identical.

def check_identical_list(list1, list2):
    if len(list1) != len(list2):
        return False

    elif list1 == list2:
      return True

    elif sorted(list1) == sorted(list2):
      if list1[-1] == list2[0] or list1[0] == list2[-1]:
        return True
      else:
        return False

    else:
      return False

list1 = [1, 2, 3, 4, 5]
list2 = [5, 1, 2, 3, 4]

check_identical_list(list1, list2)
