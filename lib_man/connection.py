import csv
import random

# List of unique promotional message templates
promo_templates = [
    "Hurry! {discount}% off on all items for the next {hours} hours only! Shop now!",
    "Exclusive offer: Buy {quantity}, Get {quantity} free on select products. Limited time!",
    "Get {discount}% off your next purchase with code {code}! Shop now!",
    "Flash Sale: Up to {discount}% off on select items. Don't miss out!",
    "Shop now and save {discount}% on your first order! Use code {code}.",
    "Big Discounts! Save up to {discount}% on your favorite products!",
    "Limited Time Offer: Free shipping on orders over ${amount}!",
    "Get {discount}% off when you subscribe to our newsletter today!",
    "Buy more, save more: {discount}% off on purchases over ${amount}.",
    "Hurry, this offer ends soon! Up to {discount}% off select items."
]

# List of unique spam message templates
spam_templates = [
    "Congratulations! You've won a {prize} worth ${amount}. Click here now!",
    "You've been selected for a free {item}! Claim it before it’s too late!",
    "Urgent: Your account has been compromised. Click here to secure it!",
    "You’ve received a bonus payout! Click here to claim your reward of ${amount}.",
    "Act now! Your {prize} is waiting! Claim your free {item} today.",
    "You’ve been chosen to receive a ${amount} {gift_card} gift card! Claim it now!",
    "Exclusive offer: Free {item} for completing a short survey. Hurry!",
    "Your package has arrived. Click here to confirm your shipping details.",
    "You’ve won a lottery! Claim your ${amount} {prize} now.",
    "Important: Your bank account will be frozen unless you verify it immediately."
]

# Function to generate random promotional messages
def generate_promotional_message():
    promo_message = random.choice(promo_templates)
    # Filling in placeholders with random values
    promo_message = promo_message.format(
        discount=random.randint(10, 70),
        hours=random.randint(1, 24),
        quantity=random.randint(1, 3),
        code=random.choice(["SAVE10", "DISCOUNT20", "WELCOME30"]),
        amount=random.randint(50, 200)
    )
    return promo_message

# Function to generate random spam messages
def generate_spam_message():
    spam_message = random.choice(spam_templates)
    # Filling in placeholders with random values
    spam_message = spam_message.format(
        prize=random.choice(["gift card", "cash prize", "vacation"]),
        amount=random.randint(100, 1000),
        item=random.choice(["iPhone", "laptop", "TV"]),
        gift_card=random.choice(["Amazon", "Walmart", "Target"])
    )
    return spam_message

# Create a list of 1000 promotional and 1000 spam messages
messages = []

# Generate 1000 unique promotional messages
for _ in range(1000):
    messages.append(["Promotional", generate_promotional_message()])

# Generate 1000 unique spam messages
for _ in range(1000):
    messages.append(["Spam", generate_spam_message()])

# Path for the CSV file
file_path = "promotional_and_spam_messages_unique.csv"

# Writing to CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Message Type", "Message"])  # Writing header
    writer.writerows(messages)

print(f"CSV file created successfully at {file_path}")
