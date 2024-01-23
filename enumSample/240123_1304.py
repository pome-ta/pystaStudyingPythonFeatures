from enum import IntFlag, auto

class SampleClass(IntFlag):
  hoge: int = 0
  fuga: int = auto()
  piyo: int = hoge << fuga


a = SampleClass.hoge
print(a)
