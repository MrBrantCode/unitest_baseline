"""
QUESTION:
Implement a `share` function that allows users to share a message via multiple platforms (email, Facebook, Twitter, and LinkedIn). The system should be designed for easy addition or removal of sharing options and flexible enough to adjust to changes in the sharing APIs.

The function should take two parameters: `message` and `platform`. The `platform` parameter should be a string representing the desired sharing platform. The system should use an object-oriented approach to allow for extensibility.

The `share` function should not contain the actual sharing logic, but instead use a strategy pattern to delegate the sharing to the corresponding platform-specific strategy class. 

The solution should include unit tests to confirm the correct functionality of the code. The tests should mock the third-party services to simulate their behavior.
"""

from abc import ABC, abstractmethod

class ShareStrategy(ABC):
    @abstractmethod
    def share(self, message):
        """Shares a message on a specific platform"""
        pass

class EmailShareStrategy(ShareStrategy):
    def share(self, message):
        # logic to share on email using email APIs
        return f"Shared '{message}' on email"

class FacebookShareStrategy(ShareStrategy):
    def share(self, message):
        # logic to share on Facebook using Facebook APIs
        return f"Shared '{message}' on Facebook"

class TwitterShareStrategy(ShareStrategy):
    def share(self, message):
        # logic to share on Twitter using Twitter APIs
        return f"Shared '{message}' on Twitter"

class LinkedInShareStrategy(ShareStrategy):
    def share(self, message):
        # logic to share on LinkedIn using LinkedIn APIs
        return f"Shared '{message}' on LinkedIn"


class ShareContext:
    def __init__(self, strategy: ShareStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ShareStrategy):
        self.strategy = strategy

    def share(self, message):
        return self.strategy.share(message)


def share(message, platform):
    platforms = {
        "email": EmailShareStrategy(),
        "facebook": FacebookShareStrategy(),
        "twitter": TwitterShareStrategy(),
        "linkedin": LinkedInShareStrategy()
    }
    share_context = ShareContext(strategy=platforms.get(platform))
    return share_context.share(message) if share_context.strategy else f"Unsupported platform: {platform}"