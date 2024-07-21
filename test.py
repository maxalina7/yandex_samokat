import data
import sender_request


def get_order_track_status_code():
    response_code = sender_request.post_new_order(data.order_body)
    track = response_code.json()["track"]
    return sender_request.get_order_track(track).status_code


def test_get_order_track_code_200():
    assert get_order_track_status_code() == 200
