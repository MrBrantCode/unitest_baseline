"""
QUESTION:
Implement a function called `propagate_span_context` that correctly propagates the span context across service boundaries to prevent the 'SpanContextCorrupted' error in a Jaeger tracing system. The function should take into account language-specific discrepancies, incorrect parent-child relationships, and improper trace context propagation.
"""

def propagate_span_context(span_context, trace_id, span_id, parent_id=None):
    """
    Propagates the span context across service boundaries to prevent 'SpanContextCorrupted' error.

    Args:
        span_context (dict): The current span context.
        trace_id (str): The ID of the trace.
        span_id (str): The ID of the span.
        parent_id (str, optional): The ID of the parent span. Defaults to None.

    Returns:
        dict: The updated span context.
    """
    # Create a new span context if it doesn't exist
    if not span_context:
        span_context = {}

    # Set the trace ID
    span_context['trace_id'] = trace_id

    # Set the span ID
    span_context['span_id'] = span_id

    # Set the parent ID if provided
    if parent_id:
        span_context['parent_id'] = parent_id

    # Ensure the correct propagation of the trace context
    span_context['trace_flags'] = 0x1  # Set the sampled flag

    return span_context