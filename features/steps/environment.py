def before_scenario(context, scenario):
    # Start browser here if needed for all tests
    pass

def after_scenario(context, scenario):
    # Close the browser after each scenario
    if hasattr(context, 'driver'):
        context.driver.quit()
