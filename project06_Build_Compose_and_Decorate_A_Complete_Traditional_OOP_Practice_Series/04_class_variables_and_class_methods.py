class Bank:
  bank_name = "Bank Al-Falah"

  def __init__(self):
    pass

  @classmethod
  def change_bank_name(cls, name):
    cls.bank_name = name
  

# Before Name Change
print(Bank.bank_name)
bank1 = Bank()
print(f"Instance before change: {bank1.bank_name}")


# After Name Change
Bank.change_bank_name("Meezan Bank")
print(Bank.bank_name)

# First Instance 
bank2 = Bank()
print(f"First Instance after change: {bank2.bank_name}")

# Second Instance
bank3 = Bank()
print(f"Second Instance after change: {bank3.bank_name}")
