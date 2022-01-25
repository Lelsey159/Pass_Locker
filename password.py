class Password:
    def __init__(self, page, password):
        self.page = page
        self.password = password

    user_passwords = []

    def save_page(self):
        Password.user_passwords.append(self)

    def delete_page(self):
        Password.user_passwords.remove(self)

    @classmethod
    def display_page(cls):
        return cls.user_passwords

    @classmethod
    def find_by_page(cls, pager):
        for pagy in cls.user_passwords:
            if pagy.page == pager:
                return pagy

    @classmethod
    def page_exists(cls, pager):
        for pagy in cls.user_passwords:
            if pagy.page == pager:
                return pagy
        return False