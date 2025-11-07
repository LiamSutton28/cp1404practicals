"""
Guitar
Estimate: 30 minutes
Actual:   19 minutes
"""
from prac_06.guitar import Guitar

guitar_01 = Guitar("Gibson L-5 CES",1922,16035.40)
guitar_02 = Guitar("Another Guitar", 2013, 200)
print(f"{guitar_01.name} get_age() - Expected 103. Got {guitar_01.get_age()}")
print(f"{guitar_02.name} get_age() - Expected 12. Got {guitar_02.get_age()}")
print(f"{guitar_01.name} is_vintage() - Expected True. Got {guitar_01.is_vintage()}")
print(f"{guitar_02.name} is_vintage() - Expected False. Got {guitar_02.is_vintage()}")
