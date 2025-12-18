"""
QUESTION:
Implement the function `update_datasets` that takes in the following parameters: 
- `datasets_f`: A 3D array representing features of the datasets.
- `datasets_l`: A 3D array representing labels of the datasets.
- `cont`: A 2D array used to keep track of the count of data for each class and camera.
- `progress_cams`: An integer representing the progress of processing the cameras.
- `datasets_s`: A 3D array representing the size of datasets for each class and camera.
- `cam_video_count`: A 2D array representing the count of videos for each class and camera.
- `amount_datas`: An integer representing the amount of data to be processed.
- `predictions`: A 2D array representing the predicted values.
- `truth`: A 2D array representing the ground truth values.
- `nb_datas`: An integer representing the number of data samples.
- `cam`: An integer representing the camera index.
- `classe`: An integer representing the class index.

The function should update the dataset-related data structures based on the given inputs and return the updated `datasets_f`, `datasets_l`, `cont`, `progress_cams`, `datasets_s`, and `cam_video_count`. 

Restrictions: The function should perform the updates in the following order: 
1. Update the features and labels arrays with the provided `predictions` and `truth` for a specific class and camera.
2. Update the count of data for the specified class and camera in the `cont` array.
3. Update the progress of processing the cameras (`progress_cams`) by adding the `amount_datas`.
4. Update the size of datasets for the specified class and camera in the `datasets_s` array.
5. Update the count of videos for the specified class and camera in the `cam_video_count` array.
"""

def update_datasets(datasets_f, datasets_l, cont, progress_cams, datasets_s, cam_video_count, amount_datas, predictions, truth, nb_datas, cam, classe):
    datasets_f[classe][cam][cont[classe][cam]:cont[classe][cam]+amount_datas, :] = predictions
    datasets_l[classe][cam][cont[classe][cam]:cont[classe][cam]+amount_datas, :] = truth
    cont[classe][cam] += amount_datas
    progress_cams += amount_datas
    datasets_s[classe][cam][cam_video_count[classe][cam]] = nb_datas
    cam_video_count[classe][cam] += 1
    return datasets_f, datasets_l, cont, progress_cams, datasets_s, cam_video_count