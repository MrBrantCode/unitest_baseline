"""
QUESTION:
Implement the `get_sentence_frame_acc` function, which calculates the accuracy of predicting intent and slot labels in a natural language processing task. The function takes four parameters: `intent_preds`, `intent_labels`, `slot_preds`, and `slot_labels`, all of which are lists of strings representing predicted and true intent and slot labels. The function returns a dictionary with two keys: "intent_accuracy" and "slot_accuracy", representing the accuracy of intent and slot label predictions, respectively. The accuracy is calculated as the percentage of correctly predicted labels, and it should handle cases where the input lists are empty.
"""

from typing import List, Dict

def get_sentence_frame_acc(
    intent_preds: List[str],
    intent_labels: List[str],
    slot_preds: List[List[str]],
    slot_labels: List[List[str]],
) -> Dict[str, float]:
    # Calculate intent accuracy
    intent_correct = sum(1 for pred, label in zip(intent_preds, intent_labels) if pred == label)
    intent_accuracy = intent_correct / len(intent_labels) if intent_labels else 0.0

    # Calculate slot accuracy
    slot_correct = 0
    total_slots = 0
    for pred_seq, label_seq in zip(slot_preds, slot_labels):
        for pred, label in zip(pred_seq, label_seq):
            total_slots += 1
            if pred == label:
                slot_correct += 1
    slot_accuracy = slot_correct / total_slots if total_slots else 0.0

    return {"intent_accuracy": intent_accuracy, "slot_accuracy": slot_accuracy}