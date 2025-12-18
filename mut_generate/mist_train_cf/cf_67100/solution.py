"""
QUESTION:
Design a mediator service that handles event logic and uses another service with RXJS Subjects to send update notifications to components. The mediator service and the RXJS Subjects service may have a circular dependency on each other. Determine if this circular relationship is acceptable and outline the potential consequences and considerations for maintaining good architectural decisions.

The function should consider the following restrictions:
- The mediator service handles event logic for components.
- The RXJS Subjects service sends update notifications to components.
- The mediator service and RXJS Subjects service may depend on each other.
- The goal is to facilitate communication between different parts of the application while maintaining clear boundaries of responsibility and low coupling among modules.
"""

class SubjectService:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class MediatorService:
    def __init__(self, subject_service):
        self.subject_service = subject_service

    def handle_event(self, event):
        # Handle event logic here
        print(f"Handling event: {event}")
        self.subject_service.notify(event)


class Component:
    def update(self, message):
        print(f"Received update: {message}")


def mediator_service(subject_service):
    return MediatorService(subject_service)


# To use the mediator service
subject_service = SubjectService()
mediator = mediator_service(subject_service)
component = Component()
subject_service.attach(component)
mediator.handle_event("Test Event")