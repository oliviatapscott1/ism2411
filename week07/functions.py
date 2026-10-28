# AI DISCLOSURE
# AI was used to explain Python error messages during Exercise 5 in the file "broken_sales.py)". The explanations were used to help understand the errors, but the fixes were completed independently. I did not copy and paste any code directly from AI, but learned how to perform the fixes on my own.

# Self-assessment answers:
# 1. In exercise 5, the first bug I noticed was the missing colon. I saw the red squiggly under the line first and immediately spotted it. I think I can spot super basic bugs but am not a pro
# 2. The apply_discount(price, tier) function takes the original price and the customer’s discount tier as inputs. It checks whether the tier is gold, silver, bronze, or something else and applies the correct discount. It then returns the price after the discount has been taken off. A colleague could use it without reading the body as long as they know they need to provide a price and a tier.
# 3. Using AI helped build my understanding because it explained what the error messages meant instead of just giving me the code to copy. I was able to use the explanations to understand why the errors happened and then fix the code myself.


# Exercise 1

# Define calculate tax funciton

def calculate_tax(price, rate):
    return price * rate

# calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")  # $7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}")  # $20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}")  # $7.50  -- this is how you can put the calculation directly inside the print statement without storing it in a variable first

# Exercise 2

def apply_discount(price, tier):  # not giving a discount, but applying the actual discount to the price
    if tier == "gold":
        return price * 0.85  
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price  # no discount for other tiers

# calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]  # list format

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")  # prints the discounted price for each tier


# Exercise 3

# write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")  
print(f"After tax: ${after_tax:.2f}")  

# refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")



# Exercise 6 - concept of scope

x = 100  # apple  # global

def double_it():
    x = 999  # another apple (not the same as above) (local variable)
    return x * 2

print(x)
print(double_it())
print(x)

# or multiply the global x  --- not really part of the exercise but i wanted the notes
def double_global():
    global x  # this tells python to use the global variable x
    x = x * 2
    return x

print(x)
print(double_global())
print(x)