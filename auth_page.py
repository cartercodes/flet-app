from flet import *

def auth_page(page: Page):
    # Define a state to toggle between sign-in and sign-up
    page.state = "sign-in"

    def toggle_state(e):
        if page.state == "sign-in":
            page.state = "sign-up"
        else:
            page.state = "sign-in"
        update_form()

    def update_form():
        form_controls.clear()
        if page.state == "sign-in":
            form_controls.extend([
                TextField(label="Email", autocorrect=False),
                TextField(label="Password", password=True),
                ElevatedButton(text="Sign in", on_click=sign_in)
            ])
        else:
            form_controls.extend([
                TextField(label="First Name"),
                TextField(label="Last Name"),
                TextField(label="Email", autocorrect=False),
                TextField(label="Password", password=True),
                ElevatedButton(text="Sign up", on_click=sign_up)
            ])
        page.update()

    def sign_in(e):
        # Implement sign-in logic here
        pass

    def sign_up(e):
        # Implement sign-up logic here
        pass

    # Form container
    form_controls = []
    form = Column(controls=form_controls, alignment=alignment.center)

    # Hyperlink to toggle between sign-in and sign-up
    toggle_link = TextButton(
        content=Text("Or sign-up here" if page.state == "sign-in" else "Or sign-in here"),
        on_click=toggle_state,
    )

     # Use the BG and PINK color variables from your main page, or define them here
    BG = '#243e36'  # Example background color
    PINK = '#e8998d'  # Example pink color used for buttons

    # Wrap the form and toggle link in a container with the same styling
    auth_container = Container(
        content=Column(controls=[form, toggle_link], alignment=alignment.center),
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        padding=padding.all(20),
        alignment=alignment.center
    )

    # Layout
    page.add(Column(controls=[form, toggle_link]))

    update_form()

    return auth_container

# TODO: Ensure that auth page has been properly architected and tested before integrating it into the main page.