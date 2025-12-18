"""
QUESTION:
Create a function `pos_tagging_workflow(tagger, save_dir, sample_sentence, test_dataset_path)` that loads a pre-trained POS tagger model from the specified directory `save_dir`, uses the model to tag the given `sample_sentence`, evaluates the model's performance on a test dataset located at `test_dataset_path`, and saves the model in the directory `save_dir`. The function should handle potential errors and return the tagged sample sentence along with a message indicating the success or failure of the workflow.
"""

def entrance(tagger, save_dir, sample_sentence, test_dataset_path):
    try:
        # Step 1: Load the pre-trained model
        tagger.load(save_dir)

        # Step 2: Tag the sample sentence using the loaded model
        tagged_sentence = tagger(sample_sentence)

        # Step 3: Evaluate the model's performance on the test dataset
        tagger.evaluate(test_dataset_path, save_dir=save_dir)

        # Step 4: Save the model in the specified directory
        tagger.save(save_dir)

        return tagged_sentence, "POS tagging workflow completed successfully."
    except FileNotFoundError:
        return None, "Error: The specified model directory does not exist."
    except Exception as e:
        return None, f"Error: An unexpected error occurred - {str(e)}"