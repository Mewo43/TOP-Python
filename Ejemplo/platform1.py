from platform import machine,system,platform, version
from platform import python_implementation, python_version_tuple

print(machine())
print(platform())
print(platform(1))
print(platform(0, 1))
print(system())
print(version())


print(python_implementation())

for atr in python_version_tuple():
    print(atr, end=',')
 