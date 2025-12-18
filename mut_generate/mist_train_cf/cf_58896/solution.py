"""
QUESTION:
Prevent a window from stealing focus when the mouse hovers over it. 

Implement a function named `prevent_focus_stealing` that prevents a specified window from gaining focus when the mouse pointer is moved over it, using either the Windows API or a scripting language. The function should take the window's title as input and prevent it from stealing focus.
"""

import ctypes
from ctypes import wintypes

def prevent_focus_stealing(window_title):
    """
    Prevents a specified window from gaining focus when the mouse pointer is moved over it.

    Args:
    window_title (str): The title of the window to prevent from stealing focus.
    """
    
    # Get the window handle by title
    hwnd = ctypes.windll.user32.FindWindowW(None, window_title)
    
    if hwnd:
        # Define the WH_CBT hook type
        WH_CBT = 5
        
        # Define the HCBT_SETFOCUS hook code
        HCBT_SETFOCUS = 9
        
        # Define the SetWindowsHookEx function
        SetWindowsHookEx = ctypes.windll.user32.SetWindowsHookExW
        SetWindowsHookEx.argtypes = [wintypes.INT, wintypes.HOOKPROC, wintypes.HINSTANCE, wintypes.DWORD]
        SetWindowsHookEx.restype = wintypes.HHOOK
        
        # Define the hook procedure
        def hook_proc(nCode, wParam, lParam):
            if nCode == HCBT_SETFOCUS and lParam == hwnd:
                # Prevent the window from gaining focus
                return 1
            return ctypes.windll.user32.CallNextHookEx(None, nCode, wParam, lParam)
        
        # Set the hook
        hook = SetWindowsHookEx(WH_CBT, hook_proc, None, 0)
        
        # Unhook when the function is finished
        ctypes.windll.user32.UnhookWindowsHookEx(hook)