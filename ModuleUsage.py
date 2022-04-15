import testModule

print(testModule.greeting("Leif"))

occupation = testModule.leifCharacteristics["Occupation"]
print(occupation)

#Built-in modules

import platform
operatingSystem = platform.system()
print(operatingSystem)

#Using the dir() Function

y = dir(platform)
print(y)

#You can just use one part of a module

from testModule import simpleCalculator

print(simpleCalculator(12, 15))