# a more complex mad libs game with one round of error checking

from datetime import datetime

def mad_lib():

    words = { "Enter an adjective:" : None,
              "Enter a noun:" : None,
              "Enter a place:" : None
    }

    now = datetime.now()

    year_born = int(raw_input("What year were you born?"))

    if year_born > now.year:
        print "Were you really born after this year? "
        year_born = raw_input("Please re-enter your birth year.")

    for prompt in words.keys():
        words[prompt] = raw_input(prompt)
        value = words[prompt]
        if len(value) == 0 or not value.isalpha():
            print "That entry won't work. Try again."
            words[prompt] = raw_input(prompt)

    years_ago = now.year - int(year_born)

    story = "In %s, exactly %s years ago, a %s %s was born in %s. It was you!" % (year_born, years_ago, words["Enter an adjective:"], words["Enter a noun:"], words["Enter a place:"])

    print story

mad_lib()

