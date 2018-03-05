
def test_count_fb_friends(app):
    app.friends.login()
    app.friends.open_friends_page()
    app.friends.check_friends()
    app.friends.scroll_page_count_friends()