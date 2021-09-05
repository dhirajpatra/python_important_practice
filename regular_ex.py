# Exercise: make a regular expression that will match an email
import re


def test_email(your_pattern):
    repattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org",
              "wha.t.`1an?ug{}ly@email.com", "dhiraj@gcol.co.in"]
    for email in emails:
        if not re.fullmatch(repattern, email):
            print("You failed to match %s" % email)
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")


# Your pattern here!
# pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
pattern = r'\b[^0-9_][\w._-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}\b'
test_email(pattern)

def transform_date_format(date):
   return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
date_input = "2021-08-01"
print(transform_date_format(date_input))