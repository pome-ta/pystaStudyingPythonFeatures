from dis import dis


def f(a):
  try:
    if a:
      print("yes")
    else:
      print("done")
  finally:
    print("done")


if __name__ == "__main__":
  code = f.__code__
  print("==co_lines==")
  print(list(code.co_lines()))
  print("\n==bytecode==")
  dis(code.co_code)

