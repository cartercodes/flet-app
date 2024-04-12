from flet import *

def main (page: Page):
    BG = '#243e36'
    FWG = '#7ca982'
    FG = '#f1f7ed'
    PINK = '#e8998d' 

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )


    categories_card = Row(
        scroll='auto',
    )

    create_task_view = Container(
        content=Container(on_click=lambda e: page.go('/'),
            height=40, width=40,
            content=Text('x')          
        )
    )

    tasks=Column()

    categories = ['Business', 'Family', 'Study', 'Health']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                border_radius=20.
                bgcolor=BG,
                width=170,
                height=110,
                padding=15,
                content=Column(
                    controls=[
                        Text('40 Tasks')
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12'
                            border_radius=20,
                            padding=padding.only(right=i*30),
                            content=Container(
                                bgcolor=PINK,
                            )

                        )
                    ]
                )
            )
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                controls=[
                    Container(
                    on_click=lambda e: shrink(e),
                    content=Icon(
                        icons.MENU)),
                    Row(
                    controls=[
                        Icon(icons.SEARCH),
                        Icon(icons.NOTIFICATIONS_OUTLINED)
                    ],
                    ),
                ],
                ),
                Container(height=20),
                Text(
                value='What\'s up, Olivia!'
                ),
                Text(
                value='CATEGORIES'
                ),
                Container(
                padding=padding.only(top=10,bottom=20,),
                content=categories_card
                ),
                Container(height=20),
                Text("TODAY'S TASKS"),
                Stack(
                controls=[
                    tasks,
                    FloatingActionButton(bottom=2,right=20,
                    icon = icons.ADD,on_click=lambda _: page.go('/create_task') #floating action button
                    )
                ]
                )
            ],
        ),
    )    

    page_1 = Container()

    page_2 = Row(
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=BG,
                border_radius=35,
                padding=padding.only(
                    top=50,
                    left=20,
                    right=20,
                    bottom=50
                )
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            ),
        ]
    )

    container = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2,
            ]
        )
    )

    #dictionary of pages
    pages = {
        '/' : View(
            "/",
            [
                container
            ],
        ),
        '/create_task' : View(
                        "/create_task",
                        [
                            create_task_view
                        ],
        )
    }

    page.add(container)
    page.on_route_change = route_change #router 
    page.go(page.route)

app(target=main)
