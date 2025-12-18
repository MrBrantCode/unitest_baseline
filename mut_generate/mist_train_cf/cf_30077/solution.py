"""
QUESTION:
Create a function named `handle_with_retry` that takes a consumer object, a message, and the maximum number of retries as input. The function should attempt to handle the message using the consumer's handle method, retrying up to the specified maximum number of retries if an error occurs. If successful, it should return the result. If all retries fail, it should raise a custom MaxRetryException. 

The function should utilize the consumer's pre_handle, handle, and post_handle methods, as well as the channel's basic_ack, basic_reject, and basic_nack methods for message acknowledgment and rejection.
"""

class MaxRetryException(Exception):
    pass

def handle_with_retry(consumer, message, max_retries):
    for _ in range(max_retries + 1):
        try:
            consumer.pre_handle()
            result = consumer.handle(message)
            consumer.post_handle()
            consumer.channel.basic_ack(delivery_tag=message.delivery_tag)
            return result
        except Exception as e:
            if _ == max_retries:
                consumer.channel.basic_nack(delivery_tag=message.delivery_tag, requeue=False)
                raise MaxRetryException("Max retries exceeded") from e
            else:
                consumer.channel.basic_nack(delivery_tag=message.delivery_tag, requeue=True)