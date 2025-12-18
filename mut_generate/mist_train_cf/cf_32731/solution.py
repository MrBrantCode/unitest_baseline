"""
QUESTION:
Write a function `get_download_progress` that takes an `update_status` and a `download_progress` as input and returns the correct download progress value based on the `update_status`. The `update_status` can be one of the following: `UPDATE_STATUS_IDLE`, `UPDATE_STATUS_CHECKING_FOR_UPDATE`, `UPDATE_STATUS_UPDATE_AVAILABLE`, `UPDATE_STATUS_DOWNLOADING`, `UPDATE_STATUS_VERIFYING`, `UPDATE_STATUS_FINALIZING`, `UPDATE_STATUS_NEED_REBOOT`, `UPDATE_STATUS_UPDATED`, or `UPDATE_STATUS_ERROR`. The function should return 0 when the `update_status` is `UPDATE_STATUS_ERROR`, and it should also return 0 when the download has finished (i.e., `download_progress` is 1) and the `update_status` is `UPDATE_STATUS_VERIFYING`, `UPDATE_STATUS_FINALIZING`, or `UPDATE_STATUS_NEED_REBOOT`. For all other cases, the function should return the `download_progress`.
"""

from enum import Enum

class UpdateStatus(Enum):
    UPDATE_STATUS_IDLE = 1
    UPDATE_STATUS_CHECKING_FOR_UPDATE = 2
    UPDATE_STATUS_UPDATE_AVAILABLE = 3
    UPDATE_STATUS_DOWNLOADING = 4
    UPDATE_STATUS_VERIFYING = 5
    UPDATE_STATUS_FINALIZING = 6
    UPDATE_STATUS_NEED_REBOOT = 7
    UPDATE_STATUS_UPDATED = 8
    UPDATE_STATUS_ERROR = 9

def get_download_progress(update_status, download_progress):
    if update_status == UpdateStatus.UPDATE_STATUS_ERROR:
        return 0  
    elif (update_status == UpdateStatus.UPDATE_STATUS_VERIFYING or 
          update_status == UpdateStatus.UPDATE_STATUS_FINALIZING or 
          update_status == UpdateStatus.UPDATE_STATUS_NEED_REBOOT) and download_progress == 1:
        return 1  
    else:
        return download_progress