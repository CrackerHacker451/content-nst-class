def check_eligibility(age):
    if age >= 18:
        return True
    else:
        return False


if check_eligibility(17):
    print("Proceed to voting booth.")