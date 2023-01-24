"""
    Class for tracking what bot awaits from user.
    For example, user choices Work with audio -> Load as audio file
    Then bot will ignore other messages from that user until they upload audio file
"""


class UserSourcesInput:
    """
        Dictionary for users: inputs "user id": "[awaited sources]"
    """
    usersInputWaiter = {}

    def add_user_input_waiter(self, user_id, source):
        if self.is_wait_for_user_input(user_id):
            if not self.usersInputWaiter[user_id].__contains__(source):
                self.usersInputWaiter[user_id].append(source)
        else:
            self.usersInputWaiter[user_id] = [source]

    def is_wait_for_user_input(self, user_id):
        return self.usersInputWaiter.__contains__(user_id)

    def end_waiting_for_user_input(self, user_id, source):
        if self.is_wait_for_user_input(user_id):
            if self.usersInputWaiter[user_id].__contains__(source):
                self.usersInputWaiter[user_id].remove(source)


user_sources_input = UserSourcesInput()
