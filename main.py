from flet import *
from custom_checkbox import CustomCheckBox

def main (page: Page):
    BG = '#243e36'
    FWG = '#7ca982'
    FG = '#f1f7ed'
    PINK = '#e8998d' 

    # BG = '#041955'
    # FWG = '#97b4ff'
    # FG = '#3450a1'
    # PINK = '#eb06ff'

    circle = Stack(
    controls=[
      Container(
        width=100,
        height=100,
        border_radius=50,
        bgcolor='white12'
        ),
      Container(
                  gradient=SweepGradient(
                      center=alignment.center,
                      start_angle=0.0,
                      end_angle=3,
                      stops=[0.5,0.5],
                  colors=['#00000000', PINK],
                  ),
                  width=100,
                  height=100,
                  border_radius=50,
                  content=Row(alignment='center',
                      controls=[
                        Container(padding=padding.all(5),
                          bgcolor=BG,
                          width=90,height=90,
                          border_radius=50,
                          content=Container(bgcolor=FG,
                            height=80,width=80,
                            border_radius=40,
                          content=CircleAvatar(opacity=0.8,
                foreground_image_url="https://images.unsplash.com/photo-1545912452-8aea7e25a3d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
            )
                          )
                          )
                      ],
                  ),
              ),
      
    ]
  )

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    def shrink(e): #shrinks page 2 to right side of screen
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right)
        page_2.controls[0].border_radius=border_radius.only(
            top_left=35,
            top_right=0,
            bottom_left=35,
            bottom_right=0
        )
        page_2.update()

    def restore(e): #restores page
        page_2.controls[0].width = 400
        page_2.controls[0].border_radius = 35
        page_2.controls[0].scale = transform.Scale(
            1,alignment=alignment.center_right)
        page_2.update()
    


    categories_card = Row(
        scroll='auto',
    )

    create_task_view = Container(
        content=Container(on_click=lambda e: page.go('/'),
            height=40, width=40,
            content=Text('x')          
        )
    )

    tasks=Column(
        height=400,
        scroll='auto',
    )
    for i in range(10):
        tasks.controls.append(
            Container(
            height=70,
            width=400,
            bgcolor=BG,
            border_radius=25,padding=padding.only(
                left=20,top=25,
            ),
            content=CustomCheckBox(
                color=PINK,
                label='Create interesting content!',
                text_color=FG,
            )),
        )

    categories = ['Business', 'Family', 'Study', 'Health']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                border_radius=20,
                bgcolor=BG,
                width=170,
                height=110,
                padding=15, 
                content=Column(
                    controls=[
                        Text('40 Tasks', color='white'),
                        Text(category, color='white'),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
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
                        icons.MENU, color=BG)),
                    Row(
                    controls=[
                        Icon(icons.SEARCH, color=BG),
                        Icon(icons.NOTIFICATIONS_OUTLINED, color=BG)
                    ],
                    ),
                ],
                ),
                Container(height=20),
                Text(
                value='What\'s up, Mitchell!',
                color='white',
                ),
                Text(
                value='CATEGORIES',
                color='white',
                size=12,
                ),
                Container(
                padding=padding.only(top=10,bottom=20,),
                content=categories_card
                ),
                Container(height=20),
                Text("TODAY'S TASKS", color='white', font_family='poppins',),
                Stack(
                controls=[
                    tasks,
                    FloatingActionButton(bottom=2,right=20,
                    bgcolor=PINK,
                    icon = icons.ADD,on_click=lambda _: page.go('/create_task') #floating action button
                    )
                ]
                )
            ],
        ),
    )    

    page_1 = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(left=50,top=60,right=200),

        content=Column(
            controls=[
            Row(alignment='start',
            controls=[
                Container(border_radius=25,
                padding=padding.only(
                top=13,left=13,),
                height=50,
                width=50,
                border=border.all(color=FWG,width=2),
                on_click=lambda e: restore(e),
                content=Text('  <', color=FWG),
                )
                ]
                ),
                Container(height=20),
                circle,
                Text('Mitchell\nCarter',size=32, color='white', weight='bold'),
                Container(height=25),
                Row(controls=[
                Icon(icons.FAVORITE_BORDER_SHARP,color='white60'),
                Text('Favorites',size=15,weight=FontWeight.W_300,color='white',font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                Icon(icons.CARD_TRAVEL,color='white60'),
                Text('Categories',size=15,weight=FontWeight.W_300,color='white',font_family='poppins')
                ]),
                Container(height=5),
                Row(controls=[
                Icon(icons.CALCULATE_OUTLINED,color='white60'),
                Text('Analytics',size=15,weight=FontWeight.W_300,color='white',font_family='poppins')
                ]),

                Image(src=f"/images/1.png",
                width=300,
                height=200,
            ),
            Text('Great',color=FG,font_family='poppins',),
            Text('Consistency',color=FG,font_family='poppins',)
            
            ]
        )
    )

    page_2 = Row(alignment='end',
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FWG,
                border_radius=35,
                animate=animation.Animation(600, AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve='decelerate'),
                padding=padding.only(
                    top=50,
                    left=20,
                    right=20,
                    bottom=50
                ),
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

app(target=main, assets_dir='assets')
