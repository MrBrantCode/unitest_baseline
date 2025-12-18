"""
QUESTION:
Create a function `get_message` that takes a response code as input and returns its associated message from the following list of response codes and messages:
- FIND_ID_SUCCESS: "ID 찾기 성공"
- FIND_ID_FAILED: "ID 찾기 실패"
- FIND_PW_SUCCESS: "PW 찾기 성공"
- FIND_PW_FAILED: "PW 찾기 실패"
- RESET_PW_SUCCESS: "비밀번호 초기화 성공"
- RESET_PW_FAILED: "비밀번호 초기화 실패"
- RESET_PW_EXPIRED: "만료된 초기화 링크"
- RESET_PW_MAIL_SUCCESS: "비밀번호 초기화 이메일 전송 성공"

If an invalid response code is provided, the function should return a default "Unknown response code" message.
"""

def get_message(response_code):
    messages = {
        1: "ID 찾기 성공",
        2: "ID 찾기 실패",
        3: "PW 찾기 성공",
        4: "PW 찾기 실패",
        5: "비밀번호 초기화 성공",
        6: "비밀번호 초기화 실패",
        7: "만료된 초기화 링크",
        8: "비밀번호 초기화 이메일 전송 성공"
    }
    return messages.get(response_code, "Unknown response code")