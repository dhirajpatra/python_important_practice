# Exercise: make a regular expression that will match an email
import re


def test_email(your_pattern):
    repattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org",
              "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(repattern, email):
            print("You failed to match %s" % email)
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")


# Your pattern here!
pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
test_email(pattern)
