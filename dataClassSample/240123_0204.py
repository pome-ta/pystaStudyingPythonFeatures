from dataclasses import dataclass


@dataclass
class SampleClass:
  hoge: int = 1
  fuga: int = 2
  piyo: int = hoge << fuga


aaa = SampleClass.hoge
abbb = SampleClass()

