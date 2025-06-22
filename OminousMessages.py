import scratchattach as sa
from dotenv import load_dotenv
import os
import random
import time

load_dotenv()

first_half = [
    "When Tuesday, is just your average Tuesday",
    "When your lunch break forgets to end",
    "When your birthday shows up twice in a week",
    "When your watch decides it’s opposite day",
    "When midnight oversleeps and wakes up at noon",
    "When your nap turns into a small hibernation",
    "When the weekend files for retirement",
    "When your alarm clock asks for a promotion",
    "When one minute refuses to pass",
    "When the snooze button joins a union"
]

# Funny ominous SECOND HALF (silly consequences)
second_half = [
    "your socks will only fit your thumbs",
    "your cereal will revolt at breakfast",
    "your phone battery will hover at 2% forever",
    "your fridge light will gossip about you",
    "your cat will demand a formal apology",
    "your coffee will brew itself at 3 AM",
    "your pillow will hide your dreams somewhere else",
    "your Wi-Fi will tell knock-knock jokes",
    "your shadow will learn interpretive dance",
    "your shoelaces will untie when you brag"
]

def ominous_message():
    return f"{random.choice(first_half)}, {random.choice(second_half)}."

SESSION_ID = os.getenv("SESSION_ID")
USERNAME = os.getenv("USERNAME")

if SESSION_ID is None or USERNAME is None:
    print("Session ID or Username is not in .env")
    exit(1)

DONE_FILE = "done.txt"

# Load already processed usernames
if os.path.exists(DONE_FILE):
    with open(DONE_FILE, "r") as f:
        done_users = set(line.strip() for line in f if line.strip())
else:
    done_users = set()


session = sa.login_by_id(SESSION_ID)
followers = session.connect_user(USERNAME).followers()

print("Signed in as", USERNAME)

for follower in followers:
    username = getattr(follower, "username", str(follower))
    if username in done_users:
        print(username, " in done users, skipped")
        continue
    try:
        follower.post_comment(ominous_message())
        print("Posted comment on", username)
        with open(DONE_FILE, "a") as f:
            f.write(username + "\n")
            print("Wrote username", username)
        time.sleep(20)
    except Exception as e:
        print(e)