
class ClickHelper:

    def _fill(self, elem, val):
        e = elem()
        e.click()
        e.clear()
        e.send_keys(val)