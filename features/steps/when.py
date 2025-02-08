from behave import when

@when("I do this")
def step_impl(context):
    print("WHEN")
