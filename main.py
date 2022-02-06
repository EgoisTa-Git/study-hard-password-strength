import urwid


def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not char.isdigit() and not char.isalpha() for char in password)


def pass_strength(edit, password, field):
    checks = (
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    )
    score = 0
    for check in checks:
        score += 2 * check(password)
    field.set_text(f'Рейтинг пароля: {score}')


def on_click_exit(button):
    raise urwid.ExitMainLoop()


def main():
    palette = [
        ('banner', 'bold, black', 'light gray'),
        ('button', 'bold, black', 'dark gray'),
    ]
    welcome = urwid.Text('Проверка сложности пароля', align='center')
    password = urwid.Edit('Введите пароль: ', mask = '*', align='left')
    rating = urwid.Text('Рейтинг пароля: ', align='center')
    rating_field = urwid.LineBox(urwid.AttrMap(rating, 'banner'))
    button = urwid.Button('ВЫХОД')
    content = urwid.LineBox(
        urwid.Pile(
            [
                welcome,
                urwid.Divider(),
                password,
                urwid.Divider(),
                rating_field,
                urwid.Divider(),
                urwid.GridFlow(
                    [urwid.AttrMap(button, 'button')],
                    cell_width = 9,
                    h_sep = 0,
                    v_sep = 0,
                    align = 'center',
                ),
            ]
        )
    )
    fill = urwid.Filler(content, valign = 'top', top = 2)
    urwid.connect_signal(button, 'click', on_click_exit)
    urwid.connect_signal(password, 'change', pass_strength, rating)
    urwid.MainLoop(fill, palette).run()


if __name__ == '__main__':
    main()
    