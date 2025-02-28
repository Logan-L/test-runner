from behave import then

@then("I should see a pass")
def step_impl(context):
    pass

@then("I should see a failure")
def step_impl(context):
    raise Exception("A failure occured!")
