from behave import given

@given("I have this")
def step_impl(context):
    print("GIVEN")
