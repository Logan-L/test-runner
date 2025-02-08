from behave import then

@then("I should see a pass")
def step_impl(context):
    print("THEN (PASS)")

@then("I should see a failure")
def step_impl(context):
    print("THEN (FAIL)")
    raise Exception("A failure occured!")
