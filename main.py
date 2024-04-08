from flet import *

def main (page: Page):
    BG = '#243e36'
    FWG = '#7ca982'
    FG = '#f1f7ed'
    PINK = '#e8998d' 

    first_page_contents = Container(
        content=Column(
            controls=[
                Row( alignment='spaceBetween', # spaces the children below. 
                    controls=[
                        Container(
                            content=Icon(
                                icons.Menu)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]       
                )
            ]
        )
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
    page.add(container)

app(target=main)
